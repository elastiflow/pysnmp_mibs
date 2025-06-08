# SNMP MIB module (TIMETRA-SAS-MIRROR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-SAS-MIRROR-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:37:16 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(TEntryId,
 TEntryIdOrZero,
 TFilterID,
 TFilterType,
 TIPFilterID,
 TMACFilterID) = mibBuilder.importSymbols(
    "TIMETRA-FILTER-MIB",
    "TEntryId",
    "TEntryIdOrZero",
    "TFilterID",
    "TFilterType",
    "TIPFilterID",
    "TMACFilterID")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(tMirrorDestinationEntry,
 tMirrorSourcePortEntry) = mibBuilder.importSymbols(
    "TIMETRA-MIRROR-MIB",
    "tMirrorDestinationEntry",
    "tMirrorSourcePortEntry")

(timetraSASConfs,
 timetraSASModules,
 timetraSASNotifyPrefix,
 timetraSASObjs) = mibBuilder.importSymbols(
    "TIMETRA-SAS-GLOBAL-MIB",
    "timetraSASConfs",
    "timetraSASModules",
    "timetraSASNotifyPrefix",
    "timetraSASObjs")

(SdpId,) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "SdpId")

(SdpBindId,
 ServiceAdminStatus,
 ServiceOperStatus,
 TFCName,
 TFCSet,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TPolicyID,
 TProfileOrNone,
 TmnxEncapVal,
 TmnxPortID,
 TmnxServId) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "SdpBindId",
    "ServiceAdminStatus",
    "ServiceOperStatus",
    "TFCName",
    "TFCSet",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPolicyID",
    "TProfileOrNone",
    "TmnxEncapVal",
    "TmnxPortID",
    "TmnxServId")


# MODULE-IDENTITY

timetraSASMirrorMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 13)
)
if mibBuilder.loadTexts:
    timetraSASMirrorMIBModule.setRevisions(
        ("1911-05-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxSASMirrorGroups_ObjectIdentity = ObjectIdentity
tmnxSASMirrorGroups = _TmnxSASMirrorGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 8)
)
_TSASMirrorObjects_ObjectIdentity = ObjectIdentity
tSASMirrorObjects = _TSASMirrorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 13)
)
_TMirrorSourcePortExtnTable_Object = MibTable
tMirrorSourcePortExtnTable = _TMirrorSourcePortExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 13, 1)
)
if mibBuilder.loadTexts:
    tMirrorSourcePortExtnTable.setStatus("current")
_TMirrorSourcePortExtnEntry_Object = MibTableRow
tMirrorSourcePortExtnEntry = _TMirrorSourcePortExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 13, 1, 1)
)
if mibBuilder.loadTexts:
    tMirrorSourcePortExtnEntry.setStatus("current")


class _TMirrorSourcePortEgressMirroringType_Type(Integer32):
    """Custom type tMirrorSourcePortEgressMirroringType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true-egress-mirroring", 1),
          ("normal-egress-mirroring", 2))
    )


_TMirrorSourcePortEgressMirroringType_Type.__name__ = "Integer32"
_TMirrorSourcePortEgressMirroringType_Object = MibTableColumn
tMirrorSourcePortEgressMirroringType = _TMirrorSourcePortEgressMirroringType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 13, 1, 1, 1),
    _TMirrorSourcePortEgressMirroringType_Type()
)
tMirrorSourcePortEgressMirroringType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourcePortEgressMirroringType.setStatus("current")
_TMirrorDestinationExtnTable_Object = MibTable
tMirrorDestinationExtnTable = _TMirrorDestinationExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 13, 2)
)
if mibBuilder.loadTexts:
    tMirrorDestinationExtnTable.setStatus("current")
_TMirrorDestinationExtnEntry_Object = MibTableRow
tMirrorDestinationExtnEntry = _TMirrorDestinationExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 13, 2, 1)
)
if mibBuilder.loadTexts:
    tMirrorDestinationExtnEntry.setStatus("current")


class _TMirrorDestinationFCProfile_Type(TProfileOrNone):
    """Custom type tMirrorDestinationFCProfile based on TProfileOrNone"""
    defaultValue = 2


_TMirrorDestinationFCProfile_Type.__name__ = "TProfileOrNone"
_TMirrorDestinationFCProfile_Object = MibTableColumn
tMirrorDestinationFCProfile = _TMirrorDestinationFCProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 13, 2, 1, 1),
    _TMirrorDestinationFCProfile_Type()
)
tMirrorDestinationFCProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestinationFCProfile.setStatus("current")


class _TMirrorDestinationMirrorSourceType_Type(Integer32):
    """Custom type tMirrorDestinationMirrorSourceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2),
          ("both", 3))
    )


_TMirrorDestinationMirrorSourceType_Type.__name__ = "Integer32"
_TMirrorDestinationMirrorSourceType_Object = MibTableColumn
tMirrorDestinationMirrorSourceType = _TMirrorDestinationMirrorSourceType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 13, 2, 1, 2),
    _TMirrorDestinationMirrorSourceType_Type()
)
tMirrorDestinationMirrorSourceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestinationMirrorSourceType.setStatus("current")
tMirrorSourcePortEntry.registerAugmentions(
    ("TIMETRA-SAS-MIRROR-MIB",
     "tMirrorSourcePortExtnEntry")
)
tMirrorSourcePortExtnEntry.setIndexNames(*tMirrorSourcePortEntry.getIndexNames())
tMirrorDestinationEntry.registerAugmentions(
    ("TIMETRA-SAS-MIRROR-MIB",
     "tMirrorDestinationExtnEntry")
)
tMirrorDestinationExtnEntry.setIndexNames(*tMirrorDestinationEntry.getIndexNames())

# Managed Objects groups

tmnxSASMirrorV1v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 8, 1)
)
tmnxSASMirrorV1v0Group.setObjects(
      *(("TIMETRA-SAS-MIRROR-MIB", "tMirrorSourcePortEgressMirroringType"),
        ("TIMETRA-SAS-MIRROR-MIB", "tMirrorDestinationFCProfile"),
        ("TIMETRA-SAS-MIRROR-MIB", "tMirrorDestinationMirrorSourceType"))
)
if mibBuilder.loadTexts:
    tmnxSASMirrorV1v0Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SAS-MIRROR-MIB",
    **{"timetraSASMirrorMIBModule": timetraSASMirrorMIBModule,
       "tmnxSASMirrorGroups": tmnxSASMirrorGroups,
       "tmnxSASMirrorV1v0Group": tmnxSASMirrorV1v0Group,
       "tSASMirrorObjects": tSASMirrorObjects,
       "tMirrorSourcePortExtnTable": tMirrorSourcePortExtnTable,
       "tMirrorSourcePortExtnEntry": tMirrorSourcePortExtnEntry,
       "tMirrorSourcePortEgressMirroringType": tMirrorSourcePortEgressMirroringType,
       "tMirrorDestinationExtnTable": tMirrorDestinationExtnTable,
       "tMirrorDestinationExtnEntry": tMirrorDestinationExtnEntry,
       "tMirrorDestinationFCProfile": tMirrorDestinationFCProfile,
       "tMirrorDestinationMirrorSourceType": tMirrorDestinationMirrorSourceType}
)
