import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "category_tree_project.settings")
django.setup()

from category_tree.models import Category


def find_rabbit_islands(categories):
    visited = set()
    rabbit_islands = []

    def dfs(category, island):
        visited.add(category.id)
        island.append(category)

        for similar_category in category.similar_categories.all():
            if similar_category.id not in visited:
                dfs(similar_category, island)

    for category in categories:
        if category.id not in visited:
            island = []
            dfs(category, island)
            rabbit_islands.append(island)

    return rabbit_islands


def main():
    all_categories = Category.objects.all()
    rabbit_islands = find_rabbit_islands(all_categories)

    for i, island in enumerate(rabbit_islands, start=1):
        print(f"Rabbit Island {i}:")
        for category in island:
            print(f"- {category.name}")


if __name__ == "__main__":
    main()
