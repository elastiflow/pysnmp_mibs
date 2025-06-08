# SNMP MIB module (TIMETRA-SAS-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-SAS-BGP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:37:23 2025
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

(bgp4PathAttrEntry,) = mibBuilder.importSymbols(
    "BGP4-MIB",
    "bgp4PathAttrEntry")

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
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")

(tBgpPeerNgParamsEntry,) = mibBuilder.importSymbols(
    "TIMETRA-BGP-MIB",
    "tBgpPeerNgParamsEntry")

(timetraSASConfs,
 timetraSASModules,
 timetraSASNotifyPrefix,
 timetraSASObjs) = mibBuilder.importSymbols(
    "TIMETRA-SAS-GLOBAL-MIB",
    "timetraSASConfs",
    "timetraSASModules",
    "timetraSASNotifyPrefix",
    "timetraSASObjs")


# MODULE-IDENTITY

timetraSASBgpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 15)
)
if mibBuilder.loadTexts:
    timetraSASBgpMIBModule.setRevisions(
        ("1913-11-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxSASBgpConformance_ObjectIdentity = ObjectIdentity
tmnxSASBgpConformance = _TmnxSASBgpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 14)
)
_TmnxSASBgpGroups_ObjectIdentity = ObjectIdentity
tmnxSASBgpGroups = _TmnxSASBgpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 14, 1)
)
_TmnxSASBgpObjects_ObjectIdentity = ObjectIdentity
tmnxSASBgpObjects = _TmnxSASBgpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 18)
)
_TBgpSASPeerObjects_ObjectIdentity = ObjectIdentity
tBgpSASPeerObjects = _TBgpSASPeerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 18, 1)
)
_TBgpPeerNgParamsExtnTable_Object = MibTable
tBgpPeerNgParamsExtnTable = _TBgpPeerNgParamsExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 18, 1, 10)
)
if mibBuilder.loadTexts:
    tBgpPeerNgParamsExtnTable.setStatus("current")
_TBgpPeerNgParamsExtnEntry_Object = MibTableRow
tBgpPeerNgParamsExtnEntry = _TBgpPeerNgParamsExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 18, 1, 10, 1)
)
if mibBuilder.loadTexts:
    tBgpPeerNgParamsExtnEntry.setStatus("current")


class _TBgpPeerNgUseSvcRoutes_Type(TruthValue):
    """Custom type tBgpPeerNgUseSvcRoutes based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgUseSvcRoutes_Type.__name__ = "TruthValue"
_TBgpPeerNgUseSvcRoutes_Object = MibTableColumn
tBgpPeerNgUseSvcRoutes = _TBgpPeerNgUseSvcRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 18, 1, 10, 1, 1),
    _TBgpPeerNgUseSvcRoutes_Type()
)
tBgpPeerNgUseSvcRoutes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgUseSvcRoutes.setStatus("current")
_Bgp4PathAttrExtnTable_Object = MibTable
bgp4PathAttrExtnTable = _Bgp4PathAttrExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 18, 1, 11)
)
if mibBuilder.loadTexts:
    bgp4PathAttrExtnTable.setStatus("current")
_Bgp4PathAttrExtnEntry_Object = MibTableRow
bgp4PathAttrExtnEntry = _Bgp4PathAttrExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 18, 1, 11, 1)
)
if mibBuilder.loadTexts:
    bgp4PathAttrExtnEntry.setStatus("current")
_Bgp4PathUseSvcRoutesOpt_Type = TruthValue
_Bgp4PathUseSvcRoutesOpt_Object = MibTableColumn
bgp4PathUseSvcRoutesOpt = _Bgp4PathUseSvcRoutesOpt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 18, 1, 11, 1, 1),
    _Bgp4PathUseSvcRoutesOpt_Type()
)
bgp4PathUseSvcRoutesOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4PathUseSvcRoutesOpt.setStatus("current")
tBgpPeerNgParamsEntry.registerAugmentions(
    ("TIMETRA-SAS-BGP-MIB",
     "tBgpPeerNgParamsExtnEntry")
)
tBgpPeerNgParamsExtnEntry.setIndexNames(*tBgpPeerNgParamsEntry.getIndexNames())
bgp4PathAttrEntry.registerAugmentions(
    ("TIMETRA-SAS-BGP-MIB",
     "bgp4PathAttrExtnEntry")
)
bgp4PathAttrExtnEntry.setIndexNames(*bgp4PathAttrEntry.getIndexNames())

# Managed Objects groups

tmnxSASBgpGlobalV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 14, 1, 1)
)
tmnxSASBgpGlobalV7v0Group.setObjects(
    ("TIMETRA-SAS-BGP-MIB", "tBgpPeerNgUseSvcRoutes")
)
if mibBuilder.loadTexts:
    tmnxSASBgpGlobalV7v0Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SAS-BGP-MIB",
    **{"timetraSASBgpMIBModule": timetraSASBgpMIBModule,
       "tmnxSASBgpConformance": tmnxSASBgpConformance,
       "tmnxSASBgpGroups": tmnxSASBgpGroups,
       "tmnxSASBgpGlobalV7v0Group": tmnxSASBgpGlobalV7v0Group,
       "tmnxSASBgpObjects": tmnxSASBgpObjects,
       "tBgpSASPeerObjects": tBgpSASPeerObjects,
       "tBgpPeerNgParamsExtnTable": tBgpPeerNgParamsExtnTable,
       "tBgpPeerNgParamsExtnEntry": tBgpPeerNgParamsExtnEntry,
       "tBgpPeerNgUseSvcRoutes": tBgpPeerNgUseSvcRoutes,
       "bgp4PathAttrExtnTable": bgp4PathAttrExtnTable,
       "bgp4PathAttrExtnEntry": bgp4PathAttrExtnEntry,
       "bgp4PathUseSvcRoutesOpt": bgp4PathUseSvcRoutesOpt}
)
