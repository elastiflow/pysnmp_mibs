# SNMP MIB module (EXTREME-HARDWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/extreme_1916/EXTREME-HARDWARE-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:23:18 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(extremenetworks,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremenetworks")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

extremeHardware = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5)
)
if mibBuilder.loadTexts:
    extremeHardware.setRevisions(
        ("2020-01-07 22:43",
         "2019-11-20 20:14",
         "2019-09-04 21:20",
         "2019-08-01 17:14")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeG8x_ObjectIdentity = ObjectIdentity
extremeG8x = _ExtremeG8x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 1)
)
if mibBuilder.loadTexts:
    extremeG8x.setStatus("current")
_ExtremeMsmG8x_ObjectIdentity = ObjectIdentity
extremeMsmG8x = _ExtremeMsmG8x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 2)
)
if mibBuilder.loadTexts:
    extremeMsmG8x.setStatus("current")
_ExtremeG48t_ObjectIdentity = ObjectIdentity
extremeG48t = _ExtremeG48t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 3)
)
if mibBuilder.loadTexts:
    extremeG48t.setStatus("current")
_ExtremeG48p_ObjectIdentity = ObjectIdentity
extremeG48p = _ExtremeG48p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 4)
)
if mibBuilder.loadTexts:
    extremeG48p.setStatus("current")
_ExtremeG24x_ObjectIdentity = ObjectIdentity
extremeG24x = _ExtremeG24x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 5)
)
if mibBuilder.loadTexts:
    extremeG24x.setStatus("current")
_Extreme10g4x_ObjectIdentity = ObjectIdentity
extreme10g4x = _Extreme10g4x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 6)
)
if mibBuilder.loadTexts:
    extreme10g4x.setStatus("current")
_ExtremeG48te_ObjectIdentity = ObjectIdentity
extremeG48te = _ExtremeG48te_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 7)
)
if mibBuilder.loadTexts:
    extremeG48te.setStatus("current")
_ExtremeG48pe_ObjectIdentity = ObjectIdentity
extremeG48pe = _ExtremeG48pe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 8)
)
if mibBuilder.loadTexts:
    extremeG48pe.setStatus("current")
_ExtremeG48ta_ObjectIdentity = ObjectIdentity
extremeG48ta = _ExtremeG48ta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 9)
)
if mibBuilder.loadTexts:
    extremeG48ta.setStatus("current")
_ExtremeG48pa_ObjectIdentity = ObjectIdentity
extremeG48pa = _ExtremeG48pa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 10)
)
if mibBuilder.loadTexts:
    extremeG48pa.setStatus("current")
_ExtremeG48xa_ObjectIdentity = ObjectIdentity
extremeG48xa = _ExtremeG48xa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 11)
)
if mibBuilder.loadTexts:
    extremeG48xa.setStatus("current")
_ExtremeMsm48_ObjectIdentity = ObjectIdentity
extremeMsm48 = _ExtremeMsm48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 12)
)
if mibBuilder.loadTexts:
    extremeMsm48.setStatus("current")
_Extreme10g4ca_ObjectIdentity = ObjectIdentity
extreme10g4ca = _Extreme10g4ca_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 13)
)
if mibBuilder.loadTexts:
    extreme10g4ca.setStatus("current")
_Extreme10g4xa_ObjectIdentity = ObjectIdentity
extreme10g4xa = _Extreme10g4xa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 14)
)
if mibBuilder.loadTexts:
    extreme10g4xa.setStatus("current")
_ExtremeG48tc_ObjectIdentity = ObjectIdentity
extremeG48tc = _ExtremeG48tc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 15)
)
if mibBuilder.loadTexts:
    extremeG48tc.setStatus("current")
_ExtremeG48te2_ObjectIdentity = ObjectIdentity
extremeG48te2 = _ExtremeG48te2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 16)
)
if mibBuilder.loadTexts:
    extremeG48te2.setStatus("current")
_ExtremeG48tcPoe_ObjectIdentity = ObjectIdentity
extremeG48tcPoe = _ExtremeG48tcPoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 17)
)
if mibBuilder.loadTexts:
    extremeG48tcPoe.setStatus("current")
_ExtremeG48te2Poe_ObjectIdentity = ObjectIdentity
extremeG48te2Poe = _ExtremeG48te2Poe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 18)
)
if mibBuilder.loadTexts:
    extremeG48te2Poe.setStatus("current")
_ExtremeG48xc_ObjectIdentity = ObjectIdentity
extremeG48xc = _ExtremeG48xc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 19)
)
if mibBuilder.loadTexts:
    extremeG48xc.setStatus("current")
_ExtremeG24xc_ObjectIdentity = ObjectIdentity
extremeG24xc = _ExtremeG24xc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 20)
)
if mibBuilder.loadTexts:
    extremeG24xc.setStatus("current")
_Extreme10g8xc_ObjectIdentity = ObjectIdentity
extreme10g8xc = _Extreme10g8xc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 21)
)
if mibBuilder.loadTexts:
    extreme10g8xc.setStatus("current")
