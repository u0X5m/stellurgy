import random, json

# Maximum Tech Level of Colonising Species
tl_max = 15

def benford():
        a = random.randint(0,99)
        if a <= 30:
                return(1)
        elif a <= 48:
                return(2)
        elif a <= 60:
                return(3)
        elif a <= 70:
                return(4)
        elif a <= 78:
                return(5)
        elif a <= 85:
                return(6)
        elif a <= 90:
                return(7)
        elif a <= 95:
                return(8)
        return(9)
        


def d(num):
        return random.randint(1,num)
    
def e_hex(num):
        b = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F", 16: "G",
             17: "H", 18: "J", 19: "K", 20: "L", 21: "M", 22: "N", 23: "P",
             24: "Q", 25: "R", 26: "S", 27: "T", 28: "U", 29: "V", 30: "W",
             31: "X", 32: "Y", 33: "Z"}
        try:
                a = num + 1
                if num <= 0:
                        return("0")
                if 1 <= num <= 9:
                        return(str(num))
                if num >= 10:
                        return(b[num])
        except:
                if num in "ABCDEFGHJKLMNPQRSTUVWXYZ":
                        return(num)
                else:
                        print("e_hex error")
                        print(num)

def e_dec(num):
        if num in "0123456789":
                return(int(num))
        elif num in "ABCDEFGH":
                return(ord(num)-55)
        
# Generate Number of Orbits for Each Primary and Distant Star

def orbits(star, system, orbit):
        # Original for RTT Worldgen
        #epi, inner, outer = d(6)-3, d(6)-1, d(6)-1
        # Bigger system with more planets
        epi, inner, outer = d(6)-2, d(6), d(6)
        if "M" in star and "V" in star:
                epi -= 1
                inner -= 1
                outer -= 1
        if "III" in star or "D" in star or "L" in star:
                epi = 0
        if "L" in star:
                inner = d(3)-1
                outer -= 1
        if "Close" in system["Stellar Orbits"] and orbit == "Primary":
                inner = 0
        if "Moderate" in system["Stellar Orbits"] and orbit == "Primary":
                outer = 0
        epi, inner, outer = max(epi, 0), max(inner, 0), max(outer, 0)
        planetary_orbits = {"Epistellar": epi,
                            "Inner": inner,
                            "Outer": outer}
        planetary_orbit_contents = {"Epistellar": [],
                            "Inner": [],
                            "Outer": []}
        if "III" in star or "D" in star:
                expansion = d(6)
        else:
                expansion = 0
        for orbit in ["Epistellar", "Inner", "Outer"]:
                for i in range(planetary_orbits[orbit]):
                        planetary_orbit_contents[orbit] += [worldgen(star, orbit, expansion, system)]
                        if expansion:
                                expansion -= 1
        return(planetary_orbits, planetary_orbit_contents)

def planet_type(classification, expansion, orbit, belt, satellite):
        if classification == "Dwarf":
                if expansion:
                        planet_class = "Stygian"
                else:
                        if orbit == "Epistellar":
                                planet_class = d(6)
                                if belt == True:
                                        planet_class -= 2
                                if planet_class <= 3:
                                        planet_class = "Rockball"
                                elif 4 <= planet_class <= 5:
                                        planet_class = "Meltball"
                                else:
                                        if d(6) <= 4:
                                                planet_class = "Hebean"
                                        else:
                                                planet_class = "Promethean"
                        elif orbit == "Inner":
                                planet_class = d(6)
                                if belt == True:
                                        planet_class -= 2
                                if satellite == "Helian":
                                        planet_class += 1
                                elif satellite == "Jovian":
                                        planet_class += 2
                                if planet_class <= 4:
                                        planet_class = "Rockball"
                                elif 5 <= planet_class <= 6:
                                        planet_class = "Arean"
                                elif planet_class == 7:
                                        planet_class = "Meltball"
                                else:
                                        if d(6) <= 4:
                                                planet_class = "Hebean"
                                        else:
                                                planet_class = "Promethean"
                        elif orbit == "Outer":
                                planet_class = d(6)
                                if belt == True:
                                        planet_class -= 1
                                if satellite == "Helian":
                                        planet_class += 1
                                elif satellite == "Jovian":
                                        planet_class += 2
                                if planet_class <= 0:
                                        planet_class = "Rockball"
                                elif 1 <= planet_class <= 4:
                                        planet_class = "Snowball"
                                elif 5 <= planet_class <= 6:
                                        planet_class = "Rockball"
                                elif planet_class == 7:
                                        planet_class = "Meltball"
                                else:
                                        roll = d(6)
                                        if roll <= 3:
                                                planet_class = "Hebean"
                                        elif 4 <= roll <= 5:
                                                planet_class = "Arean"
                                        else:
                                                planet_class = "Promethean"
        elif classification == "Terrestrial":
                if expansion:
                        planet_class = "Acheronian"
                else:                                
                        if orbit == "Epistellar":
                                planet_class = d(6)
                                if planet_class <= 4:
                                        planet_class = "Janilithic"
                                elif planet_class == 5:
                                        planet_class = "Vesperian"
                                else:
                                        planet_class = "Telluric"
                        elif orbit == "Inner":
                                planet_class = d(6) + d(6)
                                if planet_class <= 4:
                                        planet_class = "Telluric"
                                elif 5 <= planet_class <= 6:
                                        planet_class = "Arid"
                                elif planet_class == 7:
                                        planet_class = "Tectonic"
                                elif 8 <= planet_class <= 9:
                                        planet_class = "Oceanic"
                                elif planet_class == 10:
                                        planet_class = "Tectonic"
                                else:
                                        planet_class = "Telluric"
                        elif orbit == "Outer":
                                planet_class = d(6) + d(6)
                                if satellite == "Helian" or satellite == "Jovian":
                                        planet_class += 2
                                if planet_class <= 4:
                                        planet_class = "Arid"
                                elif 5 <= planet_class <= 6:
                                        planet_class = "Tectonic"
                                else:
                                        planet_class = "Oceanic"
        elif classification == "Helian":
                if expansion:
                        planet_class = "Asphodelian"
                else:  
                        if orbit == "Epistellar":
                                planet_class = d(6)
                                if planet_class <= 5:
                                        planet_class = "Helian"
                                else:
                                        planet_class = "Asphodelian"
                        elif orbit == "Inner":
                                planet_class = d(6)
                                if planet_class <= 4:
                                        planet_class = "Helian"
                                else:
                                        planet_class = "Panthalassic"
                        elif orbit == "Outer":
                                planet_class = "Helian"
        elif classification == "Jovian":
                if expansion:
                        planet_class = "Chthonian"
                else:  
                        if orbit == "Epistellar":
                                planet_class = d(6)
                                if planet_class <= 5:
                                        planet_class = "Jovian"
                                else:
                                        planet_class = "Chthonian"
                        elif orbit == "Inner" or orbit == "Outer":
                                planet_class = "Jovian"
        return(planet_class)
                
