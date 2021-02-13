import json
import platform
import psutil

def collecting_information_about_system() -> str:
    general_info = platform.uname()
    result_dict = {}

    vir_mem = psutil.virtual_memory()

    swap_mem = psutil.swap_memory()

    cpu_info = [
        {
            'cpu': i + 1,
            'current': cpu.current,
            'min': cpu.min,
            'max': cpu.max
        } for i, cpu in enumerate(psutil.cpu_freq(percpu=True))
    ]
    
    vir_mem_info = {
        'total': vir_mem.total,
        'used': vir_mem.used,
        'free': vir_mem.free
    }

    swap_mem_info = {
        'total': swap_mem.total,
        'used': swap_mem.used,
        'free': swap_mem.free
    }

    result_dict.update(
        {
            'OS': general_info.system,
            'Architecture ': general_info.processor,
            'CPU': cpu_info,
            'Virtual Memory': vir_mem_info,
            'SWAP Memory': swap_mem_info
        }
    )

    return json.dumps(result_dict, indent=4, sort_keys=True)


def main() -> None:
    print(collecting_information_about_system())


if __name__ == '__main__':
    main()
