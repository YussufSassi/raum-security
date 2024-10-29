-- Create alarm table
CREATE TABLE alarm (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT FALSE,
    admin_id VARCHAR(255) NOT NULL
);

-- Create alarm_toggle_event table
CREATE TABLE alarm_toggle_event (
    id INT AUTO_INCREMENT PRIMARY KEY,
    alarm_id INT NOT NULL,
    timestamp DATETIME NOT NULL,
    FOREIGN KEY (alarm_id) REFERENCES alarm(id)
);

-- Add index on foreign key for better performance
CREATE INDEX idx_alarm_toggle_event_alarm_id ON alarm_toggle_event(alarm_id);