# SNMP MIB module (BELAIR-MOBILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_15768/BELAIR-MOBILITY.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:08:43 2025
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

(BelAirMeshPointTopology,
 BelAirMeshPointType) = mibBuilder.importSymbols(
    "BELAIR-MESH",
    "BelAirMeshPointTopology",
    "BelAirMeshPointType")

(belairApplications,) = mibBuilder.importSymbols(
    "BELAIR-SMI",
    "belairApplications")

(BelAirAdminState,
 BelAirRowStatus) = mibBuilder.importSymbols(
    "BELAIR-TC",
    "BelAirAdminState",
    "BelAirRowStatus")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

belairMobilityMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6)
)
if mibBuilder.loadTexts:
    belairMobilityMib.setRevisions(
        ("2008-11-14 17:30",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class BelAirChannelList(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )



# MIB Managed Objects in the order of their OIDs

_BelairMobilityObjects_ObjectIdentity = ObjectIdentity
belairMobilityObjects = _BelairMobilityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 1)
)
_MobilitySystemTable_Object = MibTable
mobilitySystemTable = _MobilitySystemTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 1, 1)
)
if mibBuilder.loadTexts:
    mobilitySystemTable.setStatus("current")
_MobilitySystemEntry_Object = MibTableRow
mobilitySystemEntry = _MobilitySystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 1, 1, 1)
)
mobilitySystemEntry.setIndexNames(
    (0, "BELAIR-MOBILITY", "mobilitySystemNumber"),
)
if mibBuilder.loadTexts:
    mobilitySystemEntry.setStatus("current")


class _MobilitySystemNumber_Type(Integer32):
    """Custom type mobilitySystemNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MobilitySystemNumber_Type.__name__ = "Integer32"
_MobilitySystemNumber_Object = MibTableColumn
mobilitySystemNumber = _MobilitySystemNumber_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 1, 1, 1, 1),
    _MobilitySystemNumber_Type()
)
mobilitySystemNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mobilitySystemNumber.setStatus("current")
_MobilitySystemAdminState_Type = BelAirAdminState
_MobilitySystemAdminState_Object = MibTableColumn
mobilitySystemAdminState = _MobilitySystemAdminState_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 1, 1, 1, 2),
    _MobilitySystemAdminState_Type()
)
mobilitySystemAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobilitySystemAdminState.setStatus("current")
_MobilitySystemTopology_Type = BelAirMeshPointTopology
_MobilitySystemTopology_Object = MibTableColumn
mobilitySystemTopology = _MobilitySystemTopology_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 1, 1, 1, 3),
    _MobilitySystemTopology_Type()
)
mobilitySystemTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobilitySystemTopology.setStatus("current")
_MobilitySystemRole_Type = BelAirMeshPointType
_MobilitySystemRole_Object = MibTableColumn
mobilitySystemRole = _MobilitySystemRole_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 1, 1, 1, 4),
    _MobilitySystemRole_Type()
)
mobilitySystemRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobilitySystemRole.setStatus("current")


class _MobilitySystemNetworkId_Type(OctetString):
    """Custom type mobilitySystemNetworkId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_MobilitySystemNetworkId_Type.__name__ = "OctetString"
_MobilitySystemNetworkId_Object = MibTableColumn
mobilitySystemNetworkId = _MobilitySystemNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 1, 1, 1, 5),
    _MobilitySystemNetworkId_Type()
)
mobilitySystemNetworkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobilitySystemNetworkId.setStatus("current")
_MobilitySystemR7Compatible_Type = TruthValue
_MobilitySystemR7Compatible_Object = MibTableColumn
mobilitySystemR7Compatible = _MobilitySystemR7Compatible_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 1, 1, 1, 6),
    _MobilitySystemR7Compatible_Type()
)
mobilitySystemR7Compatible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobilitySystemR7Compatible.setStatus("current")
_MobilitySystemHomeCheck_Type = BelAirAdminState
_MobilitySystemHomeCheck_Object = MibTableColumn
mobilitySystemHomeCheck = _MobilitySystemHomeCheck_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 1, 1, 1, 7),
    _MobilitySystemHomeCheck_Type()
)
mobilitySystemHomeCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobilitySystemHomeCheck.setStatus("current")


class _MobilitySystemLinkId_Type(OctetString):
    """Custom type mobilitySystemLinkId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_MobilitySystemLinkId_Type.__name__ = "OctetString"
_MobilitySystemLinkId_Object = MibTableColumn
mobilitySystemLinkId = _MobilitySystemLinkId_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 1, 1, 1, 8),
    _MobilitySystemLinkId_Type()
)
mobilitySystemLinkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobilitySystemLinkId.setStatus("current")


class _MobilitySystemMinRssi_Type(Integer32):
    """Custom type mobilitySystemMinRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )


_MobilitySystemMinRssi_Type.__name__ = "Integer32"
_MobilitySystemMinRssi_Object = MibTableColumn
mobilitySystemMinRssi = _MobilitySystemMinRssi_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 1, 1, 1, 9),
    _MobilitySystemMinRssi_Type()
)
mobilitySystemMinRssi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobilitySystemMinRssi.setStatus("current")


class _MobilitySystemMarginRssi_Type(Integer32):
    """Custom type mobilitySystemMarginRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_MobilitySystemMarginRssi_Type.__name__ = "Integer32"
_MobilitySystemMarginRssi_Object = MibTableColumn
mobilitySystemMarginRssi = _MobilitySystemMarginRssi_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 1, 1, 1, 10),
    _MobilitySystemMarginRssi_Type()
)
mobilitySystemMarginRssi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobilitySystemMarginRssi.setStatus("current")


class _MobilitySystemSwitchRssi_Type(Integer32):
    """Custom type mobilitySystemSwitchRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )


_MobilitySystemSwitchRssi_Type.__name__ = "Integer32"
_MobilitySystemSwitchRssi_Object = MibTableColumn
mobilitySystemSwitchRssi = _MobilitySystemSwitchRssi_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 1, 1, 1, 11),
    _MobilitySystemSwitchRssi_Type()
)
mobilitySystemSwitchRssi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobilitySystemSwitchRssi.setStatus("current")


class _MobilitySystemSecondaryRssi_Type(Integer32):
    """Custom type mobilitySystemSecondaryRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )


_MobilitySystemSecondaryRssi_Type.__name__ = "Integer32"
_MobilitySystemSecondaryRssi_Object = MibTableColumn
mobilitySystemSecondaryRssi = _MobilitySystemSecondaryRssi_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 1, 1, 1, 12),
    _MobilitySystemSecondaryRssi_Type()
)
mobilitySystemSecondaryRssi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobilitySystemSecondaryRssi.setStatus("current")
_MobilitySystemPrimaryLink_Type = InterfaceIndex
_MobilitySystemPrimaryLink_Object = MibTableColumn
mobilitySystemPrimaryLink = _MobilitySystemPrimaryLink_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 1, 1, 1, 13),
    _MobilitySystemPrimaryLink_Type()
)
mobilitySystemPrimaryLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilitySystemPrimaryLink.setStatus("current")
_MobilitySystemSecondaryLink_Type = InterfaceIndex
_MobilitySystemSecondaryLink_Object = MibTableColumn
mobilitySystemSecondaryLink = _MobilitySystemSecondaryLink_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 1, 1, 1, 14),
    _MobilitySystemSecondaryLink_Type()
)
mobilitySystemSecondaryLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilitySystemSecondaryLink.setStatus("current")
_ScanListTable_Object = MibTable
scanListTable = _ScanListTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 1, 2)
)
if mibBuilder.loadTexts:
    scanListTable.setStatus("current")
_ScanListEntry_Object = MibTableRow
scanListEntry = _ScanListEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 1, 2, 1)
)
scanListEntry.setIndexNames(
    (0, "BELAIR-MOBILITY", "scanListNumber"),
)
if mibBuilder.loadTexts:
    scanListEntry.setStatus("current")


class _ScanListNumber_Type(Integer32):
    """Custom type scanListNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ScanListNumber_Type.__name__ = "Integer32"
_ScanListNumber_Object = MibTableColumn
scanListNumber = _ScanListNumber_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 1, 2, 1, 1),
    _ScanListNumber_Type()
)
scanListNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scanListNumber.setStatus("current")
_ScanListRowStatus_Type = BelAirRowStatus
_ScanListRowStatus_Object = MibTableColumn
scanListRowStatus = _ScanListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 1, 2, 1, 2),
    _ScanListRowStatus_Type()
)
scanListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scanListRowStatus.setStatus("current")
_ScanListChnlList_Type = BelAirChannelList
_ScanListChnlList_Object = MibTableColumn
scanListChnlList = _ScanListChnlList_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 1, 2, 1, 3),
    _ScanListChnlList_Type()
)
scanListChnlList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scanListChnlList.setStatus("current")
_BelairMobilityTraps_ObjectIdentity = ObjectIdentity
belairMobilityTraps = _BelairMobilityTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 2)
)
if mibBuilder.loadTexts:
    belairMobilityTraps.setStatus("current")
_BelairMobilityTrapsV2_ObjectIdentity = ObjectIdentity
belairMobilityTrapsV2 = _BelairMobilityTrapsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 2, 0)
)
if mibBuilder.loadTexts:
    belairMobilityTrapsV2.setStatus("current")
_BelairMobilityConformance_ObjectIdentity = ObjectIdentity
belairMobilityConformance = _BelairMobilityConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 4)
)

# Managed Objects groups

belairMobilityObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 4, 1)
)
belairMobilityObjectsGroup.setObjects(
      *(("BELAIR-MOBILITY", "mobilitySystemAdminState"),
        ("BELAIR-MOBILITY", "mobilitySystemSwitchRssi"),
        ("BELAIR-MOBILITY", "mobilitySystemMinRssi"),
        ("BELAIR-MOBILITY", "mobilitySystemHomeCheck"),
        ("BELAIR-MOBILITY", "mobilitySystemR7Compatible"),
        ("BELAIR-MOBILITY", "scanListChnlList"),
        ("BELAIR-MOBILITY", "scanListRowStatus"),
        ("BELAIR-MOBILITY", "scanListNumber"),
        ("BELAIR-MOBILITY", "mobilitySystemSecondaryLink"),
        ("BELAIR-MOBILITY", "mobilitySystemPrimaryLink"),
        ("BELAIR-MOBILITY", "mobilitySystemRole"),
        ("BELAIR-MOBILITY", "mobilitySystemTopology"),
        ("BELAIR-MOBILITY", "mobilitySystemNetworkId"),
        ("BELAIR-MOBILITY", "mobilitySystemLinkId"),
        ("BELAIR-MOBILITY", "mobilitySystemMarginRssi"),
        ("BELAIR-MOBILITY", "mobilitySystemSecondaryRssi"))
)
if mibBuilder.loadTexts:
    belairMobilityObjectsGroup.setStatus("current")


# Notification objects

noPrimaryLinkAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 2, 0, 1)
)
if mibBuilder.loadTexts:
    noPrimaryLinkAvailable.setStatus(
        "current"
    )

noSecondaryLinkAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 2, 0, 2)
)
if mibBuilder.loadTexts:
    noSecondaryLinkAvailable.setStatus(
        "current"
    )

primarySecondarySwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 2, 0, 3)
)
primarySecondarySwitchover.setObjects(
      *(("BELAIR-MOBILITY", "mobilitySystemPrimaryLink"),
        ("BELAIR-MOBILITY", "mobilitySystemSecondaryLink"))
)
if mibBuilder.loadTexts:
    primarySecondarySwitchover.setStatus(
        "current"
    )


# Notifications groups

belairMobilityTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 15768, 6, 6, 4, 2)
)
belairMobilityTrapsGroup.setObjects(
      *(("BELAIR-MOBILITY", "noPrimaryLinkAvailable"),
        ("BELAIR-MOBILITY", "noSecondaryLinkAvailable"),
        ("BELAIR-MOBILITY", "primarySecondarySwitchover"))
)
if mibBuilder.loadTexts:
    belairMobilityTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BELAIR-MOBILITY",
    **{"BelAirChannelList": BelAirChannelList,
       "belairMobilityMib": belairMobilityMib,
       "belairMobilityObjects": belairMobilityObjects,
       "mobilitySystemTable": mobilitySystemTable,
       "mobilitySystemEntry": mobilitySystemEntry,
       "mobilitySystemNumber": mobilitySystemNumber,
       "mobilitySystemAdminState": mobilitySystemAdminState,
       "mobilitySystemTopology": mobilitySystemTopology,
       "mobilitySystemRole": mobilitySystemRole,
       "mobilitySystemNetworkId": mobilitySystemNetworkId,
       "mobilitySystemR7Compatible": mobilitySystemR7Compatible,
       "mobilitySystemHomeCheck": mobilitySystemHomeCheck,
       "mobilitySystemLinkId": mobilitySystemLinkId,
       "mobilitySystemMinRssi": mobilitySystemMinRssi,
       "mobilitySystemMarginRssi": mobilitySystemMarginRssi,
       "mobilitySystemSwitchRssi": mobilitySystemSwitchRssi,
       "mobilitySystemSecondaryRssi": mobilitySystemSecondaryRssi,
       "mobilitySystemPrimaryLink": mobilitySystemPrimaryLink,
       "mobilitySystemSecondaryLink": mobilitySystemSecondaryLink,
       "scanListTable": scanListTable,
       "scanListEntry": scanListEntry,
       "scanListNumber": scanListNumber,
       "scanListRowStatus": scanListRowStatus,
       "scanListChnlList": scanListChnlList,
       "belairMobilityTraps": belairMobilityTraps,
       "belairMobilityTrapsV2": belairMobilityTrapsV2,
       "noPrimaryLinkAvailable": noPrimaryLinkAvailable,
       "noSecondaryLinkAvailable": noSecondaryLinkAvailable,
       "primarySecondarySwitchover": primarySecondarySwitchover,
       "belairMobilityConformance": belairMobilityConformance,
       "belairMobilityObjectsGroup": belairMobilityObjectsGroup,
       "belairMobilityTrapsGroup": belairMobilityTrapsGroup}
)
