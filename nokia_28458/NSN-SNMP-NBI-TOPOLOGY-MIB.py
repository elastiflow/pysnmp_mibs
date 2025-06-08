# SNMP MIB module (NSN-SNMP-NBI-TOPOLOGY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_28458/NSN-SNMP-NBI-TOPOLOGY-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:24:52 2025
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

(nbiEmsSynchronizationState,
 nbiEventTime,
 nbiNotSyncNEs,
 nbiObjectInstance,
 nbiSequenceId) = mibBuilder.importSymbols(
    "NSN-SNMP-NBI-COMMONFUNCTIONS-MIB",
    "nbiEmsSynchronizationState",
    "nbiEventTime",
    "nbiNotSyncNEs",
    "nbiObjectInstance",
    "nbiSequenceId")

(nbiNetActSnmp,) = mibBuilder.importSymbols(
    "NSN-SNMP-NBI-REGISTRATION-MIB",
    "nbiNetActSnmp")

(NbiActiveInterfaceVersion,
 NbiAdditionalInfo,
 NbiAdministrativeState,
 NbiChangedAttributeSet,
 NbiChangedStateSet,
 NbiCommunicationState,
 NbiEMSorNEVersion,
 NbiGetTopologyData,
 NbiLocation,
 NbiObjectInstance,
 NbiOperationalState,
 NbiProductType,
 NbiSimpleIdentifier,
 NbiUserLabel,
 NbiVendor) = mibBuilder.importSymbols(
    "NSN-SNMP-NBI-TEXTUALCONVENTIONS-MIB",
    "NbiActiveInterfaceVersion",
    "NbiAdditionalInfo",
    "NbiAdministrativeState",
    "NbiChangedAttributeSet",
    "NbiChangedStateSet",
    "NbiCommunicationState",
    "NbiEMSorNEVersion",
    "NbiGetTopologyData",
    "NbiLocation",
    "NbiObjectInstance",
    "NbiOperationalState",
    "NbiProductType",
    "NbiSimpleIdentifier",
    "NbiUserLabel",
    "NbiVendor")

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

nbiTopologyManagementMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4)
)
if mibBuilder.loadTexts:
    nbiTopologyManagementMIB.setRevisions(
        ("2011-01-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbiTopologyNotifications_ObjectIdentity = ObjectIdentity
nbiTopologyNotifications = _NbiTopologyNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 0)
)
_NbiTopologySpontaneousNotifications_ObjectIdentity = ObjectIdentity
nbiTopologySpontaneousNotifications = _NbiTopologySpontaneousNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 0, 1)
)
_NbiTopologySyncNotifications_ObjectIdentity = ObjectIdentity
nbiTopologySyncNotifications = _NbiTopologySyncNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 0, 2)
)
_NbiTopologyObjects_ObjectIdentity = ObjectIdentity
nbiTopologyObjects = _NbiTopologyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1)
)
_NbiTopologyParameterObjects_ObjectIdentity = ObjectIdentity
nbiTopologyParameterObjects = _NbiTopologyParameterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 1)
)
_NbiActiveNBIVersion_Type = NbiActiveInterfaceVersion
_NbiActiveNBIVersion_Object = MibScalar
nbiActiveNBIVersion = _NbiActiveNBIVersion_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 1, 1),
    _NbiActiveNBIVersion_Type()
)
nbiActiveNBIVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiActiveNBIVersion.setStatus("current")
_NbiAdditionalInfo_Type = NbiAdditionalInfo
_NbiAdditionalInfo_Object = MibScalar
nbiAdditionalInfo = _NbiAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 1, 2),
    _NbiAdditionalInfo_Type()
)
nbiAdditionalInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiAdditionalInfo.setStatus("current")


class _NbiAdministrativeState_Type(NbiAdministrativeState):
    """Custom type nbiAdministrativeState based on NbiAdministrativeState"""
    defaultValue = 2


