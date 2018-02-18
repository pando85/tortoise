class beautyPrint():
    @classmethod
    def print(cls, result, resource):
        result_list = result if type(result) is list else [result]
        output = getattr(cls, resource)(result_list)
        print(output)

    @classmethod
    def tag(cls, result):
        output = ""
        for tag in result:
            output += f"- *{tag['name']}*\n"
            output += "\n"
        return output

    @classmethod
    def task(cls, result):
        output = ""
        for task in result:
            output += f"- *{task['name']}*\n"
            if task['description']:
                output += f"   `{task['description']}`\n"

            if task['deadline']:
                output += f"   limit: {task['deadline']}\n"

            if task['tags']:
                output += f"    tags: {task['tags']}\n"

            if task['members']:
                output += f"    members: {task['members']}\n"
            output += "\n"
        return output

    @classmethod
    def user(cls, result):
        output = ""
        for user in result:
            output += f"- *{user['username']}*\n"

            if user['first_name']:
                output += f"    first_name: {user['first_name']}\n"

            if user['last_name']:
                output += f"    last_name: {user['last_name']}\n"

            if user['email']:
                output += f"    email: {user['email']}\n"

            if user['groups']:
                output += f"    groups: {user['groups']}\n"
            output += "\n"
        return output
