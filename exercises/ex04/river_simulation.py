from river import River

my_river = River(10, 2)

print("Initial state:")
my_river.view_river()

my_river.one_river_week()

print("\nAfter one week:")
my_river.view_river()
