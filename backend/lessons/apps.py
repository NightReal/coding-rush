from django.apps import AppConfig
import json
import os


# sorry, this is shitcode, but it works!

class LessonsConfig(AppConfig):
    name = 'lessons'

    def ready(self):
        from lessons.models import Lesson, Code

        lesson_paths = []
        code_paths = []
        for path, subdirs, files in os.walk('codes/'):
            for name in files:
                if name.startswith('c++') or name.startswith('python'):
                    code_paths.append('/'.join((path, name)))
                else:
                    lesson_paths.append('/'.join((path, name)))

        for full_path in lesson_paths:
            full_path_parts = full_path.split('/')
            if full_path_parts[-1] == 'metadata.json':
                with open(full_path, 'r') as html:
                    data = html.read()
                topic = full_path_parts[-3]
                name = full_path_parts[-2]
                j = json.loads(data)
                difficulty = j['difficulty']
                Lesson.objects.update_or_create(
                    title=name,
                    topic=topic,
                    defaults={'difficulty': difficulty}
                )
            elif full_path_parts[-1] == 'description.html':
                with open(full_path, 'r') as html:
                    data = html.read()
                topic = full_path_parts[-3]
                name = full_path_parts[-2]
                Lesson.objects.update_or_create(
                    title=name,
                    topic=topic,
                    defaults={'description': data}
                )

        for full_path in code_paths:
            full_path_parts = full_path.split('/')
            language = full_path_parts[-1].split('.')[0]
            topic = full_path_parts[-4]
            name = full_path_parts[-3]
            with open(full_path, 'r') as code:
                data = code.read()
            l = Lesson.objects.get(topic=topic, title=name)
            Code.objects.update_or_create(
                language=language,
                lesson=l,
                defaults={'code': data}
            )
