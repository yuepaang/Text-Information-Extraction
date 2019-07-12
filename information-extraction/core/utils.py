import logging
import argparse


def mark_entity(tag_seq, char_seq):
    entities = []
    temp = [0] * 12
    # temp = [0]
    temp[0] = get_ITM_dict(tag_seq, char_seq)  # return a list of dict or a empty list
    temp[1] = get_LOC_dict(tag_seq, char_seq)
    temp[2] = get_FRM_dict(tag_seq, char_seq)
    temp[3] = get_TO_dict(tag_seq, char_seq)
    temp[4] = get_TIM_dict(tag_seq, char_seq)
    temp[5] = get_ORG_dict(tag_seq, char_seq)
    temp[6] = get_TYP_dict(tag_seq, char_seq)
    temp[7] = get_VLM_dict(tag_seq, char_seq)
    temp[8] = get_DEP_dict(tag_seq, char_seq)
    temp[9] = get_ARR_dict(tag_seq, char_seq)
    temp[10] = get_DUR_dict(tag_seq, char_seq)
    temp[11] = get_PRC_dict(tag_seq, char_seq)
    for i in temp:
        if len(i) > 0:
            for d in i:
                entities.append(d)
    return entities


def get_ITM_dict(tag_seq, char_seq):
    length = len(char_seq)
    ITM = []
    # entity = dict()
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'B-ITM':
            if 'entity' in locals().keys():
                ITM.append(entity)
                del entity
            entity = dict()
            entity["entity"] = "consignment"
            entity["start"] = i
            entity["end"] = i
            entity["value"] = char
            if i+1 == length:
                ITM.append(entity)
        if tag == 'I-ITM':
            if 'entity' in locals().keys():
                entity["end"] += 1
                entity["value"] += char
            # else: itm = char
                if i+1 == length:
                    ITM.append(entity)
        if tag not in ['I-ITM', 'B-ITM']:
            if 'entity' in locals().keys():
                ITM.append(entity)
                del entity
            continue
    return ITM


def get_LOC_dict(tag_seq, char_seq):
    length = len(char_seq)
    LOC = []
    # entity = dict()
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'B-LOC':
            if 'entity' in locals().keys():
                LOC.append(entity)
                del entity
            entity = dict()
            entity["entity"] = "location"
            entity["start"] = i
            entity["end"] = i
            entity["value"] = char
            if i+1 == length:
                LOC.append(entity)
        if tag == 'I-LOC':
            if 'entity' in locals().keys():
                entity["end"] += 1
                entity["value"] += char
            # else: LOC = char
                if i+1 == length:
                    LOC.append(entity)
        if tag not in ['I-LOC', 'B-LOC']:
            if 'entity' in locals().keys():
                LOC.append(entity)
                del entity
            continue
    return LOC


def get_FRM_dict(tag_seq, char_seq):
    length = len(char_seq)
    FRM = []
    # entity = dict()
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'B-FRM':
            if 'entity' in locals().keys():
                FRM.append(entity)
                del entity
            entity = dict()
            entity["entity"] = "from"
            entity["start"] = i
            entity["end"] = i
            entity["value"] = char
            if i+1 == length:
                FRM.append(entity)
        if tag == 'I-FRM':
            if 'entity' in locals().keys():
                entity["end"] += 1
                entity["value"] += char
            # else: ITM = char
                if i+1 == length:
                    FRM.append(entity)
        if tag not in ['I-FRM', 'B-FRM']:
            if 'entity' in locals().keys():
                FRM.append(entity)
                del entity
            continue
    return FRM


def get_TO_dict(tag_seq, char_seq):
    length = len(char_seq)
    TO = []
    # entity = dict()
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'B-TO':
            if 'entity' in locals().keys():
                TO.append(entity)
                del entity
            entity = dict()
            entity["entity"] = "to"
            entity["start"] = i
            entity["end"] = i
            entity["value"] = char
            if i+1 == length:
                TO.append(entity)
        if tag == 'I-TO':
            if 'entity' in locals().keys():
                entity["end"] += 1
                entity["value"] += char
            # else: ITM = char
                if i+1 == length:
                    TO.append(entity)
        if tag not in ['I-TO', 'B-TO']:
            if 'entity' in locals().keys():
                TO.append(entity)
                del entity
            continue
    return TO


def get_TIM_dict(tag_seq, char_seq):
    length = len(char_seq)
    TIM = []
    # entity = dict()
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'B-TIM':
            if 'entity' in locals().keys():
                TIM.append(entity)
                del entity
            entity = dict()
            entity["entity"] = "time"
            entity["start"] = i
            entity["end"] = i
            entity["value"] = char
            if i+1 == length:
                TIM.append(entity)
        if tag == 'I-TIM':
            if 'entity' in locals().keys():
                entity["end"] += 1
                entity["value"] += char
            # else: ITM = char
                if i+1 == length:
                    TIM.append(entity)
        if tag not in ['I-TIM', 'B-TIM']:
            if 'entity' in locals().keys():
                TIM.append(entity)
                del entity
            continue
    return TIM


