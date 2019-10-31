def label_format(d):
    s = d["Details"]["Name"] + "\n"
    ##FLUFF
    stars = d["Stars"]
    star = stars["A"]
    s += star["Name"] + " (" + star["Position"] + ") - " + star["Class"] + "\n"
    t_companion = False  # Tight or Close companion
    m_companion = False  # Moderate companion
    d_companion = False  # Distant companion
    
    for star in sorted(stars)[1:]:
        star = stars[star]
        if star["Position"] in ["Tight", "Close"]:
            t_companion = True
        if star["Position"] == "Moderate":
            m_companion = True
        if star["Position"] == "Distant":
            d_companion = True

    if t_companion:
        for star in sorted(stars)[1:]:
            star = stars[star]
            if star["Position"] in ["Tight", "Close"]:
                s += "├── " + star["Name"] + " (" + star["Position"] + " Companion) - "+ star["Class"] + "\n"

    for orbit in ["Epistellar", "Inner", "Outer"]:
        ko = "├"
        ro = "│"
        if orbit == "Outer" and m_companion == False:
            ko = "└"
            ro = "  "
        s += ko + "── " + orbit + "\n"
        worlds = stars["A"]["System"][orbit]
        if worlds:
            for world in sorted(worlds):
                kw = "├"
                rw = "│"
                if world == sorted(worlds)[-1]:
                    kw = "└"
                    rw = " "
                world = worlds[world]
                s += ro + "      " + kw + "── " + world["Name"] + "\n"
                s += ro + "      " + rw + "     " + world["Type"] + "\n"
                s += ro + "      " + rw + "     " + world["UWP"] + "\n"
                if world["Satellites"]:
                    ks = "│"
                    s += ro + "      " + rw + "          " + ks + "\n"
                    ks = "├"
                    rs = "│"
                    for sat in sorted(world["Satellites"]):
                        if sat == sorted(world["Satellites"])[-1]:
                            ks = "└"
                            rs = " "
                        sat = world["Satellites"][sat]
                        s += ro + "      " + rw + "          " + ks + "── " + sat["Name"] + "\n"
                        s += ro + "      " + rw + "          " + rs + "     " + sat["Type"] + "\n"
                        s += ro + "      " + rw + "          " + rs + "     " + sat["UWP"] + "\n"
                        s += ro + "      " + rw + "          " + rs + "\n"
                else:
                    s += ro + "      " + rw + "\n"
        else:
            kw = "└"
            s += ro + "      " + kw + "── " + "Nothing\n"
            s += ro + "\n"
            
    if m_companion:
        for star in sorted(stars)[1:]:
            if stars[star]["Position"] == "Moderate":
                k = "├"
                if star == sorted(stars)[-1]:
                    k = "└"
                else:
                    if stars[chr(ord(star)+1)]["Position"] == "Distant":
                        k = "└"
                star = stars[star]
                s += ro +"\n"
                s += k + "── " + star["Name"] + " (" + star["Position"] + " Companion) - "+ star["Class"] + "\n"

    if d_companion:
        for star in sorted(stars)[1:]:
            if stars[star]["Position"] == "Distant":
                star = stars[star]
                s += "\n\n"
                s += star["Name"] + " (" + star["Position"] + ") - " + star["Class"] + "\n"
                for orbit in ["Epistellar", "Inner", "Outer"]:
                    ko = "├"
                    ro = "│"
                    if orbit == "Outer" and m_companion == False:
                        ko = "└"
                        ro = "  "
                    s += ko + "── " + orbit + "\n"
                    worlds = stars["A"]["System"][orbit]
                    if worlds:
                        for world in sorted(worlds):
                            kw = "├"
                            rw = "│"
                            if world == sorted(worlds)[-1]:
                                kw = "└"
                                rw = "  "
                            world = worlds[world]
                            s += ro + "      " + kw + "── " + world["Name"] + "\n"
                            s += ro + "      " + rw + "     " + world["Type"] + "\n"
                            s += ro + "      " + rw + "     " + world["UWP"] + "\n"
                            if world["Satellites"]:
                                ks = "│"
                                s += ro + "      " + rw + "          " + ks + "\n"
                                ks = "├"
                                rs = "│"
                                for sat in sorted(world["Satellites"]):
                                    if sat == sorted(world["Satellites"])[-1]:
                                        ks = "└"
                                        rs = "  "
                                    sat = world["Satellites"][sat]
                                    s += ro + "      " + rw + "          " + ks + "── " + sat["Name"] + "\n"
                                    s += ro + "      " + rw + "          " + rs + "     " + sat["Type"] + "\n"
                                    s += ro + "      " + rw + "          " + rs + "     " + sat["UWP"] + "\n"
                                    s += ro + "      " + rw + "          " + rs + "\n"
                            else:
                                s += ro + "      " + rw + "\n"
                    else:
                        s += ro + "      " + kw + "── " + "Nothing\n"
                        s += ro + "\n"
    return(s)
