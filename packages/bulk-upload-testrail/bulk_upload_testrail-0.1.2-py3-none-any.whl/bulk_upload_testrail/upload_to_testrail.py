import subprocess, sys, json
from testrail_api import TestRailAPI

project_name = sys.argv[1]
testrun_name = sys.argv[2]

def is_duplicate(list):
    if len(list) != len(set(list)):
        return True
    else:
        return False
    
def upload_to_testrail(project_id, milestone_id,suite_id, testrun_name, case_ids, username, password):

    api = TestRailAPI("https://amarthaqa.testrail.io/", "qa.eng@amartha.com", "Amartha2021")

    print("\n============= START TO CREATE TEST RUN ==============\n")

    run = api.runs.add_run(
        project_id=project_id,
        milestone_id=milestone_id,
        suite_id=suite_id,
        name=testrun_name,
        include_all= False,
        case_ids= case_ids
    )
    run_id = str(run['id'])
    print("TEST RUN : https://amarthaqa.testrail.io/index.php?/runs/view/" + run_id)
    print("\n============== SUCCESS CREATE TEST RUN ==============\n")
    print("=====================================================")
    print("=====================================================")
    print("\n========== START UPLOAD RESULT TO TESTRAIL ==========\n")
    subprocess.run('trcli -n -h https://amarthaqa.testrail.io --project "Amartha Automation Execution" --project-id '+project_id+' --username qa.eng@amartha.com --password Amartha2021 parse_junit --case-matcher "property" --title "'+testrun_name+'" --suite-id '+suite_id+' --milestone-id '+milestone_id+' --run-id '+run_id+' -f junit_report.xml', shell=True, check=True, timeout=240)
    print("=====================================================")
    print("=====================================================")

def read_json_file(path):
    with open(path, "r") as file:
        datum = json.load(file)
    return datum

dat = read_json_file("testrail_data.json")

project_id=dat[project_name+'_PROJECT_ID']
suite_id=dat[project_name+'_SUITE_ID']
testrun_name = '[Integrated][MOBILE] AFIN - '+testrun_name
milestone_id=dat[project_name+'_MILESTONE_ID']


##### Get Test ID From Running Automation #####
file = open("test_id_temp.txt", "r")

case_ids = file.read()
chars = ["'", ' ', '[', ']']
for i in chars:
    case_ids = case_ids.replace(i, '')
case_ids = case_ids.split(',')

file.close()
##########################################

if is_duplicate(case_ids):
    dup = {
        x for x in case_ids if case_ids.count(x) > 1
        }
    print("duplicates found in list : " + str(dup))
else:
    upload_to_testrail(project_id, milestone_id,suite_id, testrun_name, case_ids)