_Extreme10g4xc_ObjectIdentity = ObjectIdentity
extreme10g4xc = _Extreme10g4xc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 22)
)
if mibBuilder.loadTexts:
    extreme10g4xc.setStatus("current")
_ExtremeMsm48c_ObjectIdentity = ObjectIdentity
extremeMsm48c = _ExtremeMsm48c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 23)
)
if mibBuilder.loadTexts:
    extremeMsm48c.setStatus("current")
_ExtremeG8xc_ObjectIdentity = ObjectIdentity
extremeG8xc = _ExtremeG8xc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 24)
)
if mibBuilder.loadTexts:
    extremeG8xc.setStatus("current")
_Extreme10g1xc_ObjectIdentity = ObjectIdentity
extreme10g1xc = _Extreme10g1xc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 25)
)
if mibBuilder.loadTexts:
    extreme10g1xc.setStatus("current")
_Extreme8900Msm128_ObjectIdentity = ObjectIdentity
extreme8900Msm128 = _Extreme8900Msm128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 26)
)
if mibBuilder.loadTexts:
    extreme8900Msm128.setStatus("current")
_Extreme890010g24xC_ObjectIdentity = ObjectIdentity
extreme890010g24xC = _Extreme890010g24xC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 27)
)
if mibBuilder.loadTexts:
    extreme890010g24xC.setStatus("current")
_Extreme890010g8xXl_ObjectIdentity = ObjectIdentity
extreme890010g8xXl = _Extreme890010g8xXl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 28)
)
if mibBuilder.loadTexts:
    extreme890010g8xXl.setStatus("current")
_Extreme8900G48tXl_ObjectIdentity = ObjectIdentity
extreme8900G48tXl = _Extreme8900G48tXl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 29)
)
if mibBuilder.loadTexts:
    extreme8900G48tXl.setStatus("current")
_Extreme8900G48xXl_ObjectIdentity = ObjectIdentity
extreme8900G48xXl = _Extreme8900G48xXl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 30)
)
if mibBuilder.loadTexts:
    extreme8900G48xXl.setStatus("current")
_Extreme8900G96tC_ObjectIdentity = ObjectIdentity
extreme8900G96tC = _Extreme8900G96tC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 31)
)
if mibBuilder.loadTexts:
    extreme8900G96tC.setStatus("current")
_Extreme8900G48tXlP_ObjectIdentity = ObjectIdentity
extreme8900G48tXlP = _Extreme8900G48tXlP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 32)
)
if mibBuilder.loadTexts:
    extreme8900G48tXlP.setStatus("current")
_Extreme8500Msm24_ObjectIdentity = ObjectIdentity
extreme8500Msm24 = _Extreme8500Msm24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 33)
)
if mibBuilder.loadTexts:
    extreme8500Msm24.setStatus("current")
_Extreme8500G24xE_ObjectIdentity = ObjectIdentity
extreme8500G24xE = _Extreme8500G24xE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 34)
)
if mibBuilder.loadTexts:
    extreme8500G24xE.setStatus("current")
_Extreme8500G48tE_ObjectIdentity = ObjectIdentity
extreme8500G48tE = _Extreme8500G48tE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 35)
)
if mibBuilder.loadTexts:
    extreme8500G48tE.setStatus("current")
_Extreme8500G48tEP_ObjectIdentity = ObjectIdentity
extreme8500G48tEP = _Extreme8500G48tEP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 36)
)
if mibBuilder.loadTexts:
    extreme8500G48tEP.setStatus("current")
_Extreme10g2xc_ObjectIdentity = ObjectIdentity
extreme10g2xc = _Extreme10g2xc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 37)
)
if mibBuilder.loadTexts:
    extreme10g2xc.setStatus("current")
_Extreme890040g6xXm_ObjectIdentity = ObjectIdentity
extreme890040g6xXm = _Extreme890040g6xXm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 38)
)
if mibBuilder.loadTexts:
    extreme890040g6xXm.setStatus("current")
_Extreme8900Msm96_ObjectIdentity = ObjectIdentity
extreme8900Msm96 = _Extreme8900Msm96_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 39)
)
if mibBuilder.loadTexts:
    extreme8900Msm96.setStatus("current")
_ExtremeBdxMm1_ObjectIdentity = ObjectIdentity
extremeBdxMm1 = _ExtremeBdxMm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 40)
)
if mibBuilder.loadTexts:
    extremeBdxMm1.setStatus("current")
_ExtremeBdxa10g48x_ObjectIdentity = ObjectIdentity
extremeBdxa10g48x = _ExtremeBdxa10g48x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 41)
)
if mibBuilder.loadTexts:
    extremeBdxa10g48x.setStatus("current")
_ExtremeBdxa10g48x0_ObjectIdentity = ObjectIdentity
extremeBdxa10g48x0 = _ExtremeBdxa10g48x0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 42)
)
if mibBuilder.loadTexts:
    extremeBdxa10g48x0.setStatus("current")
_ExtremeBdxa10g24x_ObjectIdentity = ObjectIdentity
extremeBdxa10g24x = _ExtremeBdxa10g24x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 43)
)
if mibBuilder.loadTexts:
    extremeBdxa10g24x.setStatus("current")
