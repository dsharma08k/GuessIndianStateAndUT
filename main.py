import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian States and UTs Game")
image = "Indian States and UTs GIF.gif"
screen.bgpic(image)

data = pandas.read_csv("India States-UTs.csv")
all_options = data["State/UT"].tolist()
guessed_options = []

min_lat, max_lat = 6, 37
min_lon, max_lon = 68, 97

image_width, image_height = 600, 400

scale_x = image_width / (max_lon - min_lon)
scale_y = image_height / (max_lat - min_lat)

screen.setup(width=image_width, height=image_height)

def transform_coordinates(lat, lon):
    """Convert lat/lon to screen x/y based on scale and offsets."""
    x = (lon - min_lon) * scale_x - (image_width / 2)
    y = (lat - min_lat) * scale_y - (image_height / 2)
    return x, y


while len(guessed_options) < 37:
    answer_state = screen.textinput(title=f"{len(guessed_options)}/37 States or UTs Correct", prompt="What's another "
                    "State or UT name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_options if state not in guessed_options]
        pandas.DataFrame(missing_states).to_csv("areas_to_learn.csv")
        break

    if answer_state in all_options:
        guessed_options.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        area_data = data[data["State/UT"] == answer_state]

        lat = area_data.Latitude.item()
        lon = area_data.Longitude.item()
        screen_x, screen_y = transform_coordinates(lat, lon)

        t.goto(screen_x, screen_y)
        t.write(answer_state)
