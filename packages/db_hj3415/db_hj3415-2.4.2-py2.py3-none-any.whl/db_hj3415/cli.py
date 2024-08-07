import argparse
import os
import json
from db_hj3415 import mongo
from utils_hj3415 import utils

# 파일에 저장할 데이터의 기본 파일 경로
FILE_PATH = 'settings.json'
mongo_addr_title = 'mongo_addr'
def_addr = "mongodb://hj3415:piyrw421@192.168.100.175:27017/"


def save_addr(address: str):
    """주소를 파일에 저장합니다."""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            settings = json.load(file)
    else:
        settings = {
        }

    settings[mongo_addr_title] = address

    with open(FILE_PATH, 'w') as file:
        json.dump(settings, file, indent=4)

    print(f"주소가 저장 되었습니다: {address}")


def load_addr() -> str:
    """파일에서 주소를 불러옵니다."""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            settings = json.load(file)
            return settings[mongo_addr_title]
    else:
        # 기본값
        return def_addr


# 몽고db 초기화
mongo.Base.initialize_client(mongo.connect_mongo(load_addr()))


def db():
    pages = mongo.Corps.COLLECTIONS

    parser = argparse.ArgumentParser(description="데이터베이스 주소를 저장하고 불러오는 프로그램")
    subparsers = parser.add_subparsers(dest='command', help='명령을 선택하세요.')

    # 저장 서브커맨드
    parser_save = subparsers.add_parser('save', help='데이터베이스 주소를 저장합니다.')
    parser_save.add_argument('address', type=str, help='저장할 주소를 입력하세요.')

    # 불러오기 서브커맨드
    parser_load = subparsers.add_parser('print', help='저장된 데이터베이스 주소를 불러옵니다.')

    # 지우기 서브커맨드
    parser_drop = subparsers.add_parser('drop', help="데이터베이스나 페이지를 삭제합니다.")
    parser_drop.add_argument('page', help=f"Pages - {pages}")
    parser_drop.add_argument('targets', nargs='+', type=str, help="원하는 종류의 코드를 나열하세요.")

    # 인자 파싱
    args = parser.parse_args()

    # 명령에 따른 동작 수행
    if args.command == 'save':
        save_addr(args.address)
    elif args.command == 'print':
        address = load_addr()
        if address:
            print(f"데이터베이스 주소: {address}")
    elif args.command == 'drop':
        if args.page in pages:
            if len(args.targets) == 1 and args.targets[0] == 'all':
                mongo.Corps.drop_page_in_all_codes(args.page)
            else:
                # args.targets의 코드 유효성을 검사한다.
                is_valid = True
                for code in args.targets:
                    # 하나라도 코드 형식에 이상 있으면 에러
                    is_valid = utils.is_6digit(code)
                if is_valid:
                    for code in args.targets:
                        mongo.Corps(code, args.page).drop_table()
                else:
                    print(f"{args.targets} 종목 코드의 형식은 6자리 숫자입니다.")
        else:
            print(f"The page should be in {pages}")


"""def dbmanager():
    cmd = ['repair', 'sync', 'eval', 'update']
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd', help=f"Command - {cmd}")
    parser.add_argument('target', help="Target for scraping (type 6digit code or 'all' or 'parts')")
    parser.add_argument('-d', '--db_path', help="Set mongo database path")

    args = parser.parse_args()

    db_path = args.db_path if args.db_path else "mongodb://192.168.0.173:27017"
    client = mongo.connect_mongo(db_path)

    if args.cmd in cmd:
        if args.cmd == 'repair':
            if args.target == 'all' or utils.is_6digit(args.target):
                need_for_repair_codes = chk_db.chk_integrity_corps(client, args.target)
                # repair dict 예시 - {'343510': ['c106', 'c104', 'c103'], '298000': ['c104'], '091810': ['c104']}
                print(f"Need for repairing codes :{need_for_repair_codes}")
                if need_for_repair_codes:
                    # x = input("Do you want to try to repair db by scraping? (y/N)")
                    # if x == 'y' or x == 'Y':
                        for code, failed_page_list in need_for_repair_codes.items():
                            for page in failed_page_list:
                                if page == 'c101':
                                    nfsrun.c101([code, ], db_path)
                                elif page == 'c103':
                                    nfsrun.c103([code, ], db_path)
                                elif page == 'c104':
                                    nfsrun.c104([code, ], db_path)
                                elif page == 'c106':
                                    nfsrun.c106([code, ], db_path)
                            recheck_result = chk_db.chk_integrity_corps(client, code)
                            if recheck_result:
                                # 다시 스크랩해도 오류가 지속되는 경우
                                print(f"The db integrity failure persists..{recheck_result}")
                                # x = input(f"Do you want to delete {code} on DB? (y/N)")
                                # if x == 'y' or x == 'Y':
                                #    mongo.Corps.del_db(client, code)
                                # else:
                                #    print("Canceled.")
                                mongo.Corps.del_db(client, code)
                    # else:
                    #     print("Done.")
                else:
                    print("Done.")
            else:
                print(f"Invalid target option : {args.target}")
        elif args.cmd == 'update':
            if args.target == 'all' or utils.is_6digit(args.target):
                need_for_update_codes = list(chk_db.chk_modifying_corps(client, args.target).keys())
                # need_for_update_codes 예시 - [codes....]
                print(f"Need for updating codes :{need_for_update_codes}")
                if need_for_update_codes:
                    nfsrun.c103(need_for_update_codes, db_path)
                    nfsrun.c104(need_for_update_codes, db_path)
                    nfsrun.c106(need_for_update_codes, db_path)
            elif args.target == 'parts':
                pass
            else:
                print(f"Invalid target option : {args.target}")
        elif args.cmd == 'sync':
            if args.target == 'all':
                chk_db.sync_mongo_with_krx(client)
            else:
                print(f"The target should be 'all' in sync command.")
        elif args.cmd == 'eval':
            if args.target == 'all':
                # eval을 평가해서 데이터베이스에 저장한다.
                eval.make_today_eval_df(client, refresh=True)
            else:
                print(f"The target should be 'all' in sync command.")
    else:
        print(f"The command should be in {cmd}")

    client.close()"""
