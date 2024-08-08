import week_7_assignment as w7a
# import input_data.week_7_assignments_data as data_in


# PROBLEM 1: Data Analysis with Pandas
#################################################
# Instantiate parser objects:
my_white_pages_parser = w7a.WhitePagesParser("./course_2_intermediate_python/week_7/assignments/input_data/white_pages.txt")
my_yellow_pages_parser = w7a.YellowPagesParser("./course_2_intermediate_python/week_7/assignments/input_data/yellow_pages.txt")
my_company_pages_parser = w7a.CompanyPagesParser("./course_2_intermediate_python/week_7/assignments/input_data/company_pages.txt")

# Parse entire all 3 pages text files and write all 100/20/20 records to csv files:
my_white_pages_parser.to_csv(my_white_pages_parser.pages_tbl, "./course_2_intermediate_python/week_7/assignments/output_data/white_pages.csv")
my_yellow_pages_parser.to_csv(my_yellow_pages_parser.pages_tbl, "./course_2_intermediate_python/week_7/assignments/output_data/yellow_pages.csv")
my_company_pages_parser.to_csv(my_company_pages_parser.pages_tbl, "./course_2_intermediate_python/week_7/assignments/output_data/company_pages.csv")

# Look for employees with the title "Software Engineer" in the company pages.  Write results to csv files:
title_software_engineer_list = my_company_pages_parser.pages_tbl_filter_by(title="software engineer")
my_company_pages_parser.to_csv(title_software_engineer_list, "./course_2_intermediate_python/week_7/assignments/output_data/company_pages_titles_software_engineer.csv")  

# Look for employee whose name is "Eduardo Garcia", in "miami".  Write result to csv file:
my_white_pages_parser.to_csv(my_white_pages_parser.pages_tbl_filter_by(name="EDUARDO GARCIA", address_city="miami"), "./course_2_intermediate_python/week_7/assignments/output_data/company_pages_tbl_filter_by_ed_gadcia.csv")

# Look for employee whose name is "Mei Chen", in "Orlando" with zip "32822".  Write result to csv file:
my_company_pages_parser.to_csv(my_company_pages_parser.pages_tbl_filter_by(name="mei chen", address_city="orlando", address_zip="32822"), "./course_2_intermediate_python/week_7/assignments/output_data/company_pages_tbl_filter_by_mei_chen.csv")



# Look for attorney businesses with no websites in zip 32501 or aread code 954. Write result to csv file.  This lookup was done in a prior week and it took to operations.  Note how now this can be done in a single operation after we've modified our classes to use Pandas DataFrame:
my_yellow_pages_parser.to_csv(  my_yellow_pages_parser.pages_tbl[   (my_yellow_pages_parser.pages_tbl.category == "attorneys") &
                                                                    (my_yellow_pages_parser.pages_tbl.website == '') &
                                                                    (   (my_yellow_pages_parser.pages_tbl.address_zip == "32501") | (my_yellow_pages_parser.pages_tbl.phone_area_code == "954") )   ],

                                "./course_2_intermediate_python/week_7/assignments/output_data/yellow_pages_attorneys_no_website_zip_32501_area_code_954.csv" )
