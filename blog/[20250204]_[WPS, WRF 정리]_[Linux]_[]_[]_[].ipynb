{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "## WRF / WSL2 명령어 정리"
      ],
      "metadata": {
        "id": "GUW7ep7JnkU1"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# 한국형수치예보모델(KIM) 설명 및 결과 조회\n",
        "## 기상자료개방포털 기상기후데이터위키 / 모델 설명\n",
        "https://datawiki.kma.go.kr/doku.php?id=%EC%88%98%EC%B9%98%EB%AA%A8%EB%8D%B8:%EB%8B%A8%EC%A4%91%EA%B8%B0%EB%AA%A8%EB%8D%B8:%ED%95%9C%EA%B5%AD%ED%98%95%EC%88%98%EC%B9%98%EC%98%88%EB%B3%B4%EB%AA%A8%EB%8D%B8_kim#%ED%99%9C%EC%9A%A9%EB%B0%A9%EC%95%88\n",
        "## 기상청 API허브 / 결과 조회\n",
        "https://apihub.kma.go.kr/\n",
        "## TL;DR\n",
        "모델의 결과만 보려면 좋은 선택\n",
        "\n"
      ],
      "metadata": {
        "id": "dtxfaE_7oESp"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# WPS 작업\n",
        "예제 데이터를 다운로드\n",
        "WPS는 WRF Preprocessing System로 WRF 전처리 시스템\n",
        "WPS는 matthew 폴더의 grib2 형식의 파일을 geogrid, ungrib, metgrid 순서로 실행\n",
        "namelist.wps는 환경에 맞게 수정\n",
        "geogrid는 지형데이터나 지도 투영법을 정하는 작업으로 ./geogrid.exe 명령어로 실행\n",
        "ungrib는 다운받은 grib를 압축 해제하는 작업으로 ./ungrib.exe 명령어로 실행\n",
        "metgrid는 geogrid와 ungrib의 결과를 수평적으로 내삽하는 작업으로 ./metgrid.exe 명령어로 실행"
      ],
      "metadata": {
        "id": "kqzKqg_xdi1B"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# WPS, WRF 설치 라이브러리 목록\n",
        "zlib-1.2.13\n",
        "hdf5-1.10.5\n",
        "netcdf-c-4.9.0\n",
        "netcdf-fortran-4.6.0\n",
        "mpich-3.3.1\n",
        "libpng-1.6.37\n",
        "jasper-1.900.1\n",
        "WRF-4.1.2\n",
        "WPS-4.1"
      ],
      "metadata": {
        "id": "mcw7OftGiAK4"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# WPS, WRF 예제 데이터 목록\n",
        "## WPS_GEOG\n",
        "albedo_modis\n",
        "greenfrac_fpar_modis\n",
        "lai_modis_10m\n",
        "maxsnowalb_modis\n",
        "modis_landuse_20class_30s_with_lakes\n",
        "orogwd_10m\n",
        "soiltemp_1deg\n",
        "soiltype_bot_30s\n",
        "soiltype_top_30s\n",
        "topo_gmted2010_30s\n",
        "\n",
        "## test_data/matthew\n",
        "matthew_1deg"
      ],
      "metadata": {
        "id": "VrfSR8eCbjwC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "zqq6E7SNhmhs"
      },
      "outputs": [],
      "source": [
        "# 현재 폴더 위치 찾기\n",
        "echo 'alias explorer=\"explorer.exe .\"' >> ~/.bashrc\n",
        "source ~/.bashrc  # 일회성 코드\n",
        "\n",
        "explorer"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# WPS, WRF 설치 및 실행용 환경변수\n",
        "export HOME=/home/lsh\n",
        "export DIR=$HOME/WRF/Library\n",
        "export CC=gcc\n",
        "export CXX=g++\n",
        "export FC=gfortran\n",
        "export F77=gfortran\n",
        "export HDF5=$DIR\n",
        "export LD_LIBRARY_PATH=$DIR/lib:$LD_LIBRARY_PATH\n",
        "export PATH=$DIR/bin:$PATH\n",
        "export NETCDF=$DIR\n",
        "export CPPFLAGS=-I$DIR/include\n",
        "export LDFLAGS=-L$DIR/lib\n",
        "export PATH=$DIR/bin:$PATH\n",
        "export NETCDF=$DIR\n",
        "export LD_LIBRARY_PATH=$DIR/lib:$LD_LIBRARY_PATH\n",
        "export CPPFLAGS=-I$DIR/include\n",
        "export LDFLAGS=-L$DIR/lib\n",
        "export LIBS=\"-lnetcdf -lhdf5_hl -lhdf5 -lz\"\n",
        "export LDFLAGS=-L$DIR/lib\n",
        "export CPPFLAGS=-I$DIR/include\n",
        "export JASPERLIB=$DIR/lib\n",
        "export JASPERINC=$DIR/include\n",
        "export WRF_DIR=$HOME/WRF/WRF-4.1.2\n",
        "export NCARG_ROOT=/lib\n",
        "export PATH=$NCARG_ROOT/bin:$PATH\n",
        "export NCL_LIBDIR=$NCARG_ROOT/lib/ncarg/nclscripts/csm\n",
        "export NCL_SCRIPT_DIR=$NCL_LIBDIR\n",
        "export NCARG_ROOT=/home/lsh/WRF/Library/ncl_ncarg-6.6.2\n",
        "export PATH=$NCARG_ROOT/bin:$PATH\n",
        "export LD_LIBRARY_PATH=$NCARG_ROOT/lib:$LD_LIBRARY_PATH"
      ],
      "metadata": {
        "id": "ov9iT1TbiAXz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "8ljU7rRhiAU0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "QjkEK86Cnj6n"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "UCNBDQfgZ3YO"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 결과 파일 삭제 및 이동\n",
        "ln -sf /home/lsh/WRF/WPS-4.1/met_em.d01.2016-10-06_00:00:00.nc\n",
        "ln -sf /home/lsh/WRF/WPS-4.1/met_em.d01.2016-10-06_06:00:00.nc\n",
        "ln -sf /home/lsh/WRF/WPS-4.1/met_em.d01.2016-10-06_12:00:00.nc\n",
        "ln -sf /home/lsh/WRF/WPS-4.1/met_em.d01.2016-10-06_18:00:00.nc\n",
        "ln -sf /home/lsh/WRF/WPS-4.1/met_em.d01.2016-10-07_00:00:00.nc\n",
        "ln -sf /home/lsh/WRF/WPS-4.1/met_em.d01.2016-10-07_06:00:00.nc\n",
        "ln -sf /home/lsh/WRF/WPS-4.1/met_em.d01.2016-10-07_12:00:00.nc\n",
        "ln -sf /home/lsh/WRF/WPS-4.1/met_em.d01.2016-10-07_18:00:00.nc\n",
        "ln -sf /home/lsh/WRF/WPS-4.1/met_em.d01.2016-10-08_00:00:00.nc\n",
        "\n",
        "rm met_em.d01.2016-10-06_000000.nc\n",
        "rm met_em.d01.2016-10-06_060000.nc\n",
        "rm met_em.d01.2016-10-06_120000.nc\n",
        "rm met_em.d01.2016-10-06_180000.nc\n",
        "rm met_em.d01.2016-10-07_000000.nc\n",
        "rm met_em.d01.2016-10-07_060000.nc\n",
        "rm met_em.d01.2016-10-07_120000.nc\n",
        "rm met_em.d01.2016-10-07_180000.nc\n",
        "rm met_em.d01.2016-10-08_000000.nc\n",
        "\n",
        "mv met_em.d01.2016-10-06_000000.nc met_em.d01.2016-10-06_00:00:00.nc\n",
        "mv met_em.d01.2016-10-06_060000.nc met_em.d01.2016-10-06_06:00:00.nc\n",
        "mv met_em.d01.2016-10-06_120000.nc met_em.d01.2016-10-06_12:00:00.nc\n",
        "mv met_em.d01.2016-10-06_180000.nc met_em.d01.2016-10-06_18:00:00.nc\n",
        "mv met_em.d01.2016-10-07_000000.nc met_em.d01.2016-10-07_00:00:00.nc\n",
        "mv met_em.d01.2016-10-07_060000.nc met_em.d01.2016-10-07_06:00:00.nc\n",
        "mv met_em.d01.2016-10-07_120000.nc met_em.d01.2016-10-07_12:00:00.nc\n",
        "mv met_em.d01.2016-10-07_1800:00.nc met_em.d01.2016-10-07_18:00:00.nc\n",
        "mv met_em.d01.2016-10-08_000000.nc met_em.d01.2016-10-08_00:00:00.nc"
      ],
      "metadata": {
        "id": "cQZHyz86iAck"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "cv5vC7K0iAfP"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "MX-h28xBiAhb"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Tia8gEuHiAkQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "2EAeWoYOiAma"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "IKwXWncliAqj"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Z-7XLIf_iAtB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "ssfi2AwHiAvQ"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