_NbiAdministrativeState_Type.__name__ = "NbiAdministrativeState"
_NbiAdministrativeState_Object = MibScalar
nbiAdministrativeState = _NbiAdministrativeState_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 1, 3),
    _NbiAdministrativeState_Type()
)
nbiAdministrativeState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiAdministrativeState.setStatus("current")
_NbiChangedAttributeSet_Type = NbiChangedAttributeSet
_NbiChangedAttributeSet_Object = MibScalar
nbiChangedAttributeSet = _NbiChangedAttributeSet_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 1, 4),
    _NbiChangedAttributeSet_Type()
)
nbiChangedAttributeSet.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiChangedAttributeSet.setStatus("current")
_NbiChangedStateSet_Type = NbiChangedStateSet
_NbiChangedStateSet_Object = MibScalar
nbiChangedStateSet = _NbiChangedStateSet_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 1, 5),
    _NbiChangedStateSet_Type()
)
nbiChangedStateSet.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiChangedStateSet.setStatus("current")
_NbiCommunicationState_Type = NbiCommunicationState
_NbiCommunicationState_Object = MibScalar
nbiCommunicationState = _NbiCommunicationState_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 1, 6),
    _NbiCommunicationState_Type()
)
nbiCommunicationState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiCommunicationState.setStatus("current")
_NbiEMSName_Type = NbiUserLabel
_NbiEMSName_Object = MibScalar
nbiEMSName = _NbiEMSName_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 1, 7),
    _NbiEMSName_Type()
)
nbiEMSName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiEMSName.setStatus("current")


class _NbiLocation_Type(NbiLocation):
    """Custom type nbiLocation based on NbiLocation"""
    defaultValue = OctetString("")


_NbiLocation_Type.__name__ = "NbiLocation"
_NbiLocation_Object = MibScalar
nbiLocation = _NbiLocation_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 1, 8),
    _NbiLocation_Type()
)
nbiLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiLocation.setStatus("current")
_NbiNEName_Type = NbiUserLabel
_NbiNEName_Object = MibScalar
nbiNEName = _NbiNEName_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 1, 9),
    _NbiNEName_Type()
)
nbiNEName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiNEName.setStatus("current")


class _NbiOperationalState_Type(NbiOperationalState):
    """Custom type nbiOperationalState based on NbiOperationalState"""
    defaultValue = 2


_NbiOperationalState_Type.__name__ = "NbiOperationalState"
_NbiOperationalState_Object = MibScalar
nbiOperationalState = _NbiOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 1, 11),
    _NbiOperationalState_Type()
)
nbiOperationalState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiOperationalState.setStatus("current")
_NbiProductType_Type = NbiProductType
_NbiProductType_Object = MibScalar
nbiProductType = _NbiProductType_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 1, 12),
    _NbiProductType_Type()
)
nbiProductType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiProductType.setStatus("current")


class _NbiVendor_Type(NbiVendor):
    """Custom type nbiVendor based on NbiVendor"""
    defaultValue = OctetString("")


_NbiVendor_Type.__name__ = "NbiVendor"
_NbiVendor_Object = MibScalar
nbiVendor = _NbiVendor_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 1, 13),
    _NbiVendor_Type()
)
nbiVendor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiVendor.setStatus("current")


class _NbiVersion_Type(NbiEMSorNEVersion):
    """Custom type nbiVersion based on NbiEMSorNEVersion"""
    defaultValue = OctetString("")


_NbiVersion_Type.__name__ = "NbiEMSorNEVersion"
_NbiVersion_Object = MibScalar
nbiVersion = _NbiVersion_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 1, 14),
    _NbiVersion_Type()
)
nbiVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiVersion.setStatus("current")
_NbiTopologyRequestObjects_ObjectIdentity = ObjectIdentity
nbiTopologyRequestObjects = _NbiTopologyRequestObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 2)
)


class _NbiGetTopologyData_Type(NbiGetTopologyData):
    """Custom type nbiGetTopologyData based on NbiGetTopologyData"""
    defaultValue = OctetString("")


_NbiGetTopologyData_Type.__name__ = "NbiGetTopologyData"
_NbiGetTopologyData_Object = MibScalar
nbiGetTopologyData = _NbiGetTopologyData_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 2, 1),
    _NbiGetTopologyData_Type()
)
nbiGetTopologyData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbiGetTopologyData.setStatus("current")
_NbiNETopologyTable_Object = MibTable
nbiNETopologyTable = _NbiNETopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    nbiNETopologyTable.setStatus("current")
_NbiNETopologyEntry_Object = MibTableRow
nbiNETopologyEntry = _NbiNETopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 2, 2, 1)
)
nbiNETopologyEntry.setIndexNames(
    (0, "NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiNETableIndex"),
)
if mibBuilder.loadTexts:
    nbiNETopologyEntry.setStatus("current")
