CREATE TABLE IF NOT EXISTS dataset (
    school_name VARCHAR(100) NOT NULL,
    year INT NOT NULL,
    student_id INT NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100),
    year_level INT NOT NULL,
    class VARCHAR(50) NOT NULL,
    subject VARCHAR(50) NOT NULL,
    answer VARCHAR(1) NOT NULL,
    correct_answer VARCHAR(1) NOT NULL,
    question_number INT NOT NULL,
    subject_content VARCHAR(500),
    assessment_areas VARCHAR(500),
    sydney_correct_count_percentage DECIMAL(5, 2),
    sydney_average_score DECIMAL(5, 2),
    sydney_participants INT,
    student_score DECIMAL(5, 2),
    student_total_assessed INT,
    student_area_assessed_score DECIMAL(5, 2),
    total_area_assessed_score DECIMAL(5, 2),
    participant INT,
    correct_answer_percentage_per_class DECIMAL(5, 2),
    average_score DECIMAL(5, 2),
    school_percentile INT,
    sydney_percentile INT,
    strength_status VARCHAR(1),
    high_distinct_count INT,
    distinct_count INT,
    credit_count INT,
    participant_count INT,
    award VARCHAR(100)
);


LOAD DATA INFILE '/var/lib/mysql-files/dataset.csv'
INTO TABLE dataset
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
