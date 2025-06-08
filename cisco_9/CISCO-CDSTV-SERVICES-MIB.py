# SNMP MIB module (CISCO-CDSTV-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-CDSTV-SERVICES-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:52:32 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

ciscoCdstvServicesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 729)
)
if mibBuilder.loadTexts:
    ciscoCdstvServicesMIB.setRevisions(
        ("2010-03-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCdstvServicesMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCdstvServicesMIBNotifs = _CiscoCdstvServicesMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 729, 0)
)
_CiscoCdstvServicesMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCdstvServicesMIBObjects = _CiscoCdstvServicesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 729, 1)
)
_CdstvServicesMonitorTable_Object = MibTable
cdstvServicesMonitorTable = _CdstvServicesMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 729, 1, 1)
)
if mibBuilder.loadTexts:
    cdstvServicesMonitorTable.setStatus("current")
_CdstvServicesMonitorTableEntry_Object = MibTableRow
cdstvServicesMonitorTableEntry = _CdstvServicesMonitorTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 729, 1, 1, 1)
)
cdstvServicesMonitorTableEntry.setIndexNames(
    (0, "CISCO-CDSTV-SERVICES-MIB", "cdstvServicesMonitorIndex"),
)
if mibBuilder.loadTexts:
    cdstvServicesMonitorTableEntry.setStatus("current")


class _CdstvServicesMonitorIndex_Type(Unsigned32):
    """Custom type cdstvServicesMonitorIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdstvServicesMonitorIndex_Type.__name__ = "Unsigned32"
_CdstvServicesMonitorIndex_Object = MibTableColumn
cdstvServicesMonitorIndex = _CdstvServicesMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 729, 1, 1, 1, 1),
    _CdstvServicesMonitorIndex_Type()
)
cdstvServicesMonitorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdstvServicesMonitorIndex.setStatus("current")
_CdstvServiceName_Type = SnmpAdminString
_CdstvServiceName_Object = MibTableColumn
cdstvServiceName = _CdstvServiceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 729, 1, 1, 1, 2),
    _CdstvServiceName_Type()
)
cdstvServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvServiceName.setStatus("current")


class _CdstvServiceStatus_Type(Integer32):
    """Custom type cdstvServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_CdstvServiceStatus_Type.__name__ = "Integer32"
_CdstvServiceStatus_Object = MibTableColumn
cdstvServiceStatus = _CdstvServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 729, 1, 1, 1, 3),
    _CdstvServiceStatus_Type()
)
cdstvServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvServiceStatus.setStatus("current")
_CdstvServiceTrapsEnable_ObjectIdentity = ObjectIdentity
cdstvServiceTrapsEnable = _CdstvServiceTrapsEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 729, 1, 2)
)
_CdstvServiceUpNotifEnable_Type = TruthValue
_CdstvServiceUpNotifEnable_Object = MibScalar
cdstvServiceUpNotifEnable = _CdstvServiceUpNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 729, 1, 2, 1),
    _CdstvServiceUpNotifEnable_Type()
)
cdstvServiceUpNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvServiceUpNotifEnable.setStatus("current")
_CdstvServiceDownNotifEnable_Type = TruthValue
_CdstvServiceDownNotifEnable_Object = MibScalar
cdstvServiceDownNotifEnable = _CdstvServiceDownNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 729, 1, 2, 2),
    _CdstvServiceDownNotifEnable_Type()
)
cdstvServiceDownNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvServiceDownNotifEnable.setStatus("current")
_CiscoCdstvServicesMIBConform_ObjectIdentity = ObjectIdentity
ciscoCdstvServicesMIBConform = _CiscoCdstvServicesMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 729, 2)
)
_CiscoCdstvServicesMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCdstvServicesMIBCompliances = _CiscoCdstvServicesMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 729, 2, 1)
)
_CiscoCdstvServicesMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCdstvServicesMIBGroups = _CiscoCdstvServicesMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 729, 2, 2)
)

# Managed Objects groups

ciscoCdstvServicesMIBMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 729, 2, 2, 1)
)
ciscoCdstvServicesMIBMainObjectGroup.setObjects(
      *(("CISCO-CDSTV-SERVICES-MIB", "cdstvServiceName"),
        ("CISCO-CDSTV-SERVICES-MIB", "cdstvServiceStatus"))
)
if mibBuilder.loadTexts:
    ciscoCdstvServicesMIBMainObjectGroup.setStatus("current")

ciscoCdstvServicesMIBNotifEnableObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 729, 2, 2, 3)
)
ciscoCdstvServicesMIBNotifEnableObjectGroup.setObjects(
      *(("CISCO-CDSTV-SERVICES-MIB", "cdstvServiceUpNotifEnable"),
        ("CISCO-CDSTV-SERVICES-MIB", "cdstvServiceDownNotifEnable"))
)
if mibBuilder.loadTexts:
    ciscoCdstvServicesMIBNotifEnableObjectGroup.setStatus("current")


# Notification objects

cdstvServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 729, 0, 1)
)
cdstvServiceUp.setObjects(
    ("CISCO-CDSTV-SERVICES-MIB", "cdstvServiceName")
)
if mibBuilder.loadTexts:
    cdstvServiceUp.setStatus(
        "current"
    )

cdstvServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 729, 0, 2)
)
cdstvServiceDown.setObjects(
    ("CISCO-CDSTV-SERVICES-MIB", "cdstvServiceName")
)
if mibBuilder.loadTexts:
    cdstvServiceDown.setStatus(
        "current"
    )


# Notifications groups

ciscoCdstvServicesMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 729, 2, 2, 2)
)
ciscoCdstvServicesMIBNotificationGroup.setObjects(
      *(("CISCO-CDSTV-SERVICES-MIB", "cdstvServiceUp"),
        ("CISCO-CDSTV-SERVICES-MIB", "cdstvServiceDown"))
)
if mibBuilder.loadTexts:
    ciscoCdstvServicesMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoCdstvServicesMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 729, 2, 1, 1)
)
ciscoCdstvServicesMIBCompliance.setObjects(
      *(("CISCO-CDSTV-SERVICES-MIB", "ciscoCdstvServicesMIBMainObjectGroup"),
        ("CISCO-CDSTV-SERVICES-MIB", "ciscoCdstvServicesMIBNotificationGroup"),
        ("CISCO-CDSTV-SERVICES-MIB", "ciscoCdstvServicesMIBNotifEnableObjectGroup"))
)
if mibBuilder.loadTexts:
    ciscoCdstvServicesMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CDSTV-SERVICES-MIB",
    **{"ciscoCdstvServicesMIB": ciscoCdstvServicesMIB,
       "ciscoCdstvServicesMIBNotifs": ciscoCdstvServicesMIBNotifs,
       "cdstvServiceUp": cdstvServiceUp,
       "cdstvServiceDown": cdstvServiceDown,
       "ciscoCdstvServicesMIBObjects": ciscoCdstvServicesMIBObjects,
       "cdstvServicesMonitorTable": cdstvServicesMonitorTable,
       "cdstvServicesMonitorTableEntry": cdstvServicesMonitorTableEntry,
       "cdstvServicesMonitorIndex": cdstvServicesMonitorIndex,
       "cdstvServiceName": cdstvServiceName,
       "cdstvServiceStatus": cdstvServiceStatus,
       "cdstvServiceTrapsEnable": cdstvServiceTrapsEnable,
       "cdstvServiceUpNotifEnable": cdstvServiceUpNotifEnable,
       "cdstvServiceDownNotifEnable": cdstvServiceDownNotifEnable,
       "ciscoCdstvServicesMIBConform": ciscoCdstvServicesMIBConform,
       "ciscoCdstvServicesMIBCompliances": ciscoCdstvServicesMIBCompliances,
       "ciscoCdstvServicesMIBCompliance": ciscoCdstvServicesMIBCompliance,
       "ciscoCdstvServicesMIBGroups": ciscoCdstvServicesMIBGroups,
       "ciscoCdstvServicesMIBMainObjectGroup": ciscoCdstvServicesMIBMainObjectGroup,
       "ciscoCdstvServicesMIBNotificationGroup": ciscoCdstvServicesMIBNotificationGroup,
       "ciscoCdstvServicesMIBNotifEnableObjectGroup": ciscoCdstvServicesMIBNotifEnableObjectGroup}
)
