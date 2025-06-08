# SNMP MIB module (CGX-MODELS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cloudgenix_50114/CGX-MODELS-MIB.mib
# Produced by pysmi-1.6.1 at Wed Jun  4 13:56:22 2025
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

(cgxProducts,) = mibBuilder.importSymbols(
    "CLOUDGENIX-SMI",
    "cgxProducts")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

cgxModelsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1)
)
if mibBuilder.loadTexts:
    cgxModelsMIB.setRevisions(
        ("2023-05-11 21:44",
         "2023-02-24 21:27",
         "2022-02-24 19:35")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CgxModelsNotifications_ObjectIdentity = ObjectIdentity
cgxModelsNotifications = _CgxModelsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 0)
)
_CgxModelsObjects_ObjectIdentity = ObjectIdentity
cgxModelsObjects = _CgxModelsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 1)
)
_CgxModelsStats_ObjectIdentity = ObjectIdentity
cgxModelsStats = _CgxModelsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 1, 1)
)
_CgxModelsConfig_ObjectIdentity = ObjectIdentity
cgxModelsConfig = _CgxModelsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 1, 2)
)
_CgxModelsConformance_ObjectIdentity = ObjectIdentity
cgxModelsConformance = _CgxModelsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 2)
)
_CgxModelsCompliances_ObjectIdentity = ObjectIdentity
cgxModelsCompliances = _CgxModelsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 2, 1)
)
_CgxModelsGroups_ObjectIdentity = ObjectIdentity
cgxModelsGroups = _CgxModelsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 2, 2)
)
_CgxModelsHardwareV1_ObjectIdentity = ObjectIdentity
cgxModelsHardwareV1 = _CgxModelsHardwareV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 10)
)
if mibBuilder.loadTexts:
    cgxModelsHardwareV1.setStatus("current")
_Ion1000_ObjectIdentity = ObjectIdentity
ion1000 = _Ion1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 10, 1000)
)
if mibBuilder.loadTexts:
    ion1000.setStatus("current")
_Ion1200_ObjectIdentity = ObjectIdentity
ion1200 = _Ion1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 10, 1200)
)
if mibBuilder.loadTexts:
    ion1200.setStatus("current")
_Ion1200CNA_ObjectIdentity = ObjectIdentity
ion1200CNA = _Ion1200CNA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 10, 1201)
)
if mibBuilder.loadTexts:
    ion1200CNA.setStatus("current")
_Ion1200CROW_ObjectIdentity = ObjectIdentity
ion1200CROW = _Ion1200CROW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 10, 1202)
)
if mibBuilder.loadTexts:
    ion1200CROW.setStatus("current")
_Ion1200C5GWW_ObjectIdentity = ObjectIdentity
ion1200C5GWW = _Ion1200C5GWW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 10, 1203)
)
if mibBuilder.loadTexts:
    ion1200C5GWW.setStatus("current")
_Ion1200C5GEXP_ObjectIdentity = ObjectIdentity
ion1200C5GEXP = _Ion1200C5GEXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 10, 1204)
)
if mibBuilder.loadTexts:
    ion1200C5GEXP.setStatus("current")
_Ion1200S_ObjectIdentity = ObjectIdentity
ion1200S = _Ion1200S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 10, 1210)
)
if mibBuilder.loadTexts:
    ion1200S.setStatus("current")
_Ion1200SCNA_ObjectIdentity = ObjectIdentity
ion1200SCNA = _Ion1200SCNA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 10, 1211)
)
if mibBuilder.loadTexts:
    ion1200SCNA.setStatus("current")
_Ion1200SCROW_ObjectIdentity = ObjectIdentity
ion1200SCROW = _Ion1200SCROW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 10, 1212)
)
if mibBuilder.loadTexts:
    ion1200SCROW.setStatus("current")
_Ion1200SC5GWW_ObjectIdentity = ObjectIdentity
ion1200SC5GWW = _Ion1200SC5GWW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 10, 1213)
)
if mibBuilder.loadTexts:
    ion1200SC5GWW.setStatus("current")
_Ion2000_ObjectIdentity = ObjectIdentity
ion2000 = _Ion2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 10, 2000)
)
if mibBuilder.loadTexts:
    ion2000.setStatus("current")
