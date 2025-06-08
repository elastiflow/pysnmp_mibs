# SNMP MIB module (DATASTAX-OPSCALERT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/datastax_46272/DATASTAX-OPSCALERT-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:25:19 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

dataStaxOpscAlertTrap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 46272, 1, 0, 1)
)
if mibBuilder.loadTexts:
    dataStaxOpscAlertTrap.setRevisions(
        ("2015-07-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Datastax_ObjectIdentity = ObjectIdentity
datastax = _Datastax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46272)
)
_Opsc_ObjectIdentity = ObjectIdentity
opsc = _Opsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46272, 1)
)
_OpscAlerts_ObjectIdentity = ObjectIdentity
opscAlerts = _OpscAlerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46272, 1, 0)
)
_OpscAlertTable_Object = MibTable
opscAlertTable = _OpscAlertTable_Object(
    (1, 3, 6, 1, 4, 1, 46272, 1, 0, 2)
)
if mibBuilder.loadTexts:
    opscAlertTable.setStatus("current")
_OpscAlertEntry_Object = MibTableRow
opscAlertEntry = _OpscAlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 46272, 1, 0, 2, 1)
)
opscAlertEntry.setIndexNames(
    (0, "DATASTAX-OPSCALERT-MIB", "opscAlertIndex"),
)
if mibBuilder.loadTexts:
    opscAlertEntry.setStatus("current")


class _OpscAlertIndex_Type(Integer32):
    """Custom type opscAlertIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OpscAlertIndex_Type.__name__ = "Integer32"
_OpscAlertIndex_Object = MibTableColumn
opscAlertIndex = _OpscAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 46272, 1, 0, 2, 1, 1),
    _OpscAlertIndex_Type()
)
opscAlertIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    opscAlertIndex.setStatus("current")
_OpscAlertLevel_Type = Integer32
_OpscAlertLevel_Object = MibTableColumn
opscAlertLevel = _OpscAlertLevel_Object(
    (1, 3, 6, 1, 4, 1, 46272, 1, 0, 2, 1, 2),
    _OpscAlertLevel_Type()
)
opscAlertLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opscAlertLevel.setStatus("current")
_OpscAlertLevelStr_Type = OctetString
_OpscAlertLevelStr_Object = MibTableColumn
opscAlertLevelStr = _OpscAlertLevelStr_Object(
    (1, 3, 6, 1, 4, 1, 46272, 1, 0, 2, 1, 3),
    _OpscAlertLevelStr_Type()
)
opscAlertLevelStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opscAlertLevelStr.setStatus("current")
_OpscAlertMessage_Type = OctetString
_OpscAlertMessage_Object = MibTableColumn
opscAlertMessage = _OpscAlertMessage_Object(
    (1, 3, 6, 1, 4, 1, 46272, 1, 0, 2, 1, 4),
    _OpscAlertMessage_Type()
)
opscAlertMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opscAlertMessage.setStatus("current")
_OpscAlertAction_Type = Integer32
_OpscAlertAction_Object = MibTableColumn
opscAlertAction = _OpscAlertAction_Object(
    (1, 3, 6, 1, 4, 1, 46272, 1, 0, 2, 1, 5),
    _OpscAlertAction_Type()
)
opscAlertAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opscAlertAction.setStatus("current")
_OpscAlertCluster_Type = OctetString
_OpscAlertCluster_Object = MibTableColumn
opscAlertCluster = _OpscAlertCluster_Object(
    (1, 3, 6, 1, 4, 1, 46272, 1, 0, 2, 1, 6),
    _OpscAlertCluster_Type()
)
opscAlertCluster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opscAlertCluster.setStatus("current")
_OpscAlertEventSrc_Type = OctetString
_OpscAlertEventSrc_Object = MibTableColumn
opscAlertEventSrc = _OpscAlertEventSrc_Object(
    (1, 3, 6, 1, 4, 1, 46272, 1, 0, 2, 1, 7),
    _OpscAlertEventSrc_Type()
)
opscAlertEventSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opscAlertEventSrc.setStatus("current")
_OpscAlertSrcNode_Type = OctetString
_OpscAlertSrcNode_Object = MibTableColumn
opscAlertSrcNode = _OpscAlertSrcNode_Object(
    (1, 3, 6, 1, 4, 1, 46272, 1, 0, 2, 1, 8),
    _OpscAlertSrcNode_Type()
)
opscAlertSrcNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opscAlertSrcNode.setStatus("current")
_OpscAlertTargNode_Type = OctetString
_OpscAlertTargNode_Object = MibTableColumn
opscAlertTargNode = _OpscAlertTargNode_Object(
    (1, 3, 6, 1, 4, 1, 46272, 1, 0, 2, 1, 9),
    _OpscAlertTargNode_Type()
)
opscAlertTargNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opscAlertTargNode.setStatus("current")
_OpscAlertEpochTime_Type = OctetString
_OpscAlertEpochTime_Object = MibTableColumn
opscAlertEpochTime = _OpscAlertEpochTime_Object(
    (1, 3, 6, 1, 4, 1, 46272, 1, 0, 2, 1, 10),
    _OpscAlertEpochTime_Type()
)
opscAlertEpochTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opscAlertEpochTime.setStatus("current")
_OpscAlertStrTime_Type = OctetString
_OpscAlertStrTime_Object = MibTableColumn
opscAlertStrTime = _OpscAlertStrTime_Object(
    (1, 3, 6, 1, 4, 1, 46272, 1, 0, 2, 1, 11),
    _OpscAlertStrTime_Type()
)
opscAlertStrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opscAlertStrTime.setStatus("current")
_OpscAlertAPISrcIP_Type = OctetString
_OpscAlertAPISrcIP_Object = MibTableColumn
opscAlertAPISrcIP = _OpscAlertAPISrcIP_Object(
    (1, 3, 6, 1, 4, 1, 46272, 1, 0, 2, 1, 12),
    _OpscAlertAPISrcIP_Type()
)
opscAlertAPISrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opscAlertAPISrcIP.setStatus("current")
_OpscAlertUser_Type = OctetString
_OpscAlertUser_Object = MibTableColumn
opscAlertUser = _OpscAlertUser_Object(
    (1, 3, 6, 1, 4, 1, 46272, 1, 0, 2, 1, 13),
    _OpscAlertUser_Type()
)
opscAlertUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opscAlertUser.setStatus("current")

# Managed Objects groups

opscAlertElements = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46272, 1, 0, 4)
)
opscAlertElements.setObjects(
      *(("DATASTAX-OPSCALERT-MIB", "opscAlertLevel"),
        ("DATASTAX-OPSCALERT-MIB", "opscAlertLevelStr"),
        ("DATASTAX-OPSCALERT-MIB", "opscAlertMessage"),
        ("DATASTAX-OPSCALERT-MIB", "opscAlertAction"),
        ("DATASTAX-OPSCALERT-MIB", "opscAlertCluster"),
        ("DATASTAX-OPSCALERT-MIB", "opscAlertEventSrc"),
        ("DATASTAX-OPSCALERT-MIB", "opscAlertSrcNode"),
        ("DATASTAX-OPSCALERT-MIB", "opscAlertTargNode"),
        ("DATASTAX-OPSCALERT-MIB", "opscAlertEpochTime"),
        ("DATASTAX-OPSCALERT-MIB", "opscAlertStrTime"),
        ("DATASTAX-OPSCALERT-MIB", "opscAlertAPISrcIP"),
        ("DATASTAX-OPSCALERT-MIB", "opscAlertUser"))
)
if mibBuilder.loadTexts:
    opscAlertElements.setStatus("current")


# Notification objects

opscAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 46272, 1, 0, 3)
)
opscAlert.setObjects(
      *(("DATASTAX-OPSCALERT-MIB", "opscAlertLevel"),
        ("DATASTAX-OPSCALERT-MIB", "opscAlertLevelStr"),
        ("DATASTAX-OPSCALERT-MIB", "opscAlertMessage"),
        ("DATASTAX-OPSCALERT-MIB", "opscAlertAction"),
        ("DATASTAX-OPSCALERT-MIB", "opscAlertCluster"),
        ("DATASTAX-OPSCALERT-MIB", "opscAlertEventSrc"),
        ("DATASTAX-OPSCALERT-MIB", "opscAlertSrcNode"),
        ("DATASTAX-OPSCALERT-MIB", "opscAlertTargNode"),
        ("DATASTAX-OPSCALERT-MIB", "opscAlertEpochTime"),
        ("DATASTAX-OPSCALERT-MIB", "opscAlertStrTime"),
        ("DATASTAX-OPSCALERT-MIB", "opscAlertAPISrcIP"),
        ("DATASTAX-OPSCALERT-MIB", "opscAlertUser"))
)
if mibBuilder.loadTexts:
    opscAlert.setStatus(
        "current"
    )


# Notifications groups

opscAlertGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 46272, 1, 0, 5)
)
opscAlertGroup.setObjects(
    ("DATASTAX-OPSCALERT-MIB", "opscAlert")
)
if mibBuilder.loadTexts:
    opscAlertGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DATASTAX-OPSCALERT-MIB",
    **{"datastax": datastax,
       "opsc": opsc,
       "opscAlerts": opscAlerts,
       "dataStaxOpscAlertTrap": dataStaxOpscAlertTrap,
       "opscAlertTable": opscAlertTable,
       "opscAlertEntry": opscAlertEntry,
       "opscAlertIndex": opscAlertIndex,
       "opscAlertLevel": opscAlertLevel,
       "opscAlertLevelStr": opscAlertLevelStr,
       "opscAlertMessage": opscAlertMessage,
       "opscAlertAction": opscAlertAction,
       "opscAlertCluster": opscAlertCluster,
       "opscAlertEventSrc": opscAlertEventSrc,
       "opscAlertSrcNode": opscAlertSrcNode,
       "opscAlertTargNode": opscAlertTargNode,
       "opscAlertEpochTime": opscAlertEpochTime,
       "opscAlertStrTime": opscAlertStrTime,
       "opscAlertAPISrcIP": opscAlertAPISrcIP,
       "opscAlertUser": opscAlertUser,
       "opscAlert": opscAlert,
       "opscAlertElements": opscAlertElements,
       "opscAlertGroup": opscAlertGroup}
)
