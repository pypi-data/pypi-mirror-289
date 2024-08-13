import os
import argparse


stats_arcog_usage = '''
================================== stats_arcog example commands ==================================

BioSAK stats_arcog -ko ko_d.txt -db ko00001.keg -p Demo

# Required DB files:

==================================================================================================
'''


def cog_stats_to_txt(ko_stats_dict, ko_desc_dict, op_txt, op_stats_txt):
    op_txt_handle = open(op_txt, 'w')
    op_stats_txt_handle = open(op_stats_txt, 'w')
    for ko_high in sorted(list(ko_stats_dict.keys())):
        ko_d_set = ko_stats_dict[ko_high]
        ko_high_desc = ko_desc_dict[ko_high]
        op_stats_txt_handle.write('%s\t%s\t%s\n' % (ko_high, len(ko_d_set), ko_high_desc))
        for ko_d in sorted(list(ko_d_set)):
            ko_d_desc = ko_desc_dict[ko_d]
            op_txt_handle.write('%s__%s\t%s__%s\n' % (ko_high, ko_high_desc.strip(), ko_d, ko_d_desc.strip()))
    op_txt_handle.close()
    op_stats_txt_handle.close()


def stats_arcog(args):

    cog_txt             = args['cog']
    op_dir              = args['o']
    db_dir              = args['db']
    force_create_op_dir = args['f']

    ####################################################################################################################

    cog_des_txt     = '%s/arCOGdef.tab'         % db_dir
    pwd_fun_20_tab  = '%s/fun-20.tab'           % db_dir
    op_txt          = '%s/COG_cate.txt'         % op_dir
    op_stats_txt    = '%s/COG_cate_stats.txt'   % op_dir

    if os.path.isdir(op_dir) is True:
        if force_create_op_dir is True:
            os.system('rm -r %s' % op_dir)
        else:
            print('Output folder detected, program exited!')
            exit()
    os.system('mkdir %s' % op_dir)

    ############################################## Read in KEGG DB files ###############################################

    print('Read in arCOG DB files')

    cog_id_to_category_dict = dict()
    cog_id_to_description_dict = dict()
    for each_cog in open(cog_des_txt, encoding="ISO-8859-1"):
        each_cog_split = each_cog.strip().split('\t')
        cog_id = each_cog_split[0]
        cog_cate_str = each_cog_split[1]
        cog_cate_split = [i for i in cog_cate_str]
        cog_desc = each_cog_split[3]
        cog_id_to_description_dict[cog_id] = cog_desc
        cog_id_to_category_dict[cog_id] = cog_cate_split

    cog_category_to_description_dict = {}
    for cog_category in open(pwd_fun_20_tab):
        cog_category_split = cog_category.strip().split('\t')
        cog_category_to_description_dict[cog_category_split[0]] = cog_category_split[2]

    ########################################################################################################################

    ko_a_stats_dict = dict()
    ko_b_stats_dict = dict()
    ko_c_stats_dict = dict()
    for each_ko in open(cog_txt):
        each_ko_split = each_ko.strip().split('\t')
        ko_id = each_ko_split[0]
        ko_abcd_list = D2ABCD_dict.get(ko_id, [])
        for ko_abcd in ko_abcd_list:
            ko_abcd_split = ko_abcd.split('|')
            ko_a = ko_abcd_split[0][2:]
            ko_b = ko_abcd_split[1][2:]
            ko_c = ko_abcd_split[2][2:]
            if ko_a not in ko_a_stats_dict:
                ko_a_stats_dict[ko_a] = set()
            if ko_b not in ko_b_stats_dict:
                ko_b_stats_dict[ko_b] = set()
            if ko_c not in ko_c_stats_dict:
                ko_c_stats_dict[ko_c] = set()
            ko_a_stats_dict[ko_a].add(ko_id)
            ko_b_stats_dict[ko_b].add(ko_id)
            ko_c_stats_dict[ko_c].add(ko_id)

    cog_stats_to_txt(ko_a_stats_dict, ABCD_description_dict, op_a_txt, op_a_stats_txt)
    cog_stats_to_txt(ko_b_stats_dict, ABCD_description_dict, op_b_txt, op_b_stats_txt)
    cog_stats_to_txt(ko_c_stats_dict, ABCD_description_dict, op_c_txt, op_c_stats_txt)

    print('Done!')


if __name__ == "__main__":

    stats_arcog_parser = argparse.ArgumentParser(usage=stats_arcog_usage)
    stats_arcog_parser.add_argument('-cog',   required=True,                          help='cog_ids.txt')
    stats_arcog_parser.add_argument('-db',    required=True,                          help='ko00001.keg')
    stats_arcog_parser.add_argument('-o',     required=True,                          help='output directory')
    stats_arcog_parser.add_argument('-f',     required=False, action="store_true",    help='force overwrite')
    args = vars(stats_arcog_parser.parse_args())
    stats_arcog(args)