def get_ORG_dict(tag_seq, char_seq):
    length = len(char_seq)
    ORG = []
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'B-ORG':
            if 'entity' in locals().keys():
                ORG.append(entity)
                del entity
            entity = dict()
            entity["entity"] = "weight"
            entity["start"] = i
            entity["end"] = i
            entity["value"] = char
            if i+1 == length:
                ORG.append(entity)
        if tag == 'I-ORG':
            if 'entity' in locals().keys():
                entity["end"] += 1
                entity["value"] += char
            # else: ITM = char
                if i+1 == length:
                    ORG.append(entity)
        if tag not in ['I-ORG', 'B-ORG']:
            if 'entity' in locals().keys():
                ORG.append(entity)
                del entity
            continue
    return ORG


def get_TYP_dict(tag_seq, char_seq):
    length = len(char_seq)
    TYP = []
    # entity = dict()
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'B-TYP':
            if 'entity' in locals().keys():
                TYP.append(entity)
                del entity
            entity = dict()
            entity["entity"] = "type"
            entity["start"] = i
            entity["end"] = i
            entity["value"] = char
            if i+1 == length:
                TYP.append(entity)
        if tag == 'I-TYP':
            if 'entity' in locals().keys():
                entity["end"] += 1
                entity["value"] += char
            # else: ITM = char
                if i+1 == length:
                    TYP.append(entity)
        if tag not in ['I-TYP', 'B-TYP']:
            if 'entity' in locals().keys():
                TYP.append(entity)
                del entity
            continue
    return TYP


def get_VLM_dict(tag_seq, char_seq):
    length = len(char_seq)
    VLM = []
    # entity = dict()
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'B-VLM':
            if 'entity' in locals().keys():
                VLM.append(entity)
                del entity
            entity = dict()
            entity["entity"] = "volume"
            entity["start"] = i
            entity["end"] = i
            entity["value"] = char
            if i+1 == length:
                VLM.append(entity)
        if tag == 'I-VLM':
            if 'entity' in locals().keys():
                entity["end"] += 1
                entity["value"] += char
            # else: VLM = char
                if i+1 == length:
                    VLM.append(entity)
        if tag not in ['I-VLM', 'B-VLM']:
            if 'entity' in locals().keys():
                VLM.append(entity)
                del entity
            continue
    return VLM


def get_DEP_dict(tag_seq, char_seq):
    length = len(char_seq)
    DEP = []
    # entity = dict()
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'B-DEP':
            if 'entity' in locals().keys():
                DEP.append(entity)
                del entity
            entity = dict()
            entity["entity"] = "depart_time"
            entity["start"] = i
            entity["end"] = i
            entity["value"] = char
            if i+1 == length:
                DEP.append(entity)
        if tag == 'I-DEP':
            if 'entity' in locals().keys():
                entity["end"] += 1
                entity["value"] += char
            # else: DEP = char
                if i+1 == length:
                    DEP.append(entity)
        if tag not in ['I-DEP', 'B-DEP']:
            if 'entity' in locals().keys():
                DEP.append(entity)
                del entity
            continue
    return DEP


def get_ARR_dict(tag_seq, char_seq):
    length = len(char_seq)
    ARR = []
    # entity = dict()
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'B-ARR':
            if 'entity' in locals().keys():
                ARR.append(entity)
                del entity
            entity = dict()
            entity["entity"] = "arrive_time"
            entity["start"] = i
            entity["end"] = i
            entity["value"] = char
            if i+1 == length:
                ARR.append(entity)
        if tag == 'I-ARR':
            if 'entity' in locals().keys():
                entity["end"] += 1
                entity["value"] += char
            # else: ARR = char
                if i+1 == length:
                    ARR.append(entity)
        if tag not in ['I-ARR', 'B-ARR']:
            if 'entity' in locals().keys():
                ARR.append(entity)
                del entity
            continue
    return ARR


def get_DUR_dict(tag_seq, char_seq):
    length = len(char_seq)
    DUR = []
    # entity = dict()
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'B-DUR':
            if 'entity' in locals().keys():
                DUR.append(entity)
                del entity
            entity = dict()
            entity["entity"] = "duration"
            entity["start"] = i
            entity["end"] = i
            entity["value"] = char
            if i+1 == length:
                DUR.append(entity)
        if tag == 'I-DUR':
            if 'entity' in locals().keys():
                entity["end"] += 1
                entity["value"] += char
            # else: DUR = char
                if i+1 == length:
                    DUR.append(entity)
        if tag not in ['I-DUR', 'B-DUR']:
            if 'entity' in locals().keys():
                DUR.append(entity)
                del entity
            continue
    return DUR


