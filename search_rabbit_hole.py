import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "category_tree_project.settings")
django.setup()

from category_tree.models import Category


def longest_rabbit_hole(start_cat, visited=None, curr_chain=None, max_chain=None):
    if visited is None:
        visited = set()
    if curr_chain is None:
        curr_chain = []
    if max_chain is None:
        max_chain = []

    visited.add(start_cat.id)
    curr_chain.append(start_cat)

    for similar_category in start_cat.similar_categories.all():
        if similar_category.id not in visited:
            longest_rabbit_hole(similar_category, visited, curr_chain, max_chain)

    if len(curr_chain) > len(max_chain):
        max_chain[:] = curr_chain[:]

    curr_chain.pop()

    return max_chain


def main():
    first_category = Category.objects.all()[0]

    find_longest_rabbit_hole = longest_rabbit_hole(first_category)

    print("Longest Rabbit Hole:")
    for category in find_longest_rabbit_hole:
        print(f"- {category.name}")


if __name__ == "__main__":
    main()