_Ion3000_ObjectIdentity = ObjectIdentity
ion3000 = _Ion3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 10, 3000)
)
if mibBuilder.loadTexts:
    ion3000.setStatus("current")
_Ion3200_ObjectIdentity = ObjectIdentity
ion3200 = _Ion3200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 10, 3200)
)
if mibBuilder.loadTexts:
    ion3200.setStatus("current")
_Ion5200_ObjectIdentity = ObjectIdentity
ion5200 = _Ion5200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 10, 5200)
)
if mibBuilder.loadTexts:
    ion5200.setStatus("current")
_Ion7000_ObjectIdentity = ObjectIdentity
ion7000 = _Ion7000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 10, 7000)
)
if mibBuilder.loadTexts:
    ion7000.setStatus("current")
_Ion9000_ObjectIdentity = ObjectIdentity
ion9000 = _Ion9000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 10, 9000)
)
if mibBuilder.loadTexts:
    ion9000.setStatus("current")
_Ion9200_ObjectIdentity = ObjectIdentity
ion9200 = _Ion9200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 10, 9200)
)
if mibBuilder.loadTexts:
    ion9200.setStatus("current")
_CgxModelsVirtualV1_ObjectIdentity = ObjectIdentity
cgxModelsVirtualV1 = _CgxModelsVirtualV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 11)
)
if mibBuilder.loadTexts:
    cgxModelsVirtualV1.setStatus("current")
_Ion3102v_ObjectIdentity = ObjectIdentity
ion3102v = _Ion3102v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 11, 3102)
)
if mibBuilder.loadTexts:
    ion3102v.setStatus("current")
_Ion3104v_ObjectIdentity = ObjectIdentity
ion3104v = _Ion3104v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 11, 3104)
)
if mibBuilder.loadTexts:
    ion3104v.setStatus("current")
_Ion3108v_ObjectIdentity = ObjectIdentity
ion3108v = _Ion3108v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 11, 3108)
)
if mibBuilder.loadTexts:
    ion3108v.setStatus("current")
_Ion7108v_ObjectIdentity = ObjectIdentity
ion7108v = _Ion7108v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 11, 7108)
)
if mibBuilder.loadTexts:
    ion7108v.setStatus("current")
_Ion7116v_ObjectIdentity = ObjectIdentity
ion7116v = _Ion7116v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 11, 7116)
)
if mibBuilder.loadTexts:
    ion7116v.setStatus("current")
_Ion7132v_ObjectIdentity = ObjectIdentity
ion7132v = _Ion7132v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11, 1, 11, 7132)
)
if mibBuilder.loadTexts:
    ion7132v.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CGX-MODELS-MIB",
    **{"cgxModelsMIB": cgxModelsMIB,
       "cgxModelsNotifications": cgxModelsNotifications,
       "cgxModelsObjects": cgxModelsObjects,
       "cgxModelsStats": cgxModelsStats,
       "cgxModelsConfig": cgxModelsConfig,
       "cgxModelsConformance": cgxModelsConformance,
       "cgxModelsCompliances": cgxModelsCompliances,
       "cgxModelsGroups": cgxModelsGroups,
       "cgxModelsHardwareV1": cgxModelsHardwareV1,
       "ion1000": ion1000,
       "ion1200": ion1200,
       "ion1200CNA": ion1200CNA,
       "ion1200CROW": ion1200CROW,
       "ion1200C5GWW": ion1200C5GWW,
       "ion1200C5GEXP": ion1200C5GEXP,
       "ion1200S": ion1200S,
       "ion1200SCNA": ion1200SCNA,
       "ion1200SCROW": ion1200SCROW,
       "ion1200SC5GWW": ion1200SC5GWW,
       "ion2000": ion2000,
       "ion3000": ion3000,
       "ion3200": ion3200,
       "ion5200": ion5200,
       "ion7000": ion7000,
       "ion9000": ion9000,
       "ion9200": ion9200,
       "cgxModelsVirtualV1": cgxModelsVirtualV1,
       "ion3102v": ion3102v,
       "ion3104v": ion3104v,
       "ion3108v": ion3108v,
       "ion7108v": ion7108v,
       "ion7116v": ion7116v,
       "ion7132v": ion7132v}
)