def get_PRC_dict(tag_seq, char_seq):
    length = len(char_seq)
    PRC = []
    # entity = dict()
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'B-PRC':
            if 'entity' in locals().keys():
                PRC.append(entity)
                del entity
            entity = dict()
            entity["entity"] = "price"
            entity["start"] = i
            entity["end"] = i
            entity["value"] = char
            if i+1 == length:
                PRC.append(entity)
        if tag == 'I-PRC':
            if 'entity' in locals().keys():
                entity["end"] += 1
                entity["value"] += char
            # else: PRC = char
                if i+1 == length:
                    PRC.append(entity)
        if tag not in ['I-PRC', 'B-PRC']:
            if 'entity' in locals().keys():
                PRC.append(entity)
                del entity
            continue
    return PRC


def str2bool(v):
    # copy from StackOverflow
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def get_entity(tag_seq, char_seq):
    ITM = get_ITM_entity(tag_seq, char_seq)
    LOC = get_LOC_entity(tag_seq, char_seq)
    ORG = get_ORG_entity(tag_seq, char_seq)
    TIM = get_TIM_entity(tag_seq, char_seq)
    TYP = get_TYP_entity(tag_seq, char_seq)
    # VLM = get_VLM_entity(tag_seq, char_seq)
    return ITM, LOC, ORG, TIM, TYP


def get_ITM_entity(tag_seq, char_seq):
    length = len(char_seq)
    ITM = []
    # ITM = ''
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'B-ITM':
            if 'itm' in locals().keys():
                ITM.append(itm)
                del itm
            itm = char
            if i+1 == length:
                ITM.append(itm)
        if tag == 'I-ITM':
            if 'itm' in locals().keys():
                itm += char
            else:
                itm = char
            if i+1 == length:
                ITM.append(itm)
        if tag not in ['I-ITM', 'B-ITM']:
            if 'itm' in locals().keys():
                ITM.append(itm)
                del itm
            continue
    return ITM


def get_LOC_entity(tag_seq, char_seq):
    length = len(char_seq)
    LOC = []
    # loc = ''
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'B-LOC':
            if 'loc' in locals().keys():
                LOC.append(loc)
                del loc
            loc = char
            if i+1 == length:
                LOC.append(loc)
        if tag == 'I-LOC':
            if 'loc' in locals().keys():
                loc += char
            else: loc = char
            if i+1 == length:
                LOC.append(loc)
        if tag not in ['I-LOC', 'B-LOC']:
            if 'loc' in locals().keys():
                LOC.append(loc)
                del loc
            continue
    return LOC


def get_ORG_entity(tag_seq, char_seq):
    length = len(char_seq)
    ORG = []
    # org = ''
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'B-ORG':
            if 'org' in locals().keys():
                ORG.append(org)
                del org
            org = char
            if i+1 == length:
                ORG.append(org)
        if tag == 'I-ORG':
            if 'org' in locals().keys():
                org += char
            else: org = char
            if i+1 == length:
                ORG.append(org)
        if tag not in ['I-ORG', 'B-ORG']:
            if 'org' in locals().keys():
                ORG.append(org)
                del org
            continue
    return ORG


def get_TIM_entity(tag_seq, char_seq):
    length = len(char_seq)
    TIM = []
    # ITM = ''
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'B-TIM':
            if 'tim' in locals().keys():
                TIM.append(tim)
                del tim
            tim = char
            if i+1 == length:
                TIM.append(tim)
        if tag == 'I-TIM':
            if 'tim' in locals().keys():
                tim += char
            else: tim = char
            if i+1 == length:
                TIM.append(tim)
        if tag not in ['I-TIM', 'B-TIM']:
            if 'tim' in locals().keys():
                TIM.append(tim)
                del tim
            continue
    return TIM


def get_TYP_entity(tag_seq, char_seq):
    length = len(char_seq)
    TYP = []
    # ITM = ''
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'B-TYP':
            if 'typ' in locals().keys():
                TYP.append(typ)
                del typ
            typ = char
            if i+1 == length:
                TYP.append(typ)
        if tag == 'I-TYP':
            if 'typ' in locals().keys():
                typ += char
            else:
                typ = char
            if i+1 == length:
                TYP.append(typ)
        if tag not in ['I-TYP', 'B-TYP']:
            if 'typ' in locals().keys():
                TYP.append(typ)
                del typ
            continue
    return TYP


def get_VLM_entity(tag_seq, char_seq):
    length = len(char_seq)
    VLM = []
    # ITM = ''
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'B-VLM':
            if 'vlm' in locals().keys():
                VLM.append(vlm)
                del vlm
            vlm = char
            if i+1 == length:
                VLM.append(vlm)
        if tag == 'I-VLM':
            if 'vlm' in locals().keys():
                vlm += char
            else:
                vlm = char
            if i+1 == length:
                VLM.append(vlm)
        if tag not in ['I-VLM', 'B-VLM']:
            if 'vlm' in locals().keys():
                VLM.append(vlm)
                del vlm
            continue
    return VLM


def get_logger(filename):
    logger = logging.getLogger('logger')
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    handler = logging.FileHandler(filename)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s: %(message)s'))
    logging.getLogger().addHandler(handler)
    return logger
