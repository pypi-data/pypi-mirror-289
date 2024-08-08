import subprocess
import os
import sys
from deploybot.utils.config import get_config
from deploybot.utils.parser import extract_stack_name

def git_command(command, cwd, capture_output=True, check=True):
    result = subprocess.run(command, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if capture_output:
        print(result.stdout)
    if result.returncode != 0 and check:
        raise subprocess.CalledProcessError(result.returncode, command, output=result.stdout, stderr=result.stderr)
    return result

def pull_latest_changes(base_path):
    try:
        git_command(['git', 'pull'], cwd=base_path)
        print("Git pull successful.")
    except subprocess.CalledProcessError as e:
        print("Git pull failed: {}".format(e))
        print("Detailed error log: {}".format(e.stderr))
        print("Please resolve the conflicts manually or stash your changes and clean untracked files before retrying.")
        return False
    return True

def switch_branch(base_path, target_branch):
    try:
        git_command(['git', 'checkout', target_branch], cwd=base_path)
        print("Switched to branch: {}".format(target_branch))
    except subprocess.CalledProcessError as e:
        print("Failed to switch to branch: {}. Stashing changes and retrying...".format(target_branch))
        git_command(['git', 'stash'], cwd=base_path)
        try:
            git_command(['git', 'checkout', target_branch], cwd=base_path)
            print("Switched to branch: {} after stashing changes.".format(target_branch))
        except subprocess.CalledProcessError as retry_e:
            print("Failed to switch to branch after stashing: {}".format(retry_e))
            print("Detailed error log: {}".format(retry_e.stderr))
            return False

    return pull_latest_changes(base_path)

def check_and_switch_branch(environment, base_path):
    try:
        current_branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], cwd=base_path, universal_newlines=True).strip()
        target_branch = 'dev' if environment == 'staging' else 'master'

        print("Environment: {}".format(environment))
        print("Current Branch: {}".format(current_branch))

        if current_branch != target_branch:
            if not switch_branch(base_path, target_branch):
                return False
            current_branch = target_branch
        else:
            if not pull_latest_changes(base_path):
                return False

        if (environment == 'staging' and current_branch != 'dev') or (environment == 'production' and current_branch != 'master'):
            print("Warning: {} environment selected but branch is {}. Exiting.".format(environment, current_branch))
            return False

        print("Branch check passed for environment {} and branch {}".format(environment, current_branch))
        os.environ['BUILDKITE_BRANCH'] = current_branch
        return True
    except subprocess.CalledProcessError as e:
        print("Failed to determine current branch: {}".format(e))
        return False

def run_script(script_path, env_vars, base_path):
    script_dir = os.path.dirname(script_path)
    script_name = os.path.basename(script_path)
    env_vars['LC_ALL'] = 'en_US.UTF-8'
    env_vars['LANG'] = 'en_US.UTF-8'
    env_vars['ENV'] = env_vars['ENVIRONMENT']
    try:
        process = subprocess.Popen(
            ['bash', '-c', 'cd {} && bash {}/{}'.format(base_path, script_dir, script_name)],
            env=env_vars,
            stdout=sys.stdout,
            stderr=sys.stderr
        )
        process.communicate()
        return process.returncode
    except KeyboardInterrupt:
        print("\nScript execution cancelled by user.")
        sys.exit(0)

def set_environment_variables(config):
    environment = config['DEFAULT']['environment']
    aws_account_id = config['DEFAULT']['aws_account_id']
    sam_deployment_bucket = config['DEFAULT']['sam_deployment_bucket']
    buildkite_org_slug = config['DEFAULT']['buildkite_org_slug']
    buildkite_pipeline_slug = config['DEFAULT']['buildkite_pipeline_slug']

    if not environment or not aws_account_id or not sam_deployment_bucket or not buildkite_org_slug or not buildkite_pipeline_slug:
        print("Configuration not found. Please run 'deploybot configure' first.")
        sys.exit(1)

    os.environ['ENVIRONMENT'] = environment
    os.environ['AWS_ACCOUNT_ID'] = aws_account_id
    os.environ['SAM_DEPLOYMENT_BUCKET'] = sam_deployment_bucket
    os.environ['BUILDKITE_ORG_SLUG'] = buildkite_org_slug
    os.environ['BUILDKITE_PIPELINE_SLUG'] = buildkite_pipeline_slug

