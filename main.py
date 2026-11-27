import os

# Bake Bread — one warm loaf, kneaded slow, set steaming on the judge's table.
TEXT = "Thank you. Morning found you reading, and no warm loaf has reached you yet. I kneaded the dough slow, let it rise, and baked it till the crust turned gold. Here it is on your table, still steaming, waiting to be cut. Break off a piece. The smell of fresh bread will stay in this room long after the last crumb is gone."

out_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', 'out')
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, 'entry.txt'), 'w') as f:
    f.write(TEXT)