_NbiNETableIndex_Type = NbiSimpleIdentifier
_NbiNETableIndex_Object = MibTableColumn
nbiNETableIndex = _NbiNETableIndex_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 2, 2, 1, 1),
    _NbiNETableIndex_Type()
)
nbiNETableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbiNETableIndex.setStatus("current")
_NbiNETableObjectInstance_Type = NbiObjectInstance
_NbiNETableObjectInstance_Object = MibTableColumn
nbiNETableObjectInstance = _NbiNETableObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 2, 2, 1, 2),
    _NbiNETableObjectInstance_Type()
)
nbiNETableObjectInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiNETableObjectInstance.setStatus("current")
_NbiNETableNEName_Type = NbiUserLabel
_NbiNETableNEName_Object = MibTableColumn
nbiNETableNEName = _NbiNETableNEName_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 2, 2, 1, 3),
    _NbiNETableNEName_Type()
)
nbiNETableNEName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiNETableNEName.setStatus("current")


class _NbiNETableVendor_Type(NbiVendor):
    """Custom type nbiNETableVendor based on NbiVendor"""
    defaultValue = OctetString("")


_NbiNETableVendor_Type.__name__ = "NbiVendor"
_NbiNETableVendor_Object = MibTableColumn
nbiNETableVendor = _NbiNETableVendor_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 2, 2, 1, 4),
    _NbiNETableVendor_Type()
)
nbiNETableVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiNETableVendor.setStatus("current")
_NbiNETableProductType_Type = NbiProductType
_NbiNETableProductType_Object = MibTableColumn
nbiNETableProductType = _NbiNETableProductType_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 2, 2, 1, 5),
    _NbiNETableProductType_Type()
)
nbiNETableProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiNETableProductType.setStatus("current")


class _NbiNETableVersion_Type(NbiEMSorNEVersion):
    """Custom type nbiNETableVersion based on NbiEMSorNEVersion"""
    defaultValue = OctetString("")


_NbiNETableVersion_Type.__name__ = "NbiEMSorNEVersion"
_NbiNETableVersion_Object = MibTableColumn
nbiNETableVersion = _NbiNETableVersion_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 2, 2, 1, 6),
    _NbiNETableVersion_Type()
)
nbiNETableVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiNETableVersion.setStatus("current")


class _NbiNETableLocation_Type(NbiLocation):
    """Custom type nbiNETableLocation based on NbiLocation"""
    defaultValue = OctetString("")


_NbiNETableLocation_Type.__name__ = "NbiLocation"
_NbiNETableLocation_Object = MibTableColumn
nbiNETableLocation = _NbiNETableLocation_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 2, 2, 1, 7),
    _NbiNETableLocation_Type()
)
nbiNETableLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiNETableLocation.setStatus("current")


class _NbiNETableAdministrativeState_Type(NbiAdministrativeState):
    """Custom type nbiNETableAdministrativeState based on NbiAdministrativeState"""
    defaultValue = 2


_NbiNETableAdministrativeState_Type.__name__ = "NbiAdministrativeState"
_NbiNETableAdministrativeState_Object = MibTableColumn
nbiNETableAdministrativeState = _NbiNETableAdministrativeState_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 2, 2, 1, 8),
    _NbiNETableAdministrativeState_Type()
)
nbiNETableAdministrativeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiNETableAdministrativeState.setStatus("current")
_NbiNETableCommunicationState_Type = NbiCommunicationState
_NbiNETableCommunicationState_Object = MibTableColumn
nbiNETableCommunicationState = _NbiNETableCommunicationState_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 2, 2, 1, 9),
    _NbiNETableCommunicationState_Type()
)
nbiNETableCommunicationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiNETableCommunicationState.setStatus("current")


class _NbiNETableOperationalState_Type(NbiOperationalState):
    """Custom type nbiNETableOperationalState based on NbiOperationalState"""
    defaultValue = 2


_NbiNETableOperationalState_Type.__name__ = "NbiOperationalState"
_NbiNETableOperationalState_Object = MibTableColumn
nbiNETableOperationalState = _NbiNETableOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 2, 2, 1, 10),
    _NbiNETableOperationalState_Type()
)
nbiNETableOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiNETableOperationalState.setStatus("current")