def deploy(service_type, action, service_name):
    print(f"Starting deploy function with action: {action}, service_type: {service_type}, service_name: {service_name}")
    
    if action not in ['deploy']:
        print("Invalid action. Only 'deploy' is supported.")
        return
    
    config = get_config()
    set_environment_variables(config)
    environment = config['DEFAULT']['environment']
    base_path = config['DEFAULT']['base_path']

    if environment not in ['production', 'staging']:
        print("Invalid environment.")
        return

    env_path = f"{base_path}/service"
    
    if service_type == 'ecs':
        if service_name == 'auth':
            build_script_path = '{}/auth/api/.buildkite/scripts/docker-build'.format(env_path)
            deploy_script_path = '{}/auth/api/.buildkite/scripts/deploy'.format(env_path)
        else:
            build_script_path = '{}/{}/.buildkite/scripts/docker-build'.format(env_path, service_name)
            deploy_script_path = '{}/{}/.buildkite/scripts/deploy'.format(env_path, service_name)

    elif service_type == 'lambda':
        if service_name == 'auth':
            lambda_path = 'auth/lambda'
            deploy_script_name = 'deploy-lambdas'
        elif service_name.startswith('echo-auth-channels'):
            lambda_path = f"auth/{service_name}"
            deploy_script_name = 'deploy-lambdas'
        else:
            lambda_path = f"lambda/{service_name}"
            deploy_script_name = 'deploy'

        deploy_script_path = f"{env_path}/{lambda_path}/.buildkite/scripts/{deploy_script_name}"
        check_versioning_script_path = f"{env_path}/{lambda_path}/.buildkite/scripts/check-versioning"
        
        stack_name = extract_stack_name(f"{env_path}/{lambda_path}/template.yaml", environment)
        if not stack_name:
            print("Stack name not found in the template.")
            return
        os.environ['STACK_NAME'] = stack_name
        
        # Run S3 copy command before executing the deploy script
        s3_command = (f"aws s3 cp s3://{os.environ['SAM_DEPLOYMENT_BUCKET']}/{environment}/buildkite/sam/config/"
                      f"{os.environ['BUILDKITE_ORG_SLUG']}/{os.environ['BUILDKITE_PIPELINE_SLUG']}/"
                      f"{stack_name}/samconfig.toml {env_path}/{lambda_path}/samconfig.toml")
        try:
            subprocess.run(s3_command, shell=True, check=True)
            print("SAM config copied successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to copy SAM config: {e}")
            return
    else:
        print("Invalid service type. Only 'ecs' or 'lambda' are supported.")
        return

    if not check_and_switch_branch(environment, base_path):
        print("Branch check failed. Exiting action.")
        return

    if service_type == 'ecs':
        if not os.path.exists(build_script_path):
            print(f"Build script not found at {build_script_path}. Skipping build step.")
            build_script_path = None

        if not os.path.exists(deploy_script_path):
            print(f"Deploy script not found at {deploy_script_path}. Please provide the correct service name.")
            return

        if build_script_path:
            print(f"Running build script: {build_script_path}")
            run_script(build_script_path, os.environ, base_path)
        
        print(f"Running deploy script: {deploy_script_path}")
        run_script(deploy_script_path, os.environ, base_path)

    elif service_type == 'lambda':
        if not os.path.exists(deploy_script_path):
            print(f"Deploy script not found at {deploy_script_path}. Please provide the correct service name.")
            return

        print(f"Running deploy script: {deploy_script_path}")
        run_script(deploy_script_path, os.environ, base_path)

        if os.path.exists(check_versioning_script_path):
            print(f"Running check versioning script: {check_versioning_script_path}")
            run_script(check_versioning_script_path, os.environ, base_path)
        else:
            print(f"Check versioning script not found at {check_versioning_script_path}. Skipping this step.")

def migrate(db_type):
    config = get_config()
    set_environment_variables(config)
    environment = config['DEFAULT']['environment']
    base_path = config['DEFAULT']['base_path']
    
    if not check_and_switch_branch(environment, base_path):
        print("Branch check failed. Exiting action.")
        return

    script_path = '{}/.support/deploybot/migrate'.format(base_path)
    if db_type == 'mysql':
        if not os.path.exists(script_path):
            print("Migration script not found at: {}".format(script_path))
            return
        print("Running migration script for MySQL: {}".format(script_path))
        env_vars = os.environ.copy()
        run_script(script_path, env_vars, base_path)
    else:
        print("Invalid database type. Only 'mysql' is supported.")

def main_ecs(args):
    if args.action == 'deploy':
        deploy('ecs', args.action, args.service_name)
    else:
        print("Invalid action. Only 'deploy' is supported for ECS.")

def main_lambda(args):
    if args.action == 'deploy':
        deploy('lambda', args.action, args.service_name)
    else:
        print("Invalid action. Only 'deploy' is supported for Lambda.")

def main_migrate(args):
    migrate(args.db_type)