_ExtremeBdxa40g24x_ObjectIdentity = ObjectIdentity
extremeBdxa40g24x = _ExtremeBdxa40g24x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 44)
)
if mibBuilder.loadTexts:
    extremeBdxa40g24x.setStatus("current")
_ExtremeBdxa40g12x_ObjectIdentity = ObjectIdentity
extremeBdxa40g12x = _ExtremeBdxa40g12x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 45)
)
if mibBuilder.loadTexts:
    extremeBdxa40g12x.setStatus("current")
_ExtremeBdxaFm20t_ObjectIdentity = ObjectIdentity
extremeBdxaFm20t = _ExtremeBdxaFm20t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 46)
)
if mibBuilder.loadTexts:
    extremeBdxaFm20t.setStatus("current")
_ExtremeBdxaFm10t_ObjectIdentity = ObjectIdentity
extremeBdxaFm10t = _ExtremeBdxaFm10t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 47)
)
if mibBuilder.loadTexts:
    extremeBdxaFm10t.setStatus("current")
_ExtremeBdxa10g48t_ObjectIdentity = ObjectIdentity
extremeBdxa10g48t = _ExtremeBdxa10g48t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 48)
)
if mibBuilder.loadTexts:
    extremeBdxa10g48t.setStatus("current")
_ExtremeBdxb40g12xXl_ObjectIdentity = ObjectIdentity
extremeBdxb40g12xXl = _ExtremeBdxb40g12xXl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 49)
)
if mibBuilder.loadTexts:
    extremeBdxb40g12xXl.setStatus("current")
_ExtremeBdxb100g4xXl_ObjectIdentity = ObjectIdentity
extremeBdxb100g4xXl = _ExtremeBdxb100g4xXl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 50)
)
if mibBuilder.loadTexts:
    extremeBdxb100g4xXl.setStatus("current")
_ExtremeBdxb100g4x_ObjectIdentity = ObjectIdentity
extremeBdxb100g4x = _ExtremeBdxb100g4x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 51)
)
if mibBuilder.loadTexts:
    extremeBdxb100g4x.setStatus("current")
_ExtremeBdxaG48t_ObjectIdentity = ObjectIdentity
extremeBdxaG48t = _ExtremeBdxaG48t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 52)
)
if mibBuilder.loadTexts:
    extremeBdxaG48t.setStatus("current")
_ExtremeBdxaG48x_ObjectIdentity = ObjectIdentity
extremeBdxaG48x = _ExtremeBdxaG48x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 53)
)
if mibBuilder.loadTexts:
    extremeBdxaG48x.setStatus("current")
_ExtremeBdxaG48x0_ObjectIdentity = ObjectIdentity
extremeBdxaG48x0 = _ExtremeBdxaG48x0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 54)
)
if mibBuilder.loadTexts:
    extremeBdxaG48x0.setStatus("current")
_ExtremeXcm_ObjectIdentity = ObjectIdentity
extremeXcm = _ExtremeXcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 55)
)
if mibBuilder.loadTexts:
    extremeXcm.setStatus("current")
_ExtremeXcm88s1_ObjectIdentity = ObjectIdentity
extremeXcm88s1 = _ExtremeXcm88s1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 56)
)
if mibBuilder.loadTexts:
    extremeXcm88s1.setStatus("current")
_ExtremeXcm8848t_ObjectIdentity = ObjectIdentity
extremeXcm8848t = _ExtremeXcm8848t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 57)
)
if mibBuilder.loadTexts:
    extremeXcm8848t.setStatus("current")
_ExtremeXcm8848tP_ObjectIdentity = ObjectIdentity
extremeXcm8848tP = _ExtremeXcm8848tP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 58)
)
if mibBuilder.loadTexts:
    extremeXcm8848tP.setStatus("current")
_ExtremeXcm8824f_ObjectIdentity = ObjectIdentity
extremeXcm8824f = _ExtremeXcm8824f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 59)
)
if mibBuilder.loadTexts:
    extremeXcm8824f.setStatus("current")
_ExtremeXcm8808x_ObjectIdentity = ObjectIdentity
extremeXcm8808x = _ExtremeXcm8808x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 60)
)
if mibBuilder.loadTexts:
    extremeXcm8808x.setStatus("current")
_ExtremeXcm888f_ObjectIdentity = ObjectIdentity
extremeXcm888f = _ExtremeXcm888f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 61)
)
if mibBuilder.loadTexts:
    extremeXcm888f.setStatus("current")
_ExtremeX77032q_ObjectIdentity = ObjectIdentity
extremeX77032q = _ExtremeX77032q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 62)
)
if mibBuilder.loadTexts:
    extremeX77032q.setStatus("current")
_ExtremeX670g248x4q_ObjectIdentity = ObjectIdentity
extremeX670g248x4q = _ExtremeX670g248x4q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 63)
)
if mibBuilder.loadTexts:
    extremeX670g248x4q.setStatus("current")
_ExtremeX670g272x_ObjectIdentity = ObjectIdentity
extremeX670g272x = _ExtremeX670g272x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 64)
)
if mibBuilder.loadTexts:
    extremeX670g272x.setStatus("current")