def planet_details(planet_class, age, star, orbit, satellite, settlement):
        age_mod = ""
        uwp = ""
        starport = 0
        size = 0
        atmo = 0
        hydro = 0
        bio = 0
        pop = 0
        gov = 0
        law = 0
        tl = tl_max
        ind = 0
        age_mod = 0
        popd = 0
        bases = []

        # Planetoid Belts
        if planet_class in ["Vuclanoidal", "Metallic","Silicaceous", "Carbonaceous", "Gelidaceous"]:
                size = 32
                        
        elif planet_class == "Acheronian":
                size = d(6) +4
                atmo = 1

        elif planet_class == "Arean":
                size = d(6)-1
                atmo = d(6)
                if "D" in star:
                        atmo -2
                if atmo <= 3:
                        atmo = 1
                else:
                        atmo = 10
                if atmo == 1:
                        planet_class = "EuArean"
                if atmo == 10:
                        if d(2) == 2:
                                planet_class = "MesoArean"
                        else:
                                planet_class = "AreanLacustric"
                hydro = d(6) + size -7
                if atmo == 1:
                        hydro -= 4
                chem = d(6)
                if "L" in star:
                        chem += 2
                if orbit == "Outer":
                        chem += 2
                if chem <= 4:
                        age_mod = 0
                elif 5 <= chem <= 6:
                        age_mod = 1
                        planet_class = planet_class.replace("Arean", "Utgardian")
                else:
                        age_mod = 3
                        planet_class = planet_class.replace("Arean", "Titanian")
                age_ = age_mod + d(3)
                if age >= age_ and atmo == 1:
                        bio = d(6)-4
                if age >= age_ and atmo == 10:
                        bio = d(3)
                if age >= 4 + age_mod and atmo == 10:
                        bio = d(6)+size-2                        
                
        elif planet_class == "Arid":
                size = d(6)+4
                chem = d(6)
                if "K" in star and "V" in star:
                        chem += 2
                if "M" in star and "V" in star:
                        chem += 4
                if "L" in star:
                        chem += 5
                if orbit == "Outer":
                        chem += 2
                if chem <= 6:
                        age_mod = 0
                        planet_class = "Darwinian"
                elif 7 <= chem <= 8:
                        age_mod = 1
                        planet_class = "Saganian"
                else:
                        age_mod = 3
                        planet_class = "Asimovian"
                age_ = age_mod + d(3)
                if age >= age_:
                        bio = d(3)
                if age >= 4 + age_mod:
                        bio = d(6) + d(6)
                        if "D" in star:
                                bio -=3
                if bio >= 3 and age_mod == 0:
                        atmo = d(6) + d(6) + size - 7
                        atmo = min(max(atmo, 2), 9)
                else:
                        atmo = 10
                hydro = d(3)
                
        elif planet_class == "Asphodelian":
                size = d(6)+9
                atmo = 1
                
        elif planet_class == "Chthonian":
                size = 16
                atmo = 1
        
        elif planet_class == "Hebean":
                size = d(6) +1
                atmo = d(6) + size -6
                atmo = max(atmo, 0)
                if atmo >= 2:
                        atmo = 10
                hydro = d(6) + d(6) + size - 11
                hydro = max(hydro, 0)
                
        elif planet_class == "Helian":
                size = d(6) +9
                atmo = 13
                hydro = d(6)
                if hydro <= 2:
                        hydro = 2
                elif 3 <= hydro <= 4:
                        hydro = d(6) + d(6) -1
                else:
                        hydro = 15
                
        elif planet_class == "Janilithic":
                size = d(6) +4
                atmo = d(6)
                if atmo <= 3:
                        atmo = 1
                else:
                        atmo = 10

        elif planet_class == "Jovian":
                size = 16
                atmo = 16
                hydro = 16
                bio = d(6)
                if orbit == "Inner":
                        bio += 2
                if bio <= 5:
                        bio = 0
                else:
                        bio = 0
                        if age >= d(6):
                                bio = d(3)
                        if age >= 7:
                                bio = d(6) + d(6)
                                if "D" in star:
                                        bio -= 3
                        if bio:
                                chem = d(6)
                                if "L" in star:
                                        chem += 1
                                if orbit == "Epistellar":
                                        chem -= 2
                                if orbit == "Outer":
                                        chem += 2
                                if chem <= 3:
                                        planet_class = "Brammian Jovian"
                                else:
                                        planet_class = "Khonsonian Jovian"
        
        elif planet_class == "Meltball":
                if orbit == "Epistellar":
                        planet_class = random.choice(["Phaethonic", "Apollonian", "Sethian"])
                else:
                        planet_class = random.choice(["Hephaestian", "Lokian"])
                size = d(6)-1
                atmo = 1
                hydro = 15

        elif planet_class == "Oceanic":
                size = d(6)+4
                chem = d(6)
                if "K" in star and "V" in star:
                        chem += 2
                if "M" in star and "V" in star:
                        chem += 4
                if "L" in star:
                        chem += 5
                if orbit == "Outer":
                        chem += 2
                if chem <= 6:
                        age_mod = 0
                        planet_class = random.choice(["Pelagic", "BathyGaian"])
                elif 7 <= chem <= 8:
                        age_mod = 1
                        planet_class = random.choice(["Nunnic", "BathyAmunian"])
                else:
                        age_mod = 3
                        planet_class = random.choice(["Teathic", "BathyTartarian"])
                age_ = age_mod + d(3)
                if age >= age_:
                        bio = d(3)
                if age >= 4 + age_mod:
                        bio = d(6) + d(6)
                        if "D" in star:
                                bio -=3                        
                if age_mod == 0:
                        atmo = d(6) + d(6) + size - 6
                        if "K" in star and "V" in star:
                                atmo -= 1
                        if "M" in star and "V" in star:
                                atmo -= 2
                        if "L" in star:
                                atmo -= 3
                        if "IV" in star:
                                atmo -= 1
                        atmo = min(max(atmo, 2), 12)
                else:
                        atmo = d(6)
                        if 2 <= atmo <= 4:
                                atmo = 10
                        elif 5 <= atmo <= 6:
                                atmo = 12
                hydro = 11

        elif planet_class == "Panthalassic":
                size = d(6) +9
                atmo = min(d(6)+8,13)
                hydro = 11
                chem = d(6)
                if "K" in star and "V" in star:
                        chem += 2
                if "M" in star and "V" in star:
                        chem += 4
                if "L" in star:
                        chem += 5
                if 1 <= chem <= 6:
                        age_mod = 0
                        chem = d(6) + d(6)
                        if 9 <= chem <= 11:
                                planet_class = "ThioPanthalassic"
                        elif chem == 12:
                                planet_class = "ChloroPanthalassic"
                elif 7 <= chem <= 8:
                        age_mod = 1
                elif 9 <= chem:
                        age_mod = 3
                if age >= d(3) + age_mod:
                        bio = d(3)
                if age >= 4 + age_mod:
                        bio = d(6) + d(6)
                
        elif planet_class == "Promethean":
                size = d(6)-1
                chem = d(6)
                if "L" in star:
                        chem += 2
                if orbit == "Epistellar":
                        chem -= 2
                if orbit == "Outer":
                        chem += 2
                if chem <= 4:
                        age_mod = 0
                elif 5 <= chem <= 6:
                        age_mod = 1
                        planet_class = "Burian"
                else:
                        age_mod = 3
                        planet_class = "Atlan"
                if age >= d(3) + age_mod:
                        bio = d(3)
                if age >= 4 + age_mod:
                        bio = d(6) + d(6)
                        if "D" in star:
                                bio -= 3
                if bio >= 3 and age_mod == 0:
                        atmo = d(6) + d(6) + size -7
                        atmo = min(max(atmo, 2), 9)
                else:
                        atmo = 10
                hydro = d(6) + d(6) -2
                
        elif planet_class == "Rockball":
                size = d(6)-1
                hydro = d(6) + d(6) + size -11
                if "L" in star:
                        hydro += 1
                if orbit == "Epistellar":
                        hydro -= 2
                if orbit == "Outer":
                        hydro += 2
                chem = d(6) + d(6)
                if "F" in star:
                        chem -= 2
                if chem <= 5:
                        planet_class = "Ferrinian"
                elif 6 <= chem <= 8:
                        planet_class = "Lithic"
                elif 9 <= chem:
                        planet_class = "Carbonian"

        elif planet_class == "Snowball":
                size = d(6) -1
                atmo = d(6)
                if atmo <= 4:
                        atmo = 0
                else:
                        atmo = 1
                if d(2) == 2:
                        planet_class = "Gelidian"
                        hydro = 0
                else:
                        planet_class = random.choice(["Plutonian", "Erisian"])
                        hydro = d(6) + d(6) -2
                chem = d(6)
                if "L" in star:
                        chem += 2
                if orbit == "Outer":
                        chem += 2
                if chem <= 4:
                        age_mod = 0
                elif 5 <= chem <= 6:
                        age_mod = 1
                        planet_class = "Amun" + planet_class
                elif 7 <= chem:
                        age_mod = 3
                        planet_class = "Carbo" + planet_class
                if hydro:
                        if age >= d(6):
                                bio = d(6)-3
                        if age >= 6 + age_mod:
                                bio = d(6) + size -2
                
        elif planet_class == "Stygian":
                size = d(6) -1

        elif planet_class == "Tectonic":
                size = d(6) +4
                chem = d(6)
                if "K" in star and "V" in star:
                        chem += 2
                if "M" in star and "V" in star:
                        chem += 4
                if "L" in star:
                        chem += 5
                if orbit == "Outer":
                        chem += 2
                if chem <= 6:
                        age_mod = 0
                        chem = d(6) + d(6)
                        if chem <= 8:
                                planet_class == "Gaian"
                        elif 9 <= chem <= 11:
                                planet_class == "ThioGaian"
                        elif 12 <= chem:
                                planet_class == "ChloroGaian"
                elif 7 <= chem <= 8:
                        age_mod = 1
                        planet_class == "Amunian"
                elif 9 <= chem:
                        age_mod = 3
                        planet_class == "Tartarian"
                if age >= d(3) + age_mod:
                        bio = d(3)
                if age >= 4 + age_mod:
                        bio = d(6)+d(6)
                        if "D" in star:
                                bio -= 3
                atmo = 10
                if bio >= 3 and age_mod == 0:
                        atmo = d(6) + d(6) + size -7
                        min(max(atmo, 2), 9)
                if bio >= 3 and ("Thio" in planet_class or "Chloro" in planet_class):
                        atmo = 11
                hydro = d(6) + d(6) -2

        elif planet_class == "Telluric":
                size = d(6) +4
                atmo = 12
                hydro = d(6)
                if hydro <= 4:
                        hydro = 0
                else:
                        hydro = 15
                if orbit == "Epistellar":
                        planet_class = "Phosphorian"
                else:
                        planet_class = "Cytherean"

        elif planet_class == "Vesperian":
                size = d(6) +4
                chem = d(6) + d(6)
                if chem == 12:
                        planet_class = "ChloroVesperian"
                if age >= d(3):
                        bio = d(3)
                if age >= 4:
                        bio = d(6) + d(6)
                atmo = 10
                if bio >= 3:
                        atmo = d(6) + d(6) + size -7
                        min(max(atmo, 2), 9)
                if bio >= 3 and "Chloro" in planet_class:
                        atmo = 11
                hydro = d(6) + d(6) -2

        else:
                print("UNABLE TO FIND PLANET TYPE:\n" + planet_class)
                
        # Desirability:
        # Aslo modifier for flare star
        des = 0
        if "Ve" in star:
                des -= d(3)
        if orbit == "Inner":
                if "M" in star and "V" in star and "Ve" not in star:
                        des += 1
                elif "V" in star and "Ve" not in star:
                        des += 2  
        if size == 32:
                des += d(6) - d(6)
                if planet_class == "Vulcanoidal":
                        des += 3
                elif planet_class in ["Metallic", "Gelidaceous"]:
                        des += 2
                elif planet_class == "Carbonaceous":
                        des += 1
        if hydro == 0:
                des -= 1
        if 13 <= size <= 30 or 12 <= atmo <= 16 or hydro == 15:
                des -= 2
        if 1 <= size <= 11 and 2 <= atmo <= 9 and 0 <= hydro <= 11:
                if 5 <= size <= 10 and 4 <= atmo <= 9 and 4 <= hydro <= 8:
                        des += 5
                elif 10 <= hydro <= 11:
                        des += 3
                elif 2 <= atmo <= 6 and hydro <= 3:
                        des += 2
                else:
                        des += 4
        if 10 <= size <= 15 and atmo == 15:
                des -= 1
        if size == 0:
                des -= 1
        if atmo == 6 or atmo == 8:
                des += 1
                

        if bio >= 12: # Species Homeworld
                if age_mod == 0:
                        pop = des + d(3) - d(3)
                else:
                        pop = d(6) + d(6)
                tl = benford() + benford() -1
                
                if tl == 0:
                        gov = 0
                else:
                        if d(6) <= tl-9:
                                gov = 7
                        else:
                                gov = pop + d(6) + d(6) -7

        if d(6) + d(6) -2 <= des: # Colony
                pop = tl_max + settlement -9
                pop = min(max(pop, des +d(3) -d(3)), 4)
                gov = pop + d(6) + d(6) -7
                if 1 <= size <= 11 and 2 <= atmo <= 9 and bio <= 2:
                        bio = d(6) + 5
                        
        if d(6) <= tl_max - 11: # Outpost
                pop = min(d(3) + des, 4)
                if pop:
                        gov = min(pop + d(6) + d(6) -7, 6)

        if gov:
                law = gov + d(6) + d(6) -7
                
        if pop:
                ind = pop + d(6) + d(6) -7
                if law <= 3:
                        ind += 1
                elif 6 <= law <= 9:
                        ind -= 1
                elif 10 <= law <= 12:
                        law -= 2
                elif law >= 13:
                        ind -= 3
                if atmo <= 4 or atmo == 7 or atmo >= 9 or hydro == 15:
                        ind += 1
                if 12 <= tl <= 14:
                        ind += 1
                if tl >= 15:
                        ind += 2
                        
        if ind == 0:
                pop -= 1
        if 4 <= ind <= 9:
                pop += 1
                if atmo == 3 or atmo == 5:
                        atmo -= 1
                elif atmo == 6 or atmo == 8:
                        atmo += 1
        if ind >= 10:
                if d(2) == 2:
                        pop += 2
                        if atmo == 3 or atmo == 5:
                                atmo -= 1
                        elif atmo == 6 or atmo == 8:
                                atmo += 1
                else:
                        pop += 1
        if pop >= 1:
                popd = benford()
        else:
                popd = 0
        # Starport Generation
        starport = d(6) + d(6) + ind -7
        if 4 <= atmo <= 9 and 4 <= hydro <= 8 and 5 <= pop <= 7:
                starport += 1
        if 5 <= size <= 10 and 4 <= atmo <= 9 and 4 <= hydro <= 8:
                starport += 1
        if pop >= 9:
                starport += 1
        if ind >= tl-3:
                starport += 1
        if pop >= 9 and ind >= 6:
                starport += 1
        if (atmo <= 3 or atmo >= 11) and (hydro <= 3 or hydro >= 11) and pop >= 6:
                starport += 1
        if (atmo == 6 or atmo == 8) and (6 <= pop <= 8):
                starport += 1
        if 12 <= tl <= 14:
                starport += 1
        if tl >= 15:
                starport += 1
        if pop <= 3:
                starport -= 1
        if 2 <= atmo <= 5 and hydro <= 3:
                starport -= 1
        if tl <= 9:
                starport -= 1
        if starport <= 2:
                starport = "X"
        elif 3 <= starport <= 4:
                starport = "E"
        elif 5 <= starport <= 6:
                starport = "D"
        elif 7 <= starport <= 8:
                starport = "C"
        elif 9 <= starport <= 10:
                starport = "B"
        elif 11 <= starport:
                starport = "A"

        # Bases
        ## Consulate
        base = d(6) + d(6)
        if starport == "A" and base >= 6:
                bases += ["G"]
                if base >= 9:
                        bases += ["F"]
                if base >= 12:
                        bases += ["B"]
        elif starport == "B" and base >= 8:
                bases += ["G"]
                if base >= 11:
                        bases += ["F"]
        elif starport == "C" and base >= 10:
                bases += ["G"]

        ## Merchant Base
        base = d(6) + d(6)
        if starport == "A" and base >= 6:
                bases += ["M"]
                if base >= 9:
                        bases += ["Y"]
                if base >= 12:
                        bases += ["C"]
        elif starport == "B" and base >= 8:
                bases += ["M"]
                if base >= 11:
                        bases += ["Y"]
        elif starport == "C" and base >= 10:
                bases += ["M"]

        ## Naval Base
        base = d(6) + d(6)
        if starport in "ABC" and base >= 8:
                bases += ["N"]
                if base >= 11:
                        if d(3) == 3:
                                bases += ["Y", "H"]
                        elif d(2) == 2:
                                bases += ["H"]
                        else:
                                bases += ["Y"]

        ## Pirate Base
        base = d(6) + d(6)
        if starport == "B" and base >= 12:
                bases += ["P"]
        elif starport == "C" and base >= 10:
                bases += ["P"]
        elif starport in "DE" and base >= 12:
                bases += ["P"]

        ## Research Installation
        base = d(6) + d(6)
        if starport == "A" and base >= 8:
                bases += ["R"]
                if base >= 11:
                        bases += [random.choice(["H", "U", "L"])]
        elif starport in "BC" and base >= 10:
                bases += ["R"]

        ## Religious Site
        if d(6) + d(6) <= pop:
                bases += ["K"]

        ## Scout Base
        base = d(6) + d(6)
        if starport == "A" and base >= 10:
                bases += ["S"]
        elif starport in "BC" and base >= 8:
                bases += ["S"]
        elif starport == "D" and base >= 7:
                bases += ["S"]
                
        ## Ruins
        base = d(6) + d(6)
        if size >= 4 and base >= 12:
                bases += ["Z"]

        if pop == 0:
                gov = 0
                law = 0
        uwp = starport + e_hex(size) + e_hex(atmo) + e_hex(hydro) +\
              e_hex(pop) + e_hex(gov) + e_hex(law) + "-" + e_hex(tl) +\
              "-" + e_hex(bio) + e_hex(ind) + e_hex(popd)
        if bases:
                uwp += " " + " ".join(bases)
        return([[planet_class, uwp]])


