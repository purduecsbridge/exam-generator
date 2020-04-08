import glob
import jinja2
import os
import random
import shutil
import subprocess
import yaml

latex_env = jinja2.Environment(
  block_start_string = '\\BLOCK{',
	block_end_string = '}',
	variable_start_string = '\\VAR{',
	variable_end_string = '}',
	comment_start_string = '\\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

questions = []

q_path = './questions'
for filename in glob.glob(os.path.join(q_path, '*.yml')):
	with open(filename) as file:
		question = yaml.load(file, Loader=yaml.FullLoader)
		questions.append(question)

random.shuffle(questions)

env = {
	"questions": questions
}

if not os.path.exists('./out'):
	os.makedirs('./out')

for file in glob.glob(r'*.tex'):
    shutil.copy(file, './out')
os.chdir('./out')

template = latex_env.get_template('main.tex')
tex = template.render(env)

with open('exam-solution.tex', 'w') as f:
	f.write(tex)

subprocess.call(['tectonic', 'exam-solution.tex'])

with open('exam.tex', 'w') as f:
	f.write(tex.replace(r'\Ans', ''))

subprocess.call(['tectonic', 'exam.tex'])
