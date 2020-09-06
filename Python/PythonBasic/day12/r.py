import re

def main():
    pat_ac = r'^[1-9](\d){4,11}$'
    pat_ps = r'^\w{6,20}$'
    ac = input()
    ps = input()
    m_ac = re.search(pat_ac, ac)
    m_ps = re.search(pat_ps, ps)
    print(m_ac.group(0), m_ps.group(0))

if __name__ == "__main__":
    main()