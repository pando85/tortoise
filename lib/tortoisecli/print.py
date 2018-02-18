class beautyPrint():
    @classmethod
    def print(cls, result, resource):
        return getattr(cls, resource)(result)

    @classmethod
    def task(cls, result):
        output = ''
        for task in result:
            output += f"- *{task['name']}*\n"
            if task['description']:
                output += f"   `{task['description']}`\n"

            if task['deadline']:
                output += f"   Limit:{task['deadline']}\n"

            if task['tags']:
                output += f"    tags:{task['tags']}\n"

            if task['members']:
                output += f"    members:{task['members']}\n"
            output += "\n"

        print(output)