_ExtremeX460g224t10g4_ObjectIdentity = ObjectIdentity
extremeX460g224t10g4 = _ExtremeX460g224t10g4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 65)
)
if mibBuilder.loadTexts:
    extremeX460g224t10g4.setStatus("current")
_ExtremeX460g224p10g4_ObjectIdentity = ObjectIdentity
extremeX460g224p10g4 = _ExtremeX460g224p10g4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 66)
)
if mibBuilder.loadTexts:
    extremeX460g224p10g4.setStatus("current")
_ExtremeX460g224x10g4_ObjectIdentity = ObjectIdentity
extremeX460g224x10g4 = _ExtremeX460g224x10g4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 67)
)
if mibBuilder.loadTexts:
    extremeX460g224x10g4.setStatus("current")
_ExtremeX460g248t10g4_ObjectIdentity = ObjectIdentity
extremeX460g248t10g4 = _ExtremeX460g248t10g4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 68)
)
if mibBuilder.loadTexts:
    extremeX460g248t10g4.setStatus("current")
_ExtremeX460g248p10g4_ObjectIdentity = ObjectIdentity
extremeX460g248p10g4 = _ExtremeX460g248p10g4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 69)
)
if mibBuilder.loadTexts:
    extremeX460g248p10g4.setStatus("current")
_ExtremeX460g224p24hp_ObjectIdentity = ObjectIdentity
extremeX460g224p24hp = _ExtremeX460g224p24hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 70)
)
if mibBuilder.loadTexts:
    extremeX460g224p24hp.setStatus("current")
_ExtremeX460g224t24ht_ObjectIdentity = ObjectIdentity
extremeX460g224t24ht = _ExtremeX460g224t24ht_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 71)
)
if mibBuilder.loadTexts:
    extremeX460g224t24ht.setStatus("current")
_ExtremeX460g248x10g4_ObjectIdentity = ObjectIdentity
extremeX460g248x10g4 = _ExtremeX460g248x10g4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 72)
)
if mibBuilder.loadTexts:
    extremeX460g248x10g4.setStatus("current")
_ExtremeX460g224tG4_ObjectIdentity = ObjectIdentity
extremeX460g224tG4 = _ExtremeX460g224tG4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 73)
)
if mibBuilder.loadTexts:
    extremeX460g224tG4.setStatus("current")
_ExtremeX460g224pG4_ObjectIdentity = ObjectIdentity
extremeX460g224pG4 = _ExtremeX460g224pG4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 74)
)
if mibBuilder.loadTexts:
    extremeX460g224pG4.setStatus("current")
_ExtremeX460g248tG4_ObjectIdentity = ObjectIdentity
extremeX460g248tG4 = _ExtremeX460g248tG4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 75)
)
if mibBuilder.loadTexts:
    extremeX460g248tG4.setStatus("current")
_ExtremeX460g248pG4_ObjectIdentity = ObjectIdentity
extremeX460g248pG4 = _ExtremeX460g248pG4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 76)
)
if mibBuilder.loadTexts:
    extremeX460g248pG4.setStatus("current")
_ExtremeX460g216mp32p_ObjectIdentity = ObjectIdentity
extremeX460g216mp32p = _ExtremeX460g216mp32p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 77)
)
if mibBuilder.loadTexts:
    extremeX460g216mp32p.setStatus("current")
_ExtremeX450g224t10g4_ObjectIdentity = ObjectIdentity
extremeX450g224t10g4 = _ExtremeX450g224t10g4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 78)
)
if mibBuilder.loadTexts:
    extremeX450g224t10g4.setStatus("current")
_ExtremeX450g224p10g4_ObjectIdentity = ObjectIdentity
extremeX450g224p10g4 = _ExtremeX450g224p10g4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 79)
)
if mibBuilder.loadTexts:
    extremeX450g224p10g4.setStatus("current")
_ExtremeX450g248t10g4_ObjectIdentity = ObjectIdentity
extremeX450g248t10g4 = _ExtremeX450g248t10g4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 80)
)
if mibBuilder.loadTexts:
    extremeX450g248t10g4.setStatus("current")
_ExtremeX450g248p10g4_ObjectIdentity = ObjectIdentity
extremeX450g248p10g4 = _ExtremeX450g248p10g4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 81)
)
if mibBuilder.loadTexts:
    extremeX450g248p10g4.setStatus("current")
_ExtremeX450g224tG4_ObjectIdentity = ObjectIdentity
extremeX450g224tG4 = _ExtremeX450g224tG4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 82)
)
if mibBuilder.loadTexts:
    extremeX450g224tG4.setStatus("current")
_ExtremeX450g224pG4_ObjectIdentity = ObjectIdentity
extremeX450g224pG4 = _ExtremeX450g224pG4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 83)
)
if mibBuilder.loadTexts:
    extremeX450g224pG4.setStatus("current")
_ExtremeX450g248tG4_ObjectIdentity = ObjectIdentity
extremeX450g248tG4 = _ExtremeX450g248tG4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 84)
)
if mibBuilder.loadTexts:
    extremeX450g248tG4.setStatus("current")
