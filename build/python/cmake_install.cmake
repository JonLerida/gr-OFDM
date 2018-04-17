# Install script for directory: /home/leri/Escritorio/tfg/AccesoMedio/gr-OFDM/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/OFDM" TYPE FILE FILES
    "/home/leri/Escritorio/tfg/AccesoMedio/gr-OFDM/python/__init__.py"
    "/home/leri/Escritorio/tfg/AccesoMedio/gr-OFDM/python/MAC_OFDM.py"
    "/home/leri/Escritorio/tfg/AccesoMedio/gr-OFDM/python/PHY_OFDM.py"
    "/home/leri/Escritorio/tfg/AccesoMedio/gr-OFDM/python/ofdm_frame_sync_bb.py"
    "/home/leri/Escritorio/tfg/AccesoMedio/gr-OFDM/python/OFDM_PHY_IMPL_cb.py"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/OFDM" TYPE FILE FILES
    "/home/leri/Escritorio/tfg/AccesoMedio/gr-OFDM/build/python/__init__.pyc"
    "/home/leri/Escritorio/tfg/AccesoMedio/gr-OFDM/build/python/MAC_OFDM.pyc"
    "/home/leri/Escritorio/tfg/AccesoMedio/gr-OFDM/build/python/PHY_OFDM.pyc"
    "/home/leri/Escritorio/tfg/AccesoMedio/gr-OFDM/build/python/ofdm_frame_sync_bb.pyc"
    "/home/leri/Escritorio/tfg/AccesoMedio/gr-OFDM/build/python/OFDM_PHY_IMPL_cb.pyc"
    "/home/leri/Escritorio/tfg/AccesoMedio/gr-OFDM/build/python/__init__.pyo"
    "/home/leri/Escritorio/tfg/AccesoMedio/gr-OFDM/build/python/MAC_OFDM.pyo"
    "/home/leri/Escritorio/tfg/AccesoMedio/gr-OFDM/build/python/PHY_OFDM.pyo"
    "/home/leri/Escritorio/tfg/AccesoMedio/gr-OFDM/build/python/ofdm_frame_sync_bb.pyo"
    "/home/leri/Escritorio/tfg/AccesoMedio/gr-OFDM/build/python/OFDM_PHY_IMPL_cb.pyo"
    )
endif()

