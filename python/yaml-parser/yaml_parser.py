import yaml

with open("input.yaml", 'r') as stream:
    try:
        yaml_data = yaml.safe_load(stream)
        #print(yaml_data)

        employee_1 = yaml_data["employee_1"]
        #print(employee_1)

        name = yaml_data["employee_1"]["Name"]
        age =  yaml_data["employee_1"]["Age"]
        #print(name)
        #print(age)

        #company =  yaml_data["employee_1"]["Company"]
        #print(company)

        # Responsibilities_list = yaml_data["employee_1"]["Responsibilities_list"]
        # print(Responsibilities_list)

        # for responsibility in Responsibilities_list:
        #     print(responsibility)

        # Languages_NestedList = yaml_data["employee_1"]["Languages_NestedList"]
        # print(Languages_NestedList)
        
        # for languages in Languages_NestedList:
        #     print(languages)

        # for languages in Languages_NestedList:
        #     for language in languages:
        #         print(language)

        Education = yaml_data["employee_1"]["Education"]
        print(Education)

        bachelor_gpa = yaml_data["employee_1"]["Education"]["Bachelors"]["GPA"]
        print(bachelor_gpa)
    except yaml.YAMLError as exc:
        print(exc)