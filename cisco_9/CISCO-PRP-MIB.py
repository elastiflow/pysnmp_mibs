# SNMP MIB module (CISCO-PRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-PRP-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:18:36 2025
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

ciscoPrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 866)
)
if mibBuilder.loadTexts:
    ciscoPrpMIB.setRevisions(
        ("2019-09-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PrpStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("stateUp", 1),
          ("stateDown", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoPrpMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoPrpMIBNotifs = _CiscoPrpMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 866, 0)
)
_CiscoPrpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoPrpMIBObjects = _CiscoPrpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 866, 1)
)
_CiscoPrpChannelTable_Object = MibTable
ciscoPrpChannelTable = _CiscoPrpChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoPrpChannelTable.setStatus("current")
_CiscoPrpChannelEntry_Object = MibTableRow
ciscoPrpChannelEntry = _CiscoPrpChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1)
)
ciscoPrpChannelEntry.setIndexNames(
    (0, "CISCO-PRP-MIB", "ciscoPrpChannelIndex"),
)
if mibBuilder.loadTexts:
    ciscoPrpChannelEntry.setStatus("current")
_CiscoPrpChannelIndex_Type = Unsigned32
_CiscoPrpChannelIndex_Object = MibTableColumn
ciscoPrpChannelIndex = _CiscoPrpChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 1),
    _CiscoPrpChannelIndex_Type()
)
ciscoPrpChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoPrpChannelIndex.setStatus("current")
_CiscoPrpChannelId_Type = Unsigned32
_CiscoPrpChannelId_Object = MibTableColumn
ciscoPrpChannelId = _CiscoPrpChannelId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 2),
    _CiscoPrpChannelId_Type()
)
ciscoPrpChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoPrpChannelId.setStatus("current")
_CiscoPrpChannelName_Type = DisplayString
_CiscoPrpChannelName_Object = MibTableColumn
ciscoPrpChannelName = _CiscoPrpChannelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 3),
    _CiscoPrpChannelName_Type()
)
ciscoPrpChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoPrpChannelName.setStatus("current")
_CiscoPrpChannelStatus_Type = PrpStatus
_CiscoPrpChannelStatus_Object = MibTableColumn
ciscoPrpChannelStatus = _CiscoPrpChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 4),
    _CiscoPrpChannelStatus_Type()
)
ciscoPrpChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoPrpChannelStatus.setStatus("current")
_CiscoPrpChannelLanAStatus_Type = PrpStatus
_CiscoPrpChannelLanAStatus_Object = MibTableColumn
ciscoPrpChannelLanAStatus = _CiscoPrpChannelLanAStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 5),
    _CiscoPrpChannelLanAStatus_Type()
)
ciscoPrpChannelLanAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoPrpChannelLanAStatus.setStatus("current")
_CiscoPrpChannelLanBStatus_Type = PrpStatus
_CiscoPrpChannelLanBStatus_Object = MibTableColumn
ciscoPrpChannelLanBStatus = _CiscoPrpChannelLanBStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 6),
    _CiscoPrpChannelLanBStatus_Type()
)
ciscoPrpChannelLanBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoPrpChannelLanBStatus.setStatus("current")
_CiscoPrpMIBConform_ObjectIdentity = ObjectIdentity
ciscoPrpMIBConform = _CiscoPrpMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 866, 2)
)
_CiscoPrpMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoPrpMIBCompliances = _CiscoPrpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 866, 2, 1)
)
_CiscoPrpMIBGroups_ObjectIdentity = ObjectIdentity
ciscoPrpMIBGroups = _CiscoPrpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 866, 2, 2)
)

# Managed Objects groups

ciscoPrpMIBMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 866, 2, 2, 1)
)
ciscoPrpMIBMainObjectGroup.setObjects(
      *(("CISCO-PRP-MIB", "ciscoPrpChannelId"),
        ("CISCO-PRP-MIB", "ciscoPrpChannelStatus"),
        ("CISCO-PRP-MIB", "ciscoPrpChannelLanAStatus"),
        ("CISCO-PRP-MIB", "ciscoPrpChannelLanBStatus"),
        ("CISCO-PRP-MIB", "ciscoPrpChannelName"))
)
if mibBuilder.loadTexts:
    ciscoPrpMIBMainObjectGroup.setStatus("current")


# Notification objects

ciscoPrpChannelStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 866, 0, 1)
)
ciscoPrpChannelStateChange.setObjects(
      *(("CISCO-PRP-MIB", "ciscoPrpChannelId"),
        ("CISCO-PRP-MIB", "ciscoPrpChannelName"),
        ("CISCO-PRP-MIB", "ciscoPrpChannelStatus"))
)
if mibBuilder.loadTexts:
    ciscoPrpChannelStateChange.setStatus(
        "current"
    )

ciscoPrpLanAStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 866, 0, 2)
)
ciscoPrpLanAStateChange.setObjects(
      *(("CISCO-PRP-MIB", "ciscoPrpChannelId"),
        ("CISCO-PRP-MIB", "ciscoPrpChannelName"),
        ("CISCO-PRP-MIB", "ciscoPrpChannelLanAStatus"))
)
if mibBuilder.loadTexts:
    ciscoPrpLanAStateChange.setStatus(
        "current"
    )

ciscoPrpLanBStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 866, 0, 3)
)
ciscoPrpLanBStateChange.setObjects(
      *(("CISCO-PRP-MIB", "ciscoPrpChannelId"),
        ("CISCO-PRP-MIB", "ciscoPrpChannelName"),
        ("CISCO-PRP-MIB", "ciscoPrpChannelLanBStatus"))
)
if mibBuilder.loadTexts:
    ciscoPrpLanBStateChange.setStatus(
        "current"
    )


# Notifications groups

ciscoPrpMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 866, 2, 2, 2)
)
ciscoPrpMIBNotificationGroup.setObjects(
      *(("CISCO-PRP-MIB", "ciscoPrpChannelStateChange"),
        ("CISCO-PRP-MIB", "ciscoPrpLanAStateChange"),
        ("CISCO-PRP-MIB", "ciscoPrpLanBStateChange"))
)
if mibBuilder.loadTexts:
    ciscoPrpMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoPrpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 866, 2, 1, 1)
)
ciscoPrpMIBCompliance.setObjects(
      *(("CISCO-PRP-MIB", "ciscoPrpMIBMainObjectGroup"),
        ("CISCO-PRP-MIB", "ciscoPrpMIBNotificationGroup"))
)
if mibBuilder.loadTexts:
    ciscoPrpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PRP-MIB",
    **{"PrpStatus": PrpStatus,
       "ciscoPrpMIB": ciscoPrpMIB,
       "ciscoPrpMIBNotifs": ciscoPrpMIBNotifs,
       "ciscoPrpChannelStateChange": ciscoPrpChannelStateChange,
       "ciscoPrpLanAStateChange": ciscoPrpLanAStateChange,
       "ciscoPrpLanBStateChange": ciscoPrpLanBStateChange,
       "ciscoPrpMIBObjects": ciscoPrpMIBObjects,
       "ciscoPrpChannelTable": ciscoPrpChannelTable,
       "ciscoPrpChannelEntry": ciscoPrpChannelEntry,
       "ciscoPrpChannelIndex": ciscoPrpChannelIndex,
       "ciscoPrpChannelId": ciscoPrpChannelId,
       "ciscoPrpChannelName": ciscoPrpChannelName,
       "ciscoPrpChannelStatus": ciscoPrpChannelStatus,
       "ciscoPrpChannelLanAStatus": ciscoPrpChannelLanAStatus,
       "ciscoPrpChannelLanBStatus": ciscoPrpChannelLanBStatus,
       "ciscoPrpMIBConform": ciscoPrpMIBConform,
       "ciscoPrpMIBCompliances": ciscoPrpMIBCompliances,
       "ciscoPrpMIBCompliance": ciscoPrpMIBCompliance,
       "ciscoPrpMIBGroups": ciscoPrpMIBGroups,
       "ciscoPrpMIBMainObjectGroup": ciscoPrpMIBMainObjectGroup,
       "ciscoPrpMIBNotificationGroup": ciscoPrpMIBNotificationGroup}
)