_ExtremeX450g248pG4_ObjectIdentity = ObjectIdentity
extremeX450g248pG4 = _ExtremeX450g248pG4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 85)
)
if mibBuilder.loadTexts:
    extremeX450g248pG4.setStatus("current")
_ExtremeX440g248p10g4_ObjectIdentity = ObjectIdentity
extremeX440g248p10g4 = _ExtremeX440g248p10g4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 86)
)
if mibBuilder.loadTexts:
    extremeX440g248p10g4.setStatus("current")
_ExtremeX440g248t10g4_ObjectIdentity = ObjectIdentity
extremeX440g248t10g4 = _ExtremeX440g248t10g4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 87)
)
if mibBuilder.loadTexts:
    extremeX440g248t10g4.setStatus("current")
_ExtremeX440g248td10g_ObjectIdentity = ObjectIdentity
extremeX440g248td10g = _ExtremeX440g248td10g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 88)
)
if mibBuilder.loadTexts:
    extremeX440g248td10g.setStatus("current")
_ExtremeX440g224p10g4_ObjectIdentity = ObjectIdentity
extremeX440g224p10g4 = _ExtremeX440g224p10g4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 89)
)
if mibBuilder.loadTexts:
    extremeX440g224p10g4.setStatus("current")
_ExtremeX440g224t10g4_ObjectIdentity = ObjectIdentity
extremeX440g224t10g4 = _ExtremeX440g224t10g4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 90)
)
if mibBuilder.loadTexts:
    extremeX440g224t10g4.setStatus("current")
_ExtremeX440g224td10g_ObjectIdentity = ObjectIdentity
extremeX440g224td10g = _ExtremeX440g224td10g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 91)
)
if mibBuilder.loadTexts:
    extremeX440g224td10g.setStatus("current")
_ExtremeX440g224x10g4_ObjectIdentity = ObjectIdentity
extremeX440g224x10g4 = _ExtremeX440g224x10g4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 92)
)
if mibBuilder.loadTexts:
    extremeX440g224x10g4.setStatus("current")
_ExtremeX440g212p10g4_ObjectIdentity = ObjectIdentity
extremeX440g212p10g4 = _ExtremeX440g212p10g4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 93)
)
if mibBuilder.loadTexts:
    extremeX440g212p10g4.setStatus("current")
_ExtremeX440g212t10g4_ObjectIdentity = ObjectIdentity
extremeX440g212t10g4 = _ExtremeX440g212t10g4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 94)
)
if mibBuilder.loadTexts:
    extremeX440g212t10g4.setStatus("current")
_ExtremeX440g212t8fxg4_ObjectIdentity = ObjectIdentity
extremeX440g212t8fxg4 = _ExtremeX440g212t8fxg4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 95)
)
if mibBuilder.loadTexts:
    extremeX440g212t8fxg4.setStatus("current")
_ExtremeX440g224tG4_ObjectIdentity = ObjectIdentity
extremeX440g224tG4 = _ExtremeX440g224tG4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 96)
)
if mibBuilder.loadTexts:
    extremeX440g224tG4.setStatus("current")
_ExtremeX440g224fxG4_ObjectIdentity = ObjectIdentity
extremeX440g224fxG4 = _ExtremeX440g224fxG4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 97)
)
if mibBuilder.loadTexts:
    extremeX440g224fxG4.setStatus("current")
_ExtremeX62016t_ObjectIdentity = ObjectIdentity
extremeX62016t = _ExtremeX62016t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 98)
)
if mibBuilder.loadTexts:
    extremeX62016t.setStatus("current")
_ExtremeX62016p_ObjectIdentity = ObjectIdentity
extremeX62016p = _ExtremeX62016p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 99)
)
if mibBuilder.loadTexts:
    extremeX62016p.setStatus("current")
_ExtremeX62016x_ObjectIdentity = ObjectIdentity
extremeX62016x = _ExtremeX62016x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 100)
)
if mibBuilder.loadTexts:
    extremeX62016x.setStatus("current")
_ExtremeX62010x_ObjectIdentity = ObjectIdentity
extremeX62010x = _ExtremeX62010x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 101)
)
if mibBuilder.loadTexts:
    extremeX62010x.setStatus("current")
_ExtremeX6208t2x_ObjectIdentity = ObjectIdentity
extremeX6208t2x = _ExtremeX6208t2x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 102)
)
if mibBuilder.loadTexts:
    extremeX6208t2x.setStatus("current")
_ExtremeX87032c_ObjectIdentity = ObjectIdentity
extremeX87032c = _ExtremeX87032c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 103)
)
if mibBuilder.loadTexts:
    extremeX87032c.setStatus("current")
_ExtremeX87096x8c_ObjectIdentity = ObjectIdentity
extremeX87096x8c = _ExtremeX87096x8c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 104)
)
if mibBuilder.loadTexts:
    extremeX87096x8c.setStatus("current")
