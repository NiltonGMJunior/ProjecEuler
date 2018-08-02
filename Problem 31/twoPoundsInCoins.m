function cnt = twoPoundsInCoins()

    cnt = 0;
    
    for p100 = 0:2
        for p50 = 0:4
            for p20 = 0:10
                for p10 = 0:20
                    for p5 = 0:40
                        for p2 = 0:100
                            for p1 = 0:200
                                coeffs = [p1 p2 p5 p10 p20 p50 p100];
                                cnt = cnt + isSumTwo(coeffs);
                                disp(coeffs);
                            end
                        end
                    end
                end
            end
        end
    end
    

end

function tf = isSumTwo(coeffs)

    base = [1, 2, 5, 10, 20, 50, 100];
    
    tf = (sum(base.*coeffs) == 200);

end