import os
import random
from openai import OpenAI
client = OpenAI()

def read_map_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def read_code_files(selected_lines):
    code_contents = []
    for line_number in selected_lines:
        file_path = f"code{line_number}.txt"
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                code_contents.append(file.read())
    return code_contents

def main():
    user_prompt = input("Enter a prompt: ")

    map_lines = read_map_file("map.txt")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
        ]
    )

    print(response.choices[0].message.content)


    selected_lines = random.sample(map_lines, k=random.randint(1, 2))

    print("Selected lines from map.txt:")
    for line in selected_lines:
        print(line.strip())

    code_contents = read_code_files(selected_lines)

    print("\nContent from relevant code files:")
    for idx, content in enumerate(code_contents, start=1):
        print(f"File {idx}:")
        print(content.strip())
        print()

if __name__ == "__main__":
    main()
