# ROS 2 Publisher-Subscriber Demo

A minimal ROS 2 Jazzy project demonstrating publisher and subscriber nodes written in Python.

## Nodes

- **publisher_node**: Publishes a float value and a string counter on two separate topics every 1 second
- **subscriber_node**: Subscribes to both topics and logs received messages

## Topics

| Topic | Type | Purpose |
|-------|------|---------|
| `/float_topic` | `std_msgs/Float32` | Float value incremented by 0.01 |
| `/string_topic` | `std_msgs/String` | Counter message |

## How to Run

**Terminal 1:**
```bash
ros2 run demo_pkg publisher_node
