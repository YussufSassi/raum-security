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
    toggled_to BOOLEAN NOT NULL,
    FOREIGN KEY (alarm_id) REFERENCES alarm(id)
);

CREATE TABLE intruder_detection_event (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    alarm_id INT NOT NULL,
    FOREIGN KEY (alarm_id) REFERENCES alarm(id)
);


CREATE TABLE schedule_alarm_toggle (
    id INT AUTO_INCREMENT PRIMARY KEY,
    toggle_alarm_at INT NOT NULL,
    toggle_alarm_to BOOLEAN NOT NULL,
    alarm_id INT NOT NULL,
    FOREIGN KEY (alarm_id) REFERENCES alarm(id)
);

CREATE TABLE `image` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `path` VARCHAR(255) NOT NULL,
    `timestamp` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (alarm_id) REFERENCES alarm(id)
);


CREATE INDEX idx_alarm_toggle_event_alarm_id ON alarm_toggle_event(alarm_id);
CREATE INDEX idx_intruder_detection_event_alarm_id ON intruder_detection_event(alarm_id);
CREATE INDEX idx_schedule_alarm_toggle_alarm_id ON schedule_alarm_toggle(alarm_id);