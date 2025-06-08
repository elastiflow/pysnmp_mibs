# SNMP MIB module (ETHER-CHIPSET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/ETHER-CHIPSET-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 13:46:50 2025
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

(dot3,) = mibBuilder.importSymbols(
    "EtherLike-MIB",
    "dot3")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

etherChipsetMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 70)
)
if mibBuilder.loadTexts:
    etherChipsetMIB.setRevisions(
        ("1999-08-24 04:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dot3ChipSets_ObjectIdentity = ObjectIdentity
dot3ChipSets = _Dot3ChipSets_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8)
)
_Dot3ChipSetAMD_ObjectIdentity = ObjectIdentity
dot3ChipSetAMD = _Dot3ChipSetAMD_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 1)
)
_Dot3ChipSetAMD7990_ObjectIdentity = ObjectIdentity
dot3ChipSetAMD7990 = _Dot3ChipSetAMD7990_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 1)
)
if mibBuilder.loadTexts:
    dot3ChipSetAMD7990.setStatus("current")
_Dot3ChipSetAMD79900_ObjectIdentity = ObjectIdentity
dot3ChipSetAMD79900 = _Dot3ChipSetAMD79900_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 2)
)
if mibBuilder.loadTexts:
    dot3ChipSetAMD79900.setStatus("current")
_Dot3ChipSetAMD79C940_ObjectIdentity = ObjectIdentity
dot3ChipSetAMD79C940 = _Dot3ChipSetAMD79C940_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 3)
)
if mibBuilder.loadTexts:
    dot3ChipSetAMD79C940.setStatus("current")
_Dot3ChipSetAMD79C90_ObjectIdentity = ObjectIdentity
dot3ChipSetAMD79C90 = _Dot3ChipSetAMD79C90_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 4)
)
if mibBuilder.loadTexts:
    dot3ChipSetAMD79C90.setStatus("current")
_Dot3ChipSetAMD79C960_ObjectIdentity = ObjectIdentity
dot3ChipSetAMD79C960 = _Dot3ChipSetAMD79C960_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 5)
)
if mibBuilder.loadTexts:
    dot3ChipSetAMD79C960.setStatus("current")
_Dot3ChipSetAMD79C961_ObjectIdentity = ObjectIdentity
dot3ChipSetAMD79C961 = _Dot3ChipSetAMD79C961_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 6)
)
if mibBuilder.loadTexts:
    dot3ChipSetAMD79C961.setStatus("current")
_Dot3ChipSetAMD79C961A_ObjectIdentity = ObjectIdentity
dot3ChipSetAMD79C961A = _Dot3ChipSetAMD79C961A_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 7)
)
if mibBuilder.loadTexts:
    dot3ChipSetAMD79C961A.setStatus("current")
_Dot3ChipSetAMD79C965_ObjectIdentity = ObjectIdentity
dot3ChipSetAMD79C965 = _Dot3ChipSetAMD79C965_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 8)
)
if mibBuilder.loadTexts:
    dot3ChipSetAMD79C965.setStatus("current")
_Dot3ChipSetAMD79C970_ObjectIdentity = ObjectIdentity
dot3ChipSetAMD79C970 = _Dot3ChipSetAMD79C970_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 9)
)
if mibBuilder.loadTexts:
    dot3ChipSetAMD79C970.setStatus("current")
_Dot3ChipSetAMD79C970A_ObjectIdentity = ObjectIdentity
dot3ChipSetAMD79C970A = _Dot3ChipSetAMD79C970A_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 10)
)
if mibBuilder.loadTexts:
    dot3ChipSetAMD79C970A.setStatus("current")
_Dot3ChipSetAMD79C971_ObjectIdentity = ObjectIdentity
dot3ChipSetAMD79C971 = _Dot3ChipSetAMD79C971_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 11)
)
if mibBuilder.loadTexts:
    dot3ChipSetAMD79C971.setStatus("current")
_Dot3ChipSetAMD79C972_ObjectIdentity = ObjectIdentity
dot3ChipSetAMD79C972 = _Dot3ChipSetAMD79C972_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 12)
)
if mibBuilder.loadTexts:
    dot3ChipSetAMD79C972.setStatus("current")
_Dot3ChipSetIntel_ObjectIdentity = ObjectIdentity
dot3ChipSetIntel = _Dot3ChipSetIntel_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 2)
)
_Dot3ChipSetIntel82586_ObjectIdentity = ObjectIdentity
dot3ChipSetIntel82586 = _Dot3ChipSetIntel82586_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 2, 1)
)
if mibBuilder.loadTexts:
    dot3ChipSetIntel82586.setStatus("current")
_Dot3ChipSetIntel82596_ObjectIdentity = ObjectIdentity
dot3ChipSetIntel82596 = _Dot3ChipSetIntel82596_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 2, 2)
)
if mibBuilder.loadTexts:
    dot3ChipSetIntel82596.setStatus("current")
_Dot3ChipSetIntel82595_ObjectIdentity = ObjectIdentity
dot3ChipSetIntel82595 = _Dot3ChipSetIntel82595_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 2, 3)
)
if mibBuilder.loadTexts:
    dot3ChipSetIntel82595.setStatus("current")
_Dot3ChipSetIntel82557_ObjectIdentity = ObjectIdentity
dot3ChipSetIntel82557 = _Dot3ChipSetIntel82557_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 2, 4)
)
if mibBuilder.loadTexts:
    dot3ChipSetIntel82557.setStatus("current")
_Dot3ChipSetIntel82558_ObjectIdentity = ObjectIdentity
dot3ChipSetIntel82558 = _Dot3ChipSetIntel82558_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 2, 5)
)
if mibBuilder.loadTexts:
    dot3ChipSetIntel82558.setStatus("current")
_Dot3ChipSetSeeq_ObjectIdentity = ObjectIdentity
dot3ChipSetSeeq = _Dot3ChipSetSeeq_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 3)
)
_Dot3ChipSetSeeq8003_ObjectIdentity = ObjectIdentity
dot3ChipSetSeeq8003 = _Dot3ChipSetSeeq8003_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 1)
)
if mibBuilder.loadTexts:
    dot3ChipSetSeeq8003.setStatus("current")
_Dot3ChipSetSeeq80C03_ObjectIdentity = ObjectIdentity
dot3ChipSetSeeq80C03 = _Dot3ChipSetSeeq80C03_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 2)
)
if mibBuilder.loadTexts:
    dot3ChipSetSeeq80C03.setStatus("current")
_Dot3ChipSetSeeq84C30_ObjectIdentity = ObjectIdentity
dot3ChipSetSeeq84C30 = _Dot3ChipSetSeeq84C30_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 3)
)
if mibBuilder.loadTexts:
    dot3ChipSetSeeq84C30.setStatus("current")
_Dot3ChipSetSeeq8431_ObjectIdentity = ObjectIdentity
dot3ChipSetSeeq8431 = _Dot3ChipSetSeeq8431_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 4)
)
if mibBuilder.loadTexts:
    dot3ChipSetSeeq8431.setStatus("current")
_Dot3ChipSetSeeq80C300_ObjectIdentity = ObjectIdentity
dot3ChipSetSeeq80C300 = _Dot3ChipSetSeeq80C300_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 5)
)
if mibBuilder.loadTexts:
    dot3ChipSetSeeq80C300.setStatus("current")
_Dot3ChipSetSeeq84C300_ObjectIdentity = ObjectIdentity
dot3ChipSetSeeq84C300 = _Dot3ChipSetSeeq84C300_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 6)
)
if mibBuilder.loadTexts:
    dot3ChipSetSeeq84C300.setStatus("current")
_Dot3ChipSetSeeq84301_ObjectIdentity = ObjectIdentity
dot3ChipSetSeeq84301 = _Dot3ChipSetSeeq84301_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 7)
)
if mibBuilder.loadTexts:
    dot3ChipSetSeeq84301.setStatus("current")
_Dot3ChipSetSeeq84302_ObjectIdentity = ObjectIdentity
dot3ChipSetSeeq84302 = _Dot3ChipSetSeeq84302_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 8)
)
if mibBuilder.loadTexts:
    dot3ChipSetSeeq84302.setStatus("current")
_Dot3ChipSetSeeq8100_ObjectIdentity = ObjectIdentity
dot3ChipSetSeeq8100 = _Dot3ChipSetSeeq8100_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 9)
)
if mibBuilder.loadTexts:
    dot3ChipSetSeeq8100.setStatus("current")
_Dot3ChipSetNational_ObjectIdentity = ObjectIdentity
dot3ChipSetNational = _Dot3ChipSetNational_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 4)
)
_Dot3ChipSetNational8390_ObjectIdentity = ObjectIdentity
dot3ChipSetNational8390 = _Dot3ChipSetNational8390_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 1)
)
if mibBuilder.loadTexts:
    dot3ChipSetNational8390.setStatus("current")
_Dot3ChipSetNationalSonic_ObjectIdentity = ObjectIdentity
dot3ChipSetNationalSonic = _Dot3ChipSetNationalSonic_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 2)
)
if mibBuilder.loadTexts:
    dot3ChipSetNationalSonic.setStatus("current")
_Dot3ChipSetNational83901_ObjectIdentity = ObjectIdentity
dot3ChipSetNational83901 = _Dot3ChipSetNational83901_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 3)
)
if mibBuilder.loadTexts:
    dot3ChipSetNational83901.setStatus("current")
_Dot3ChipSetNational83902_ObjectIdentity = ObjectIdentity
dot3ChipSetNational83902 = _Dot3ChipSetNational83902_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 4)
)
if mibBuilder.loadTexts:
    dot3ChipSetNational83902.setStatus("current")
_Dot3ChipSetNational83905_ObjectIdentity = ObjectIdentity
dot3ChipSetNational83905 = _Dot3ChipSetNational83905_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 5)
)
if mibBuilder.loadTexts:
    dot3ChipSetNational83905.setStatus("current")
_Dot3ChipSetNational83907_ObjectIdentity = ObjectIdentity
dot3ChipSetNational83907 = _Dot3ChipSetNational83907_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 6)
)
if mibBuilder.loadTexts:
    dot3ChipSetNational83907.setStatus("current")
_Dot3ChipSetNational83916_ObjectIdentity = ObjectIdentity
dot3ChipSetNational83916 = _Dot3ChipSetNational83916_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 7)
)
if mibBuilder.loadTexts:
    dot3ChipSetNational83916.setStatus("current")
_Dot3ChipSetNational83934_ObjectIdentity = ObjectIdentity
dot3ChipSetNational83934 = _Dot3ChipSetNational83934_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 8)
)
if mibBuilder.loadTexts:
    dot3ChipSetNational83934.setStatus("current")
_Dot3ChipSetNational83936_ObjectIdentity = ObjectIdentity
dot3ChipSetNational83936 = _Dot3ChipSetNational83936_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 9)
)
if mibBuilder.loadTexts:
    dot3ChipSetNational83936.setStatus("current")
_Dot3ChipSetFujitsu_ObjectIdentity = ObjectIdentity
dot3ChipSetFujitsu = _Dot3ChipSetFujitsu_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 5)
)
_Dot3ChipSetFujitsu86950_ObjectIdentity = ObjectIdentity
dot3ChipSetFujitsu86950 = _Dot3ChipSetFujitsu86950_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 5, 1)
)
if mibBuilder.loadTexts:
    dot3ChipSetFujitsu86950.setStatus("current")
_Dot3ChipSetFujitsu86960_ObjectIdentity = ObjectIdentity
dot3ChipSetFujitsu86960 = _Dot3ChipSetFujitsu86960_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 5, 2)
)
if mibBuilder.loadTexts:
    dot3ChipSetFujitsu86960.setStatus("current")
_Dot3ChipSetFujitsu86964_ObjectIdentity = ObjectIdentity
dot3ChipSetFujitsu86964 = _Dot3ChipSetFujitsu86964_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 5, 3)
)
if mibBuilder.loadTexts:
    dot3ChipSetFujitsu86964.setStatus("current")
_Dot3ChipSetFujitsu86965A_ObjectIdentity = ObjectIdentity
dot3ChipSetFujitsu86965A = _Dot3ChipSetFujitsu86965A_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 5, 4)
)
if mibBuilder.loadTexts:
    dot3ChipSetFujitsu86965A.setStatus("current")
_Dot3ChipSetFujitsu86965B_ObjectIdentity = ObjectIdentity
dot3ChipSetFujitsu86965B = _Dot3ChipSetFujitsu86965B_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 5, 5)
)
if mibBuilder.loadTexts:
    dot3ChipSetFujitsu86965B.setStatus("current")
_Dot3ChipSetDigital_ObjectIdentity = ObjectIdentity
dot3ChipSetDigital = _Dot3ChipSetDigital_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 6)
)
_Dot3ChipSetDigitalDC21040_ObjectIdentity = ObjectIdentity
dot3ChipSetDigitalDC21040 = _Dot3ChipSetDigitalDC21040_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 6, 1)
)
if mibBuilder.loadTexts:
    dot3ChipSetDigitalDC21040.setStatus("current")
_Dot3ChipSetDigital21041_ObjectIdentity = ObjectIdentity
dot3ChipSetDigital21041 = _Dot3ChipSetDigital21041_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 6, 2)
)
if mibBuilder.loadTexts:
    dot3ChipSetDigital21041.setStatus("current")
_Dot3ChipSetDigital21140_ObjectIdentity = ObjectIdentity
dot3ChipSetDigital21140 = _Dot3ChipSetDigital21140_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 6, 3)
)
if mibBuilder.loadTexts:
    dot3ChipSetDigital21140.setStatus("current")
_Dot3ChipSetDigital21143_ObjectIdentity = ObjectIdentity
dot3ChipSetDigital21143 = _Dot3ChipSetDigital21143_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 6, 4)
)
if mibBuilder.loadTexts:
    dot3ChipSetDigital21143.setStatus("current")
_Dot3ChipSetDigital21340_ObjectIdentity = ObjectIdentity
dot3ChipSetDigital21340 = _Dot3ChipSetDigital21340_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 6, 5)
)
if mibBuilder.loadTexts:
    dot3ChipSetDigital21340.setStatus("current")
_Dot3ChipSetDigital21440_ObjectIdentity = ObjectIdentity
dot3ChipSetDigital21440 = _Dot3ChipSetDigital21440_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 6, 6)
)
if mibBuilder.loadTexts:
    dot3ChipSetDigital21440.setStatus("current")
_Dot3ChipSetDigital21540_ObjectIdentity = ObjectIdentity
dot3ChipSetDigital21540 = _Dot3ChipSetDigital21540_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 6, 7)
)
if mibBuilder.loadTexts:
    dot3ChipSetDigital21540.setStatus("current")
_Dot3ChipSetTI_ObjectIdentity = ObjectIdentity
dot3ChipSetTI = _Dot3ChipSetTI_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 7)
)
_Dot3ChipSetTIE100_ObjectIdentity = ObjectIdentity
dot3ChipSetTIE100 = _Dot3ChipSetTIE100_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 7, 1)
)
if mibBuilder.loadTexts:
    dot3ChipSetTIE100.setStatus("current")
_Dot3ChipSetTIE110_ObjectIdentity = ObjectIdentity
dot3ChipSetTIE110 = _Dot3ChipSetTIE110_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 7, 2)
)
if mibBuilder.loadTexts:
    dot3ChipSetTIE110.setStatus("current")
_Dot3ChipSetTIX3100_ObjectIdentity = ObjectIdentity
dot3ChipSetTIX3100 = _Dot3ChipSetTIX3100_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 7, 3)
)
if mibBuilder.loadTexts:
    dot3ChipSetTIX3100.setStatus("current")
_Dot3ChipSetTIX3150_ObjectIdentity = ObjectIdentity
dot3ChipSetTIX3150 = _Dot3ChipSetTIX3150_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 7, 4)
)
if mibBuilder.loadTexts:
    dot3ChipSetTIX3150.setStatus("current")
_Dot3ChipSetTIX3270_ObjectIdentity = ObjectIdentity
dot3ChipSetTIX3270 = _Dot3ChipSetTIX3270_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 7, 5)
)
if mibBuilder.loadTexts:
    dot3ChipSetTIX3270.setStatus("current")
_Dot3ChipSetToshiba_ObjectIdentity = ObjectIdentity
dot3ChipSetToshiba = _Dot3ChipSetToshiba_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 8)
)
_Dot3ChipSetToshibaTC35815F_ObjectIdentity = ObjectIdentity
dot3ChipSetToshibaTC35815F = _Dot3ChipSetToshibaTC35815F_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 8, 1)
)
if mibBuilder.loadTexts:
    dot3ChipSetToshibaTC35815F.setStatus("current")
_Dot3ChipSetLucent_ObjectIdentity = ObjectIdentity
dot3ChipSetLucent = _Dot3ChipSetLucent_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 9)
)
_Dot3ChipSetLucentATT1MX10_ObjectIdentity = ObjectIdentity
dot3ChipSetLucentATT1MX10 = _Dot3ChipSetLucentATT1MX10_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 9, 1)
)
if mibBuilder.loadTexts:
    dot3ChipSetLucentATT1MX10.setStatus("current")
_Dot3ChipSetLucentLUC3M08_ObjectIdentity = ObjectIdentity
dot3ChipSetLucentLUC3M08 = _Dot3ChipSetLucentLUC3M08_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 9, 2)
)
if mibBuilder.loadTexts:
    dot3ChipSetLucentLUC3M08.setStatus("current")
_Dot3ChipSetGalileo_ObjectIdentity = ObjectIdentity
dot3ChipSetGalileo = _Dot3ChipSetGalileo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 10)
)
_Dot3ChipSetGalileoGT48001_ObjectIdentity = ObjectIdentity
dot3ChipSetGalileoGT48001 = _Dot3ChipSetGalileoGT48001_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 10, 1)
)
if mibBuilder.loadTexts:
    dot3ChipSetGalileoGT48001.setStatus("current")
_Dot3ChipSetGalileoGT48002_ObjectIdentity = ObjectIdentity
dot3ChipSetGalileoGT48002 = _Dot3ChipSetGalileoGT48002_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 10, 2)
)
if mibBuilder.loadTexts:
    dot3ChipSetGalileoGT48002.setStatus("current")
_Dot3ChipSetGalileoGT48004_ObjectIdentity = ObjectIdentity
dot3ChipSetGalileoGT48004 = _Dot3ChipSetGalileoGT48004_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 10, 3)
)
if mibBuilder.loadTexts:
    dot3ChipSetGalileoGT48004.setStatus("current")
_Dot3ChipSetGalileoGT48207_ObjectIdentity = ObjectIdentity
dot3ChipSetGalileoGT48207 = _Dot3ChipSetGalileoGT48207_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 10, 4)
)
if mibBuilder.loadTexts:
    dot3ChipSetGalileoGT48207.setStatus("current")
_Dot3ChipSetGalileoGT48208_ObjectIdentity = ObjectIdentity
dot3ChipSetGalileoGT48208 = _Dot3ChipSetGalileoGT48208_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 10, 5)
)
if mibBuilder.loadTexts:
    dot3ChipSetGalileoGT48208.setStatus("current")
_Dot3ChipSetGalileoGT48212_ObjectIdentity = ObjectIdentity
dot3ChipSetGalileoGT48212 = _Dot3ChipSetGalileoGT48212_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 10, 6)
)
if mibBuilder.loadTexts:
    dot3ChipSetGalileoGT48212.setStatus("current")
_Dot3ChipSetJato_ObjectIdentity = ObjectIdentity
dot3ChipSetJato = _Dot3ChipSetJato_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 11)
)
_Dot3ChipSetJatoJT1001_ObjectIdentity = ObjectIdentity
dot3ChipSetJatoJT1001 = _Dot3ChipSetJatoJT1001_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 11, 1)
)
if mibBuilder.loadTexts:
    dot3ChipSetJatoJT1001.setStatus("current")
_Dot3ChipSetXaQti_ObjectIdentity = ObjectIdentity
dot3ChipSetXaQti = _Dot3ChipSetXaQti_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 12)
)
_Dot3ChipSetXaQtiXQ11800FP_ObjectIdentity = ObjectIdentity
dot3ChipSetXaQtiXQ11800FP = _Dot3ChipSetXaQtiXQ11800FP_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 12, 1)
)
if mibBuilder.loadTexts:
    dot3ChipSetXaQtiXQ11800FP.setStatus("current")