class _NbiNETableAdditionalInfo_Type(NbiAdditionalInfo):
    """Custom type nbiNETableAdditionalInfo based on NbiAdditionalInfo"""
    defaultValue = OctetString("")


_NbiNETableAdditionalInfo_Type.__name__ = "NbiAdditionalInfo"
_NbiNETableAdditionalInfo_Object = MibTableColumn
nbiNETableAdditionalInfo = _NbiNETableAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 1, 2, 2, 1, 11),
    _NbiNETableAdditionalInfo_Type()
)
nbiNETableAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiNETableAdditionalInfo.setStatus("current")
_NbiTopologyConformance_ObjectIdentity = ObjectIdentity
nbiTopologyConformance = _NbiTopologyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 2)
)
_NbiTopologyCompliances_ObjectIdentity = ObjectIdentity
nbiTopologyCompliances = _NbiTopologyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 2, 1)
)
_NbiTopologyGroups_ObjectIdentity = ObjectIdentity
nbiTopologyGroups = _NbiTopologyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 2, 2)
)

# Managed Objects groups

nbiTopologyParameterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 2, 2, 1)
)
nbiTopologyParameterGroup.setObjects(
      *(("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiAdministrativeState"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiChangedAttributeSet"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiChangedStateSet"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiCommunicationState"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiOperationalState"))
)
if mibBuilder.loadTexts:
    nbiTopologyParameterGroup.setStatus("current")

nbiTopologySynchronizationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 2, 2, 2)
)
nbiTopologySynchronizationGroup.setObjects(
    ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiGetTopologyData")
)
if mibBuilder.loadTexts:
    nbiTopologySynchronizationGroup.setStatus("current")

nbiTopologyOptionalParameterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 2, 2, 4)
)
nbiTopologyOptionalParameterGroup.setObjects(
      *(("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiAdditionalInfo"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiEMSName"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiNEName"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiVersion"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiLocation"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiProductType"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiVendor"))
)
if mibBuilder.loadTexts:
    nbiTopologyOptionalParameterGroup.setStatus("current")


# Notification objects

nbiCreateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 0, 1, 1)
)
nbiCreateNotification.setObjects(
      *(("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiSequenceId"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiObjectInstance"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiNEName"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiEventTime"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiVendor"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiProductType"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiVersion"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiLocation"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiAdministrativeState"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiCommunicationState"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiOperationalState"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiAdditionalInfo"))
)
if mibBuilder.loadTexts:
    nbiCreateNotification.setStatus(
        "current"
    )

nbiDeleteNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 0, 1, 2)
)
nbiDeleteNotification.setObjects(
      *(("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiSequenceId"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiObjectInstance"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiEventTime"))
)
if mibBuilder.loadTexts:
    nbiDeleteNotification.setStatus(
        "current"
    )

nbiAVCNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 0, 1, 3)
)
nbiAVCNotification.setObjects(
      *(("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiSequenceId"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiObjectInstance"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiEventTime"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiChangedAttributeSet"))
)
if mibBuilder.loadTexts:
    nbiAVCNotification.setStatus(
        "current"
    )

nbiStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 0, 1, 4)
)
nbiStateChangeNotification.setObjects(
      *(("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiSequenceId"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiObjectInstance"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiEventTime"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiChangedStateSet"))
)
if mibBuilder.loadTexts:
    nbiStateChangeNotification.setStatus(
        "current"
    )

nbiSyncEMSDataNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 0, 2, 1)
)
nbiSyncEMSDataNotification.setObjects(
      *(("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiSequenceId"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiObjectInstance"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiEMSName"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiEventTime"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiVendor"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiProductType"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiVersion"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiLocation"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiActiveNBIVersion"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiEmsSynchronizationState"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiNotSyncNEs"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiAdditionalInfo"))
)
if mibBuilder.loadTexts:
    nbiSyncEMSDataNotification.setStatus(
        "current"
    )

nbiSyncDataNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 0, 2, 2)
)
nbiSyncDataNotification.setObjects(
      *(("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiObjectInstance"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiNEName"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiEventTime"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiVendor"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiProductType"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiVersion"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiLocation"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiAdministrativeState"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiCommunicationState"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiOperationalState"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiAdditionalInfo"))
)
if mibBuilder.loadTexts:
    nbiSyncDataNotification.setStatus(
        "current"
    )


# Notifications groups

nbiTopologyNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 2, 2, 3)
)
nbiTopologyNotificationGroup.setObjects(
      *(("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiCreateNotification"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiDeleteNotification"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiSyncDataNotification"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiSyncEMSDataNotification"))
)
if mibBuilder.loadTexts:
    nbiTopologyNotificationGroup.setStatus(
        "current"
    )

nbiTopologyOptionalNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 2, 2, 5)
)
nbiTopologyOptionalNotificationGroup.setObjects(
      *(("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiAVCNotification"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiStateChangeNotification"))
)
if mibBuilder.loadTexts:
    nbiTopologyOptionalNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

nbiTopologyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 4, 2, 1, 1)
)
nbiTopologyCompliance.setObjects(
      *(("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiTopologyParameterGroup"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiTopologySynchronizationGroup"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiTopologyNotificationGroup"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiTopologyOptionalParameterGroup"),
        ("NSN-SNMP-NBI-TOPOLOGY-MIB", "nbiTopologyOptionalNotificationGroup"))
)
if mibBuilder.loadTexts:
    nbiTopologyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSN-SNMP-NBI-TOPOLOGY-MIB",
    **{"nbiTopologyManagementMIB": nbiTopologyManagementMIB,
       "nbiTopologyNotifications": nbiTopologyNotifications,
       "nbiTopologySpontaneousNotifications": nbiTopologySpontaneousNotifications,
       "nbiCreateNotification": nbiCreateNotification,
       "nbiDeleteNotification": nbiDeleteNotification,
       "nbiAVCNotification": nbiAVCNotification,
       "nbiStateChangeNotification": nbiStateChangeNotification,
       "nbiTopologySyncNotifications": nbiTopologySyncNotifications,
       "nbiSyncEMSDataNotification": nbiSyncEMSDataNotification,
       "nbiSyncDataNotification": nbiSyncDataNotification,
       "nbiTopologyObjects": nbiTopologyObjects,
       "nbiTopologyParameterObjects": nbiTopologyParameterObjects,
       "nbiActiveNBIVersion": nbiActiveNBIVersion,
       "nbiAdditionalInfo": nbiAdditionalInfo,
       "nbiAdministrativeState": nbiAdministrativeState,
       "nbiChangedAttributeSet": nbiChangedAttributeSet,
       "nbiChangedStateSet": nbiChangedStateSet,
       "nbiCommunicationState": nbiCommunicationState,
       "nbiEMSName": nbiEMSName,
       "nbiLocation": nbiLocation,
       "nbiNEName": nbiNEName,
       "nbiOperationalState": nbiOperationalState,
       "nbiProductType": nbiProductType,
       "nbiVendor": nbiVendor,
       "nbiVersion": nbiVersion,
       "nbiTopologyRequestObjects": nbiTopologyRequestObjects,
       "nbiGetTopologyData": nbiGetTopologyData,
       "nbiNETopologyTable": nbiNETopologyTable,
       "nbiNETopologyEntry": nbiNETopologyEntry,
       "nbiNETableIndex": nbiNETableIndex,
       "nbiNETableObjectInstance": nbiNETableObjectInstance,
       "nbiNETableNEName": nbiNETableNEName,
       "nbiNETableVendor": nbiNETableVendor,
       "nbiNETableProductType": nbiNETableProductType,
       "nbiNETableVersion": nbiNETableVersion,
       "nbiNETableLocation": nbiNETableLocation,
       "nbiNETableAdministrativeState": nbiNETableAdministrativeState,
       "nbiNETableCommunicationState": nbiNETableCommunicationState,
       "nbiNETableOperationalState": nbiNETableOperationalState,
       "nbiNETableAdditionalInfo": nbiNETableAdditionalInfo,
       "nbiTopologyConformance": nbiTopologyConformance,
       "nbiTopologyCompliances": nbiTopologyCompliances,
       "nbiTopologyCompliance": nbiTopologyCompliance,
       "nbiTopologyGroups": nbiTopologyGroups,
       "nbiTopologyParameterGroup": nbiTopologyParameterGroup,
       "nbiTopologySynchronizationGroup": nbiTopologySynchronizationGroup,
       "nbiTopologyNotificationGroup": nbiTopologyNotificationGroup,
       "nbiTopologyOptionalParameterGroup": nbiTopologyOptionalParameterGroup,
       "nbiTopologyOptionalNotificationGroup": nbiTopologyOptionalNotificationGroup}
)