def worldgen(star, orbit, expansion, system):
        settlement = system["Settlement"]
        age = system["Age"]
        content = d(6)
        content_ = d(6)
        world = []
        if "L" in star:
                content -= 1
        if content <= 1:
                # Belt
                if orbit == "Epistellar":
                        planet_class = "Vuclanoidal"
                else:
                        planet_class = d(6) + d(6)
                        if planet_class <= 3:
                                planet_class = "Metallic"
                        elif 4 <= planet_class <= 6:
                                planet_class = "Silicaceous"
                        elif 7 <= planet_class <= 10:
                                planet_class = "Carbonaceous"
                        elif 11 <= planet_class:
                                planet_class = "Gelidaceous"
                world += planet_details(planet_class, age, star, orbit, False, settlement)
                world[0][0] = planet_class + " Belt"
                # Belt with dwarf planet
                if content_ >= 5:
                        dwarf = planet_type("Dwarf", expansion, orbit, True, False)
                        dwarf = planet_details(dwarf, age, star, orbit, False, settlement)
                        dwarf[0][0] = dwarf[0][0] + " Dwarf"
                        world += dwarf
                        
        elif content == 2:
                if content_ <= 5:
                        dwarf = planet_type("Dwarf", expansion, orbit, False, False)
                        dwarf = planet_details(dwarf, age, star, orbit, False, settlement)
                        dwarf[0][0] = dwarf[0][0] + " Dwarf"
                        world += dwarf
                if content_ == 6:
                        dwarf = planet_type("Dwarf", expansion, orbit, False, False)
                        dwarf = planet_details(dwarf, age, star, orbit, False, settlement)
                        dwarf[0][0] = dwarf[0][0] + " Dwarf"
                        world += dwarf
                        dwarf = planet_type("Dwarf", expansion, orbit, False, False)
                        dwarf = planet_details(dwarf, age, star, orbit, False, settlement)
                        dwarf[0][0] = dwarf[0][0] + " Dwarf"
                        world += dwarf
                        
        elif content == 3:
                if content_ <= 4:
                        terrestrial_type = planet_type("Terrestrial", expansion, orbit, False, False)
                        terrestrial = planet_details(terrestrial_type, age, star, orbit, False, settlement)
                        terrestrial[0][0] = terrestrial[0][0] + " Terrestrial"
                        world += terrestrial
                elif content_ >= 5:
                        terrestrial_type = planet_type("Terrestrial", expansion, orbit, False, False)
                        terrestrial = planet_details(terrestrial_type, age, star, orbit, False, settlement)
                        terrestrial[0][0] = terrestrial[0][0] + " Terrestrial"
                        world += terrestrial
                        dwarf = planet_type("Dwarf", expansion, orbit, False, True)
                        dwarf = planet_details(dwarf, age, star, orbit, True, settlement)
                        dwarf[0][0] = dwarf[0][0] + " Dwarf"
                        world += dwarf

        elif content == 4:
                helian_type = planet_type("Helian", expansion, orbit, False, False)
                helian = planet_details(helian_type, age, star, orbit, False, settlement)
                if helian[0][0] != "Helian":
                        helian[0][0] = helian[0][0] + " Helian"
                world += helian
                satellites = max(0, d(6) -3)
                if satellites:
                        if content_ <= 5:
                                for i in range(satellites):
                                        dwarf = planet_type("Dwarf", expansion, orbit, False, True)
                                        dwarf = planet_details(dwarf, age, star, orbit, True, settlement)
                                        dwarf[0][0] = dwarf[0][0] + " Dwarf"
                                        world += dwarf
                        else:
                                terrestrial_type = planet_type("Terrestrial", expansion, orbit, False, True)
                                terrestrial = planet_details(terrestrial_type, age, star, orbit, True, settlement)
                                terrestrial[0][0] = terrestrial[0][0] + " Terrestrial"
                                world += terrestrial
                                if satellites -1:
                                        for i in range(satellites-1):
                                                dwarf = planet_type("Dwarf", expansion, orbit, False, True)
                                                dwarf = planet_details(dwarf, age, star, orbit, True, settlement)
                                                dwarf[0][0] = dwarf[0][0] + " Dwarf"
                                                world += dwarf
        else:
                jovian_type = planet_type("Jovian", expansion, orbit, False, False)
                world += planet_details(jovian_type, age, star, orbit, False, settlement)
                world[0][0] = world[0][0] + " Giant"
                satellites = d(6)
                if content_ <= 5:
                        for i in range(satellites):
                               dwarf = planet_type("Dwarf", expansion, orbit, False, True)
                               dwarf = planet_details(dwarf, age, star, orbit, True, settlement)
                               dwarf[0][0] = dwarf[0][0] + " Dwarf"
                               world += dwarf
                        
                else:
                        content_ = d(6)
                        if content_ <= 5:
                                terrestrial = planet_type("Terrestrial", expansion, orbit, False, True)
                                terrestrial = planet_details(terrestrial, age, star, orbit, True, settlement)
                                terrestrial[0][0] = terrestrial[0][0] + " Terrestrial"
                                world += terrestrial
                                if satellites -1:
                                        for i in range(satellites-1):
                                                dwarf = planet_type("Dwarf", expansion, orbit, False, True)
                                                dwarf = planet_details(dwarf, age, star, orbit, True, settlement)
                                                dwarf[0][0] = dwarf[0][0] + " Dwarf"
                                                world += dwarf
                        else:
                                helian = planet_type("Helian", expansion, orbit, False, True)
                                helian = planet_details(helian, age, star, orbit, True, settlement)
                                if helian[0][0] != "Helian":
                                        helian[0][0] = helian[0][0] + " Helian"
                                world += helian
                                if satellites -1:
                                        for i in range(satellites-1):
                                                dwarf = planet_type("Dwarf", expansion, orbit, False, True)
                                                dwarf = planet_details(dwarf, age, star, orbit, True, settlement)
                                                dwarf[0][0] = dwarf[0][0] + " Dwarf"
                                                world += dwarf

                rings = d(6)
                if rings >= 5:
                    world[0][0] = "Ringed " + world[0][0]
        if world:
                return(world)

       