_ExtremeBpeG24t_ObjectIdentity = ObjectIdentity
extremeBpeG24t = _ExtremeBpeG24t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 105)
)
if mibBuilder.loadTexts:
    extremeBpeG24t.setStatus("current")
_ExtremePe_ObjectIdentity = ObjectIdentity
extremePe = _ExtremePe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 106)
)
if mibBuilder.loadTexts:
    extremePe.setStatus("current")
_ExtremeV40024t10ge2_ObjectIdentity = ObjectIdentity
extremeV40024t10ge2 = _ExtremeV40024t10ge2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 107)
)
if mibBuilder.loadTexts:
    extremeV40024t10ge2.setStatus("current")
_ExtremeV40024p10ge2_ObjectIdentity = ObjectIdentity
extremeV40024p10ge2 = _ExtremeV40024p10ge2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 108)
)
if mibBuilder.loadTexts:
    extremeV40024p10ge2.setStatus("current")
_ExtremeV40048t10ge4_ObjectIdentity = ObjectIdentity
extremeV40048t10ge4 = _ExtremeV40048t10ge4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 109)
)
if mibBuilder.loadTexts:
    extremeV40048t10ge4.setStatus("current")
_ExtremeV40048p10ge4_ObjectIdentity = ObjectIdentity
extremeV40048p10ge4 = _ExtremeV40048p10ge4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 110)
)
if mibBuilder.loadTexts:
    extremeV40048p10ge4.setStatus("current")
_ExtremeX69048t2q4c_ObjectIdentity = ObjectIdentity
extremeX69048t2q4c = _ExtremeX69048t2q4c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 111)
)
if mibBuilder.loadTexts:
    extremeX69048t2q4c.setStatus("current")
_ExtremeX69048x2q4c_ObjectIdentity = ObjectIdentity
extremeX69048x2q4c = _ExtremeX69048x2q4c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 112)
)
if mibBuilder.loadTexts:
    extremeX69048x2q4c.setStatus("current")
_ExtremeX59024t1q2c_ObjectIdentity = ObjectIdentity
extremeX59024t1q2c = _ExtremeX59024t1q2c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 113)
)
if mibBuilder.loadTexts:
    extremeX59024t1q2c.setStatus("current")
_ExtremeX59024x1q2c_ObjectIdentity = ObjectIdentity
extremeX59024x1q2c = _ExtremeX59024x1q2c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 114)
)
if mibBuilder.loadTexts:
    extremeX59024x1q2c.setStatus("current")
_ExtremeStack_ObjectIdentity = ObjectIdentity
extremeStack = _ExtremeStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 115)
)
if mibBuilder.loadTexts:
    extremeStack.setStatus("current")
_ExtremeX46548t_ObjectIdentity = ObjectIdentity
extremeX46548t = _ExtremeX46548t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 116)
)
if mibBuilder.loadTexts:
    extremeX46548t.setStatus("current")
_ExtremeX46548p_ObjectIdentity = ObjectIdentity
extremeX46548p = _ExtremeX46548p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 117)
)
if mibBuilder.loadTexts:
    extremeX46548p.setStatus("current")
_ExtremeX46548w_ObjectIdentity = ObjectIdentity
extremeX46548w = _ExtremeX46548w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 118)
)
if mibBuilder.loadTexts:
    extremeX46548w.setStatus("current")
_ExtremeX46524mu_ObjectIdentity = ObjectIdentity
extremeX46524mu = _ExtremeX46524mu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 119)
)
if mibBuilder.loadTexts:
    extremeX46524mu.setStatus("current")
_ExtremeX46524mu24w_ObjectIdentity = ObjectIdentity
extremeX46524mu24w = _ExtremeX46524mu24w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 120)
)
if mibBuilder.loadTexts:
    extremeX46524mu24w.setStatus("current")
_ExtremeX46524w_ObjectIdentity = ObjectIdentity
extremeX46524w = _ExtremeX46524w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 121)
)
if mibBuilder.loadTexts:
    extremeX46524w.setStatus("current")
_ExtremeV3008p2tW_ObjectIdentity = ObjectIdentity
extremeV3008p2tW = _ExtremeV3008p2tW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 122)
)
if mibBuilder.loadTexts:
    extremeV3008p2tW.setStatus("current")
_ExtremeX43524p4s_ObjectIdentity = ObjectIdentity
extremeX43524p4s = _ExtremeX43524p4s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 123)
)
if mibBuilder.loadTexts:
    extremeX43524p4s.setStatus("current")
_ExtremeX43524t4s_ObjectIdentity = ObjectIdentity
extremeX43524t4s = _ExtremeX43524t4s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 124)
)
if mibBuilder.loadTexts:
    extremeX43524t4s.setStatus("current")
_ExtremeX4358p4s_ObjectIdentity = ObjectIdentity
extremeX4358p4s = _ExtremeX4358p4s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 125)
)
if mibBuilder.loadTexts:
    extremeX4358p4s.setStatus("current")
_ExtremeX4358t4s_ObjectIdentity = ObjectIdentity
extremeX4358t4s = _ExtremeX4358t4s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 126)
)
if mibBuilder.loadTexts:
    extremeX4358t4s.setStatus("current")
_ExtremeX4358p2tW_ObjectIdentity = ObjectIdentity
extremeX4358p2tW = _ExtremeX4358p2tW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 127)
)
if mibBuilder.loadTexts:
    extremeX4358p2tW.setStatus("current")
_ExtremeX46524xe_ObjectIdentity = ObjectIdentity
extremeX46524xe = _ExtremeX46524xe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 128)
)
if mibBuilder.loadTexts:
    extremeX46524xe.setStatus("current")
_ExtremeX46524s_ObjectIdentity = ObjectIdentity
extremeX46524s = _ExtremeX46524s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 129)
)
if mibBuilder.loadTexts:
    extremeX46524s.setStatus("current")
_ExtremeX465i48w_ObjectIdentity = ObjectIdentity
extremeX465i48w = _ExtremeX465i48w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 130)
)
if mibBuilder.loadTexts:
    extremeX465i48w.setStatus("current")
_ExtremeX69548y8c_ObjectIdentity = ObjectIdentity
extremeX69548y8c = _ExtremeX69548y8c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 131)
)
if mibBuilder.loadTexts:
    extremeX69548y8c.setStatus("current")
_ExtremeV3008p2x_ObjectIdentity = ObjectIdentity
extremeV3008p2x = _ExtremeV3008p2x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 132)
)
if mibBuilder.loadTexts:
    extremeV3008p2x.setStatus("current")
_ExtremeV3008t2x_ObjectIdentity = ObjectIdentity
extremeV3008t2x = _ExtremeV3008t2x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 133)
)
if mibBuilder.loadTexts:
    extremeV3008t2x.setStatus("current")
_ExtremeV300ht8p2x_ObjectIdentity = ObjectIdentity
extremeV300ht8p2x = _ExtremeV300ht8p2x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 134)
)
if mibBuilder.loadTexts:
    extremeV300ht8p2x.setStatus("current")
_ExtremeV300ht8t2x_ObjectIdentity = ObjectIdentity
extremeV300ht8t2x = _ExtremeV300ht8t2x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 5, 135)
)
if mibBuilder.loadTexts:
    extremeV300ht8t2x.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-HARDWARE-MIB",
    **{"extremeHardware": extremeHardware,
       "extremeG8x": extremeG8x,
       "extremeMsmG8x": extremeMsmG8x,
       "extremeG48t": extremeG48t,
       "extremeG48p": extremeG48p,
       "extremeG24x": extremeG24x,
       "extreme10g4x": extreme10g4x,
       "extremeG48te": extremeG48te,
       "extremeG48pe": extremeG48pe,
       "extremeG48ta": extremeG48ta,
       "extremeG48pa": extremeG48pa,
       "extremeG48xa": extremeG48xa,
       "extremeMsm48": extremeMsm48,
       "extreme10g4ca": extreme10g4ca,
       "extreme10g4xa": extreme10g4xa,
       "extremeG48tc": extremeG48tc,
       "extremeG48te2": extremeG48te2,
       "extremeG48tcPoe": extremeG48tcPoe,
       "extremeG48te2Poe": extremeG48te2Poe,
       "extremeG48xc": extremeG48xc,
       "extremeG24xc": extremeG24xc,
       "extreme10g8xc": extreme10g8xc,
       "extreme10g4xc": extreme10g4xc,
       "extremeMsm48c": extremeMsm48c,
       "extremeG8xc": extremeG8xc,
       "extreme10g1xc": extreme10g1xc,
       "extreme8900Msm128": extreme8900Msm128,
       "extreme890010g24xC": extreme890010g24xC,
       "extreme890010g8xXl": extreme890010g8xXl,
       "extreme8900G48tXl": extreme8900G48tXl,
       "extreme8900G48xXl": extreme8900G48xXl,
       "extreme8900G96tC": extreme8900G96tC,
       "extreme8900G48tXlP": extreme8900G48tXlP,
       "extreme8500Msm24": extreme8500Msm24,
       "extreme8500G24xE": extreme8500G24xE,
       "extreme8500G48tE": extreme8500G48tE,
       "extreme8500G48tEP": extreme8500G48tEP,
       "extreme10g2xc": extreme10g2xc,
       "extreme890040g6xXm": extreme890040g6xXm,
       "extreme8900Msm96": extreme8900Msm96,
       "extremeBdxMm1": extremeBdxMm1,
       "extremeBdxa10g48x": extremeBdxa10g48x,
       "extremeBdxa10g48x0": extremeBdxa10g48x0,
       "extremeBdxa10g24x": extremeBdxa10g24x,
       "extremeBdxa40g24x": extremeBdxa40g24x,
       "extremeBdxa40g12x": extremeBdxa40g12x,
       "extremeBdxaFm20t": extremeBdxaFm20t,
       "extremeBdxaFm10t": extremeBdxaFm10t,
       "extremeBdxa10g48t": extremeBdxa10g48t,
       "extremeBdxb40g12xXl": extremeBdxb40g12xXl,
       "extremeBdxb100g4xXl": extremeBdxb100g4xXl,
       "extremeBdxb100g4x": extremeBdxb100g4x,
       "extremeBdxaG48t": extremeBdxaG48t,
       "extremeBdxaG48x": extremeBdxaG48x,
       "extremeBdxaG48x0": extremeBdxaG48x0,
       "extremeXcm": extremeXcm,
       "extremeXcm88s1": extremeXcm88s1,
       "extremeXcm8848t": extremeXcm8848t,
       "extremeXcm8848tP": extremeXcm8848tP,
       "extremeXcm8824f": extremeXcm8824f,
       "extremeXcm8808x": extremeXcm8808x,
       "extremeXcm888f": extremeXcm888f,
       "extremeX77032q": extremeX77032q,
       "extremeX670g248x4q": extremeX670g248x4q,
       "extremeX670g272x": extremeX670g272x,
       "extremeX460g224t10g4": extremeX460g224t10g4,
       "extremeX460g224p10g4": extremeX460g224p10g4,
       "extremeX460g224x10g4": extremeX460g224x10g4,
       "extremeX460g248t10g4": extremeX460g248t10g4,
       "extremeX460g248p10g4": extremeX460g248p10g4,
       "extremeX460g224p24hp": extremeX460g224p24hp,
       "extremeX460g224t24ht": extremeX460g224t24ht,
       "extremeX460g248x10g4": extremeX460g248x10g4,
       "extremeX460g224tG4": extremeX460g224tG4,
       "extremeX460g224pG4": extremeX460g224pG4,
       "extremeX460g248tG4": extremeX460g248tG4,
       "extremeX460g248pG4": extremeX460g248pG4,
       "extremeX460g216mp32p": extremeX460g216mp32p,
       "extremeX450g224t10g4": extremeX450g224t10g4,
       "extremeX450g224p10g4": extremeX450g224p10g4,
       "extremeX450g248t10g4": extremeX450g248t10g4,
       "extremeX450g248p10g4": extremeX450g248p10g4,
       "extremeX450g224tG4": extremeX450g224tG4,
       "extremeX450g224pG4": extremeX450g224pG4,
       "extremeX450g248tG4": extremeX450g248tG4,
       "extremeX450g248pG4": extremeX450g248pG4,
       "extremeX440g248p10g4": extremeX440g248p10g4,
       "extremeX440g248t10g4": extremeX440g248t10g4,
       "extremeX440g248td10g": extremeX440g248td10g,
       "extremeX440g224p10g4": extremeX440g224p10g4,
       "extremeX440g224t10g4": extremeX440g224t10g4,
       "extremeX440g224td10g": extremeX440g224td10g,
       "extremeX440g224x10g4": extremeX440g224x10g4,
       "extremeX440g212p10g4": extremeX440g212p10g4,
       "extremeX440g212t10g4": extremeX440g212t10g4,
       "extremeX440g212t8fxg4": extremeX440g212t8fxg4,
       "extremeX440g224tG4": extremeX440g224tG4,
       "extremeX440g224fxG4": extremeX440g224fxG4,
       "extremeX62016t": extremeX62016t,
       "extremeX62016p": extremeX62016p,
       "extremeX62016x": extremeX62016x,
       "extremeX62010x": extremeX62010x,
       "extremeX6208t2x": extremeX6208t2x,
       "extremeX87032c": extremeX87032c,
       "extremeX87096x8c": extremeX87096x8c,
       "extremeBpeG24t": extremeBpeG24t,
       "extremePe": extremePe,
       "extremeV40024t10ge2": extremeV40024t10ge2,
       "extremeV40024p10ge2": extremeV40024p10ge2,
       "extremeV40048t10ge4": extremeV40048t10ge4,
       "extremeV40048p10ge4": extremeV40048p10ge4,
       "extremeX69048t2q4c": extremeX69048t2q4c,
       "extremeX69048x2q4c": extremeX69048x2q4c,
       "extremeX59024t1q2c": extremeX59024t1q2c,
       "extremeX59024x1q2c": extremeX59024x1q2c,
       "extremeStack": extremeStack,
       "extremeX46548t": extremeX46548t,
       "extremeX46548p": extremeX46548p,
       "extremeX46548w": extremeX46548w,
       "extremeX46524mu": extremeX46524mu,
       "extremeX46524mu24w": extremeX46524mu24w,
       "extremeX46524w": extremeX46524w,
       "extremeV3008p2tW": extremeV3008p2tW,
       "extremeX43524p4s": extremeX43524p4s,
       "extremeX43524t4s": extremeX43524t4s,
       "extremeX4358p4s": extremeX4358p4s,
       "extremeX4358t4s": extremeX4358t4s,
       "extremeX4358p2tW": extremeX4358p2tW,
       "extremeX46524xe": extremeX46524xe,
       "extremeX46524s": extremeX46524s,
       "extremeX465i48w": extremeX465i48w,
       "extremeX69548y8c": extremeX69548y8c,
       "extremeV3008p2x": extremeV3008p2x,
       "extremeV3008t2x": extremeV3008t2x,
       "extremeV300ht8p2x": extremeV300ht8p2x,
       "extremeV300ht8t2x": extremeV300ht8t2x}
)