_Dot3ChipSetXaQtiXQ18110FP_ObjectIdentity = ObjectIdentity
dot3ChipSetXaQtiXQ18110FP = _Dot3ChipSetXaQtiXQ18110FP_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 12, 2)
)
if mibBuilder.loadTexts:
    dot3ChipSetXaQtiXQ18110FP.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ETHER-CHIPSET-MIB",
    **{"dot3ChipSets": dot3ChipSets,
       "dot3ChipSetAMD": dot3ChipSetAMD,
       "dot3ChipSetAMD7990": dot3ChipSetAMD7990,
       "dot3ChipSetAMD79900": dot3ChipSetAMD79900,
       "dot3ChipSetAMD79C940": dot3ChipSetAMD79C940,
       "dot3ChipSetAMD79C90": dot3ChipSetAMD79C90,
       "dot3ChipSetAMD79C960": dot3ChipSetAMD79C960,
       "dot3ChipSetAMD79C961": dot3ChipSetAMD79C961,
       "dot3ChipSetAMD79C961A": dot3ChipSetAMD79C961A,
       "dot3ChipSetAMD79C965": dot3ChipSetAMD79C965,
       "dot3ChipSetAMD79C970": dot3ChipSetAMD79C970,
       "dot3ChipSetAMD79C970A": dot3ChipSetAMD79C970A,
       "dot3ChipSetAMD79C971": dot3ChipSetAMD79C971,
       "dot3ChipSetAMD79C972": dot3ChipSetAMD79C972,
       "dot3ChipSetIntel": dot3ChipSetIntel,
       "dot3ChipSetIntel82586": dot3ChipSetIntel82586,
       "dot3ChipSetIntel82596": dot3ChipSetIntel82596,
       "dot3ChipSetIntel82595": dot3ChipSetIntel82595,
       "dot3ChipSetIntel82557": dot3ChipSetIntel82557,
       "dot3ChipSetIntel82558": dot3ChipSetIntel82558,
       "dot3ChipSetSeeq": dot3ChipSetSeeq,
       "dot3ChipSetSeeq8003": dot3ChipSetSeeq8003,
       "dot3ChipSetSeeq80C03": dot3ChipSetSeeq80C03,
       "dot3ChipSetSeeq84C30": dot3ChipSetSeeq84C30,
       "dot3ChipSetSeeq8431": dot3ChipSetSeeq8431,
       "dot3ChipSetSeeq80C300": dot3ChipSetSeeq80C300,
       "dot3ChipSetSeeq84C300": dot3ChipSetSeeq84C300,
       "dot3ChipSetSeeq84301": dot3ChipSetSeeq84301,
       "dot3ChipSetSeeq84302": dot3ChipSetSeeq84302,
       "dot3ChipSetSeeq8100": dot3ChipSetSeeq8100,
       "dot3ChipSetNational": dot3ChipSetNational,
       "dot3ChipSetNational8390": dot3ChipSetNational8390,
       "dot3ChipSetNationalSonic": dot3ChipSetNationalSonic,
       "dot3ChipSetNational83901": dot3ChipSetNational83901,
       "dot3ChipSetNational83902": dot3ChipSetNational83902,
       "dot3ChipSetNational83905": dot3ChipSetNational83905,
       "dot3ChipSetNational83907": dot3ChipSetNational83907,
       "dot3ChipSetNational83916": dot3ChipSetNational83916,
       "dot3ChipSetNational83934": dot3ChipSetNational83934,
       "dot3ChipSetNational83936": dot3ChipSetNational83936,
       "dot3ChipSetFujitsu": dot3ChipSetFujitsu,
       "dot3ChipSetFujitsu86950": dot3ChipSetFujitsu86950,
       "dot3ChipSetFujitsu86960": dot3ChipSetFujitsu86960,
       "dot3ChipSetFujitsu86964": dot3ChipSetFujitsu86964,
       "dot3ChipSetFujitsu86965A": dot3ChipSetFujitsu86965A,
       "dot3ChipSetFujitsu86965B": dot3ChipSetFujitsu86965B,
       "dot3ChipSetDigital": dot3ChipSetDigital,
       "dot3ChipSetDigitalDC21040": dot3ChipSetDigitalDC21040,
       "dot3ChipSetDigital21041": dot3ChipSetDigital21041,
       "dot3ChipSetDigital21140": dot3ChipSetDigital21140,
       "dot3ChipSetDigital21143": dot3ChipSetDigital21143,
       "dot3ChipSetDigital21340": dot3ChipSetDigital21340,
       "dot3ChipSetDigital21440": dot3ChipSetDigital21440,
       "dot3ChipSetDigital21540": dot3ChipSetDigital21540,
       "dot3ChipSetTI": dot3ChipSetTI,
       "dot3ChipSetTIE100": dot3ChipSetTIE100,
       "dot3ChipSetTIE110": dot3ChipSetTIE110,
       "dot3ChipSetTIX3100": dot3ChipSetTIX3100,
       "dot3ChipSetTIX3150": dot3ChipSetTIX3150,
       "dot3ChipSetTIX3270": dot3ChipSetTIX3270,
       "dot3ChipSetToshiba": dot3ChipSetToshiba,
       "dot3ChipSetToshibaTC35815F": dot3ChipSetToshibaTC35815F,
       "dot3ChipSetLucent": dot3ChipSetLucent,
       "dot3ChipSetLucentATT1MX10": dot3ChipSetLucentATT1MX10,
       "dot3ChipSetLucentLUC3M08": dot3ChipSetLucentLUC3M08,
       "dot3ChipSetGalileo": dot3ChipSetGalileo,
       "dot3ChipSetGalileoGT48001": dot3ChipSetGalileoGT48001,
       "dot3ChipSetGalileoGT48002": dot3ChipSetGalileoGT48002,
       "dot3ChipSetGalileoGT48004": dot3ChipSetGalileoGT48004,
       "dot3ChipSetGalileoGT48207": dot3ChipSetGalileoGT48207,
       "dot3ChipSetGalileoGT48208": dot3ChipSetGalileoGT48208,
       "dot3ChipSetGalileoGT48212": dot3ChipSetGalileoGT48212,
       "dot3ChipSetJato": dot3ChipSetJato,
       "dot3ChipSetJatoJT1001": dot3ChipSetJatoJT1001,
       "dot3ChipSetXaQti": dot3ChipSetXaQti,
       "dot3ChipSetXaQtiXQ11800FP": dot3ChipSetXaQtiXQ11800FP,
       "dot3ChipSetXaQtiXQ18110FP": dot3ChipSetXaQtiXQ18110FP,
       "etherChipsetMIB": etherChipsetMIB}
)