def sysgen(sysname):
        system = {"Stars": [],
                  "Stellar Orbits": ["Primary"],
                  "Planetary System Orbits": [],
                  "Age": 0,
                  "Settlement": random.randint(1,12)*100
                  }
        # Star system generation:
        main_sequence, brown_dwarf = False, False
        while not (main_sequence or brown_dwarf):
                a = d(6)
                b = d(6)
                if a >= 4:
                        main_sequence = True
                if b >= 4:
                        brown_dwarf = True
        age = d(6)+d(6)+d(6)-3
        system["Age"] = age
        stars = []
        if main_sequence:
                numstars = d(6)+d(6)+d(6)
                if numstars <= 10:
                        numstars = 1
                elif numstars >= 16:
                        numstars = 3
                else:
                        numstars = 2
                stars = [0]*numstars
                for star in range(numstars):
                        if star == 0:
                                stars[0] = d(6)+d(6)
                        else:
                                stars[star] = stars[0] + d(6) - 1
                for star in range(numstars):
                        if stars[star] == 2:
                                if age <= 2:
                                        stars[star] = "A V"
                                elif age == 3:
                                        age_ = d(6)
                                        if age_ <= 2:
                                               stars[star] = "F IV"
                                        elif age_ == 3:
                                                stars[star] = "K III"
                                        else:
                                                stars[star] = "D"
                                else:
                                        stars[star] = "D"
                        elif stars[star] == 3:
                                if age <= 5:
                                        stars[star] = "F V"
                                elif age == 6:
                                        age_ = d(6)
                                        if age_ <= 4:
                                               stars[star] = "G IV"
                                        else:
                                                stars[star] = "M III"
                                else:
                                        stars[star] = "D"
                        elif stars[star] == 4:
                                if age <= 11:
                                        stars[star] = "G V"
                                elif age == 12 or age == 13:
                                        age_ = d(6)
                                        if age_ <= 3:
                                               stars[star] = "K IV"
                                        else:
                                                stars[star] = "M III"
                                else:
                                        stars[star] = "D"
                        elif stars[star] == 5:
                                stars[star] = "K V"
                        elif 6 <= stars[star] <= 13:
                                age_ = d(6) + d(6)
                                if len(stars) > 1:
                                        age_ += 2
                                if age_ <= 9:
                                        stars[star] = "M V"
                                elif 10 <= age_ <= 12:
                                        stars[star] = "M Ve"
                                else:
                                        stars[star] = "L"
                        else:
                                stars[star] = "L"
        if brown_dwarf:
                stars += ["L"]
        
                
        # Determine the position of each star relative to the primary.
        # If primary or distant, generate a planetary system.
        for i in range(len(stars)):
                orbit = "Primary"
                if " " in stars[i]:
                        stars[i] = stars[i].replace(" ", str(random.randint(0,9)))
                if i >= 1:
                        orbit = d(6)
                        if orbit <= 2:
                                orbit = "Tight"
                        elif 3 <= orbit <= 4:
                                orbit = "Close"
                        elif orbit == 5:
                                orbit = "Moderate"
                        else:
                                orbit = "Distant"

                        system["Stellar Orbits"] += [orbit]
                if i == 0 or orbit == "Distant":
                        system["Planetary System Orbits"] += [orbits(stars[i], system, orbit)]
                else: 
                        system["Planetary System Orbits"] += [""]
        system["Stars"] = stars
        # PBG
        system_string = str(system)
        B = system_string.count("Belt")
        G = system_string.count("Giant")
        stars = []
        world_tot = 0
        moon_tot = 0
        worlds = system["Planetary System Orbits"]
        system_clean = {"Details": {"Name": sysname,
                                      "Age": system["Age"],
                                      "Fluff": "",
                                      "Settlement": system["Settlement"],
                                      "Belts": B,
                                      "Giants": G,
                                      "Stars": len(stars),
                                    },
                        "Stars": {}}
        for i in range(len(system["Stars"])):
                star = {"Name": sysname + " " + chr(65+i),
                        "Designation": chr(65+i),
                        "Position": system["Stellar Orbits"][i],
                        "Class": system["Stars"][i],
                        }
                epistellar_worlds = {}
                inner_worlds = {}
                outer_worlds = {}
                count_orbit = 1
                count_pos = 1

                if worlds[i]:
                        for world in worlds[i][1]["Epistellar"]:
                                world_tot += 1
                                sats = {}
                                if len(world) > 1:
                                        count_sat = 1
                                        for sat in world[1:]:
                                                moon_tot += 1
                                                sats[str(count_sat)] = {"Name": sysname + " " + chr(65+i) + str(count_orbit) + "-" + str(count_sat),
                                                                        "Type": sat[0],
                                                                        "UWP": sat[1],
                                                                        "Primary": chr(65+i),
                                                                        "Position": str(count_orbit) + "-" + str(count_sat),
                                                                        "Fluff": ""
                                                                        }
                                                count_sat += 1
                                                
                                world = {"Name": sysname + " " + chr(65+i) + str(count_orbit),
                                         "Type": world[0][0],
                                         "UWP": world[0][1],
                                         "Primary": chr(65+i),
                                         "Position": "E" + str(count_pos),
                                         "Orbit": count_orbit,
                                         "Satellites": sats,
                                         "Fluff": ""}
                                epistellar_worlds[str(count_orbit)] = world
                                count_orbit += 1
                                count_pos += 1
                        for world in worlds[i][1]["Inner"]:
                                world_tot += 1
                                sats = {}
                                if len(world) > 1:
                                        count_sat = 1                                
                                        for sat in world[1:]:
                                                moon_tot += 1
                                                sats[str(count_sat)] = {"Name": sysname + " " + chr(65+i) + str(count_orbit) + "-" + str(count_sat),
                                                                        "Type": sat[0],
                                                                        "UWP": sat[1],
                                                                        "Primary": chr(65+i),
                                                                        "Position": str(count_orbit) + "-" + str(count_sat),
                                                                        "Fluff": ""
                                                                        }
                                                count_sat += 1
                                                
                                world = {"Name": sysname + " " + chr(65+i) + str(count_orbit),
                                         "Type": world[0][0],
                                         "UWP": world[0][1],
                                         "Primary": chr(65+i),
                                         "Position": "I" + str(count_pos),
                                         "Orbit": count_orbit,
                                         "Satellites": sats,
                                         "Fluff": ""}
                                inner_worlds[str(count_orbit)] = world
                                count_orbit += 1
                                count_pos += 1
                        for world in worlds[i][1]["Outer"]:
                                world_tot += 1
                                sats = {}
                                if len(world) > 1:
                                        count_sat = 1                                
                                        for sat in world[1:]:
                                                moon_tot += 1
                                                sats[str(count_sat)] = {"Name": sysname + " " + chr(65+i) + str(count_orbit) + "-" + str(count_sat),
                                                                        "Type": sat[0],
                                                                        "UWP": sat[1],
                                                                        "Primary": chr(65+i),
                                                                        "Position": str(count_orbit) + "-" + str(count_sat),
                                                                        "Fluff": ""
                                                                        }
                                                count_sat += 1
                                                
                                world = {"Name": sysname + " " + chr(65+i) + str(count_orbit),
                                         "Type": world[0][0],
                                         "UWP": world[0][1],
                                         "Primary": chr(65+i),
                                         "Position": "O" + str(count_pos),
                                         "Orbit": count_orbit,
                                         "Satellites": sats,
                                         "Fluff": ""}
                                outer_worlds[str(count_orbit)] = world
                                count_orbit += 1
                                count_pos += 1
                                               
                        star["System"] = {"Epistellar": epistellar_worlds,
                                           "Inner": inner_worlds,
                                           "Outer": outer_worlds}
                else:
                        star["System"] = "NA"
                system_clean["Stars"][chr(65+i)] = star   
        system_clean["Details"]["Worlds"] = world_tot
        system_clean["Details"]["Moons"] = moon_tot
        mainworld(system_clean)
        dump_json(system_clean, sysname)
        return(system_clean)

