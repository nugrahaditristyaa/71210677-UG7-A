{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "1_A_71210677.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyOaFthAKMD12pmBxkfQHze3"
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
      "cell_type": "code",
      "metadata": {
        "id": "Az2Ysa7OAOjD"
      },
      "source": [
        "der = input(\"Masukan deret angka : \")\n",
        "spil = der.split(\",\")\n",
        "jum = 0\n",
        "\n",
        "print(\"Total :\",end=\"\")\n",
        "\n",
        "for num in spil :\n",
        "    if(int(num) % 2 == 1) :\n",
        "      num = int(num) * -1\n",
        "      print(\"\",num,end=\"\")\n",
        "    elif(int(num) % 2 == 0) :\n",
        "      if (num == spil[0]) :\n",
        "          print(num,end=\"\")\n",
        "      else:\n",
        "          print(\" +\",num,end=\"\")\n",
        "\n",
        "    jum = jum + int(num)\n",
        "print()\n",
        "print(\"Hasil perhitungan diatas ialah\",jum)"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}