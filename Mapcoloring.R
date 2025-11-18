library(tidyverse)
library(sf)
library(leaflet)
library(maps)
library(tmaptools)
library(plotly)

# Read in Data
greedy1 <- read_csv("greedy1.csv")
# Format to Long
greedy1 <- greedy1 |>
pivot_longer(
    cols =  everything(),
    names_to = "State",
    values_to = "Color"
  )
# Add State abbreviations for plotly
greedy1 <- greedy1 |> mutate(abbrev = state.abb)

# Create Map
map <- plot_geo(
  greedy1,
  type = "choropleth",
  locations = ~abbrev,
  z = ~Color,
  locationmode = "USA-states"
  ) |> layout(title = "Map Coloring: Greedy Algorithm 1", 
          geo = list(scope = "usa")) 
# Display Map
map

# Read in Data
greedy2 <- read_csv("greedy2.csv")
# Format to Long
greedy2 <- greedy2 |>
  pivot_longer(
    cols =  everything(),
    names_to = "State",
    values_to = "Color"
  )

greedy2 <- greedy2[order(greedy2$State),]
# Add State abbreviations for plotly
greedy2 <- greedy2 |> mutate(abbrev = state.abb)


# Create Map
map2 <- plot_geo(
  greedy2,
  type = "choropleth",
  locations = ~abbrev,
  z = ~Color,
  locationmode = "USA-states"
) |> layout(title = "Map Coloring: Greedy Algorithm 2", 
            geo = list(scope = "usa"))
# Display Map
map2