def mainworld(system):
        mainworld = "X000000-0-000"
        #            0123456789ABC
        better = False
        for star in system["Stars"]:
                for orbit in system["Stars"][star]["System"]:
                        for body in system["Stars"][star]["System"][orbit]:
                                planet = system["Stars"][star]["System"][orbit][body]
                                uwp = planet["UWP"]
                                if uwp[0] < mainworld[0]:
                                        better = True
                                elif uwp[0] == mainworld[0]:
                                        if e_dec(uwp[11]) > e_dec(mainworld[11]):
                                                better = True
                                        elif e_dec(uwp[11]) == e_dec(mainworld[11]):
                                                if e_dec(uwp[4]) > e_dec(mainworld[4]):
                                                        better = True
                                                elif e_dec(uwp[4]) == e_dec(mainworld[4]):
                                                        if e_dec(uwp[6]) < e_dec(mainworld[6]):
                                                                better = True
                                if better == True:
                                        mainworld = uwp
                                        a = star
                                        b = orbit
                                        c = body
                                        d = False
                                        better = False
                                if planet["Satellites"]:
                                        for sat in planet["Satellites"]:
                                                uwp = planet["Satellites"][sat]["UWP"]
                                                if uwp[0] < mainworld[0]:
                                                        better = True
                                                elif uwp[0] == mainworld[0]:
                                                        if e_dec(uwp[11]) > e_dec(mainworld[11]):
                                                                better = True
                                                        elif e_dec(uwp[11]) == e_dec(mainworld[11]):
                                                                if e_dec(uwp[4]) > e_dec(mainworld[4]):
                                                                        better = True
                                                                elif e_dec(uwp[4]) == e_dec(mainworld[4]):
                                                                        if e_dec(uwp[6]) < e_dec(mainworld[6]):
                                                                                better = True
                                                if better == True:
                                                        mainworld = uwp
                                                        a = star
                                                        b = orbit
                                                        c = body
                                                        d = sat
                                                        better = False
        if not d:
                system["Stars"][a]["System"][b][c]["UWP"] = mainworld + " A"
        else:
                system["Stars"][a]["System"][b][c]["Satellites"][d]["UWP"] = mainworld + " A"
                                                
        

def dump_json(d, name):
        with open(name + ".json", "w") as f:
                json.dump(d, f, sort_keys=True, indent=4, separators=(',', ': '))