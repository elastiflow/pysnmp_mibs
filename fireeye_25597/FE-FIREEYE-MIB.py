# SNMP MIB module (FE-FIREEYE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/fireeye_25597/FE-FIREEYE-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:02:53 2025
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fireeyeMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 20, 1)
)
if mibBuilder.loadTexts:
    fireeyeMibModule.setRevisions(
        ("2017-03-03 18:52",
         "2016-12-06 15:23",
         "2016-11-30 10:07",
         "2016-11-15 15:58",
         "2016-11-10 16:18",
         "2016-10-11 16:17",
         "2016-10-07 14:38",
         "2016-07-15 21:17",
         "2016-06-15 10:45",
         "2016-06-13 14:01",
         "2016-04-29 11:10",
         "2016-04-25 10:50",
         "2015-11-19 13:49",
         "2015-09-28 11:32",
         "2015-08-20 20:11",
         "2015-08-20 09:22",
         "2015-03-26 22:02",
         "2014-10-06 21:20",
         "2014-10-02 14:50",
         "2014-09-27 17:20",
         "2014-06-28 11:20",
         "2014-06-18 11:20",
         "2014-05-27 11:40",
         "2014-04-07 11:20",
         "2014-04-02 10:40",
         "2014-03-19 10:40",
         "2014-03-10 10:00",
         "2014-01-21 21:00",
         "2011-09-08 19:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fireeye_ObjectIdentity = ObjectIdentity
fireeye = _Fireeye_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597)
)
_Variables_ObjectIdentity = ObjectIdentity
variables = _Variables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 1)
)
_Lms_ObjectIdentity = ObjectIdentity
lms = _Lms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1)
)
_LmsVersion_Type = OctetString
_LmsVersion_Object = MibScalar
lmsVersion = _LmsVersion_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 1),
    _LmsVersion_Type()
)
lmsVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lmsVersion.setStatus("current")
_EventTable_Object = MibTable
eventTable = _EventTable_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2)
)
if mibBuilder.loadTexts:
    eventTable.setStatus("current")
_EventEntry_Object = MibTableRow
eventEntry = _EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1)
)
eventEntry.setIndexNames(
    (0, "FE-FIREEYE-MIB", "eventIndex"),
)
if mibBuilder.loadTexts:
    eventEntry.setStatus("current")
_EventIndex_Type = Unsigned32
_EventIndex_Object = MibTableColumn
eventIndex = _EventIndex_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 1),
    _EventIndex_Type()
)
eventIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventIndex.setStatus("current")
_EventId_Type = Unsigned32
_EventId_Object = MibTableColumn
eventId = _EventId_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 2),
    _EventId_Type()
)
eventId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventId.setStatus("current")
_EventType_Type = OctetString
_EventType_Object = MibTableColumn
eventType = _EventType_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 3),
    _EventType_Type()
)
eventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventType.setStatus("current")
_EventDate_Type = OctetString
_EventDate_Object = MibTableColumn
eventDate = _EventDate_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 4),
    _EventDate_Type()
)
eventDate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventDate.setStatus("current")
_EventTime_Type = OctetString
_EventTime_Object = MibTableColumn
eventTime = _EventTime_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 5),
    _EventTime_Type()
)
eventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTime.setStatus("current")
_EventTraceId_Type = Counter64
_EventTraceId_Object = MibTableColumn
eventTraceId = _EventTraceId_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 6),
    _EventTraceId_Type()
)
eventTraceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTraceId.setStatus("current")
_EventSrcIp_Type = IpAddress
_EventSrcIp_Object = MibTableColumn
eventSrcIp = _EventSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 7),
    _EventSrcIp_Type()
)
eventSrcIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventSrcIp.setStatus("current")
_EventDstIp_Type = IpAddress
_EventDstIp_Object = MibTableColumn
eventDstIp = _EventDstIp_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 8),
    _EventDstIp_Type()
)
eventDstIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventDstIp.setStatus("current")
_EventSrcMac_Type = OctetString
_EventSrcMac_Object = MibTableColumn
eventSrcMac = _EventSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 9),
    _EventSrcMac_Type()
)
eventSrcMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventSrcMac.setStatus("current")
_EventDstMac_Type = OctetString
_EventDstMac_Object = MibTableColumn
eventDstMac = _EventDstMac_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 10),
    _EventDstMac_Type()
)
eventDstMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventDstMac.setStatus("current")
_EventDstPort_Type = Integer32
_EventDstPort_Object = MibTableColumn
eventDstPort = _EventDstPort_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 11),
    _EventDstPort_Type()
)
eventDstPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventDstPort.setStatus("current")
_EventVlan_Type = Integer32
_EventVlan_Object = MibTableColumn
eventVlan = _EventVlan_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 12),
    _EventVlan_Type()
)
eventVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventVlan.setStatus("current")
_EventProtocol_Type = OctetString
_EventProtocol_Object = MibTableColumn
eventProtocol = _EventProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 13),
    _EventProtocol_Type()
)
eventProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventProtocol.setStatus("current")
_EventProfileId_Type = Unsigned32
_EventProfileId_Object = MibTableColumn
eventProfileId = _EventProfileId_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 14),
    _EventProfileId_Type()
)
eventProfileId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventProfileId.setStatus("current")
_EventOsInfo_Type = OctetString
_EventOsInfo_Object = MibTableColumn
eventOsInfo = _EventOsInfo_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 15),
    _EventOsInfo_Type()
)
eventOsInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventOsInfo.setStatus("current")
_EventService_Type = OctetString
_EventService_Object = MibTableColumn
eventService = _EventService_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 16),
    _EventService_Type()
)
eventService.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventService.setStatus("current")
_EventAttackType_Type = OctetString
_EventAttackType_Object = MibTableColumn
eventAttackType = _EventAttackType_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 17),
    _EventAttackType_Type()
)
eventAttackType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventAttackType.setStatus("current")
_EventSignatureName_Type = OctetString
_EventSignatureName_Object = MibTableColumn
eventSignatureName = _EventSignatureName_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 18),
    _EventSignatureName_Type()
)
eventSignatureName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventSignatureName.setStatus("current")
_EventSignatureType_Type = OctetString
_EventSignatureType_Object = MibTableColumn
eventSignatureType = _EventSignatureType_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 19),
    _EventSignatureType_Type()
)
eventSignatureType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventSignatureType.setStatus("current")
_EventSrcHost_Type = OctetString
_EventSrcHost_Object = MibTableColumn
eventSrcHost = _EventSrcHost_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 20),
    _EventSrcHost_Type()
)
eventSrcHost.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventSrcHost.setStatus("current")
_EventCncNo_Type = Unsigned32
_EventCncNo_Object = MibTableColumn
eventCncNo = _EventCncNo_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 21),
    _EventCncNo_Type()
)
eventCncNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventCncNo.setStatus("current")
_AlertSignatureId_Type = Unsigned32
_AlertSignatureId_Object = MibTableColumn
alertSignatureId = _AlertSignatureId_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 22),
    _AlertSignatureId_Type()
)
alertSignatureId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertSignatureId.setStatus("current")
_AlertCncHost_Type = OctetString
_AlertCncHost_Object = MibTableColumn
alertCncHost = _AlertCncHost_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 23),
    _AlertCncHost_Type()
)
alertCncHost.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertCncHost.setStatus("current")
_AlertCncPort_Type = Integer32
_AlertCncPort_Object = MibTableColumn
alertCncPort = _AlertCncPort_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 24),
    _AlertCncPort_Type()
)
alertCncPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertCncPort.setStatus("current")
_AlertChecksum_Type = OctetString
_AlertChecksum_Object = MibTableColumn
alertChecksum = _AlertChecksum_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 25),
    _AlertChecksum_Type()
)
alertChecksum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertChecksum.setStatus("current")
_AlertAnalysisType_Type = OctetString
_AlertAnalysisType_Object = MibTableColumn
alertAnalysisType = _AlertAnalysisType_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 26),
    _AlertAnalysisType_Type()
)
alertAnalysisType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertAnalysisType.setStatus("current")
_AlertProfile_Type = OctetString
_AlertProfile_Object = MibTableColumn
alertProfile = _AlertProfile_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 27),
    _AlertProfile_Type()
)
alertProfile.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertProfile.setStatus("current")
_AlertAction_Type = OctetString
_AlertAction_Object = MibTableColumn
alertAction = _AlertAction_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 28),
    _AlertAction_Type()
)
alertAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertAction.setStatus("current")
_AlertInterface_Type = OctetString
_AlertInterface_Object = MibTableColumn
alertInterface = _AlertInterface_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 29),
    _AlertInterface_Type()
)
alertInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertInterface.setStatus("current")
_AlertSensorIp_Type = IpAddress
_AlertSensorIp_Object = MibTableColumn
alertSensorIp = _AlertSensorIp_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 30),
    _AlertSensorIp_Type()
)
alertSensorIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertSensorIp.setStatus("current")
_AlertSensorHost_Type = OctetString
_AlertSensorHost_Object = MibTableColumn
alertSensorHost = _AlertSensorHost_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 31),
    _AlertSensorHost_Type()
)
alertSensorHost.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertSensorHost.setStatus("current")
_AlertSensorProduct_Type = OctetString
_AlertSensorProduct_Object = MibTableColumn
alertSensorProduct = _AlertSensorProduct_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 32),
    _AlertSensorProduct_Type()
)
alertSensorProduct.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertSensorProduct.setStatus("current")
_AlertSensorRelease_Type = OctetString
_AlertSensorRelease_Object = MibTableColumn
alertSensorRelease = _AlertSensorRelease_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 33),
    _AlertSensorRelease_Type()
)
alertSensorRelease.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertSensorRelease.setStatus("current")
_AlertUrl_Type = OctetString
_AlertUrl_Object = MibTableColumn
alertUrl = _AlertUrl_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 34),
    _AlertUrl_Type()
)
alertUrl.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertUrl.setStatus("current")
_EventSrcAddrType_Type = InetAddressType
_EventSrcAddrType_Object = MibTableColumn
eventSrcAddrType = _EventSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 35),
    _EventSrcAddrType_Type()
)
eventSrcAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventSrcAddrType.setStatus("current")
_EventSrcAddr_Type = InetAddress
_EventSrcAddr_Object = MibTableColumn
eventSrcAddr = _EventSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 36),
    _EventSrcAddr_Type()
)
eventSrcAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventSrcAddr.setStatus("current")
_EventDstAddrType_Type = InetAddressType
_EventDstAddrType_Object = MibTableColumn
eventDstAddrType = _EventDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 37),
    _EventDstAddrType_Type()
)
eventDstAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventDstAddrType.setStatus("current")
_EventDstAddr_Type = InetAddress
_EventDstAddr_Object = MibTableColumn
eventDstAddr = _EventDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 38),
    _EventDstAddr_Type()
)
eventDstAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventDstAddr.setStatus("current")
_EventSensorAddrType_Type = InetAddressType
_EventSensorAddrType_Object = MibTableColumn
eventSensorAddrType = _EventSensorAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 39),
    _EventSensorAddrType_Type()
)
eventSensorAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventSensorAddrType.setStatus("current")
_EventSensorAddr_Type = InetAddress
_EventSensorAddr_Object = MibTableColumn
eventSensorAddr = _EventSensorAddr_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 40),
    _EventSensorAddr_Type()
)
eventSensorAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventSensorAddr.setStatus("current")
_EventSrcPort_Type = Integer32
_EventSrcPort_Object = MibTableColumn
eventSrcPort = _EventSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 41),
    _EventSrcPort_Type()
)
eventSrcPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventSrcPort.setStatus("current")
_EventDateTime_Type = OctetString
_EventDateTime_Object = MibTableColumn
eventDateTime = _EventDateTime_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 42),
    _EventDateTime_Type()
)
eventDateTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventDateTime.setStatus("current")
_IpsSignatureId_Type = Unsigned32
_IpsSignatureId_Object = MibTableColumn
ipsSignatureId = _IpsSignatureId_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 43),
    _IpsSignatureId_Type()
)
ipsSignatureId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsSignatureId.setStatus("current")
_IpsSignatureRevision_Type = Unsigned32
_IpsSignatureRevision_Object = MibTableColumn
ipsSignatureRevision = _IpsSignatureRevision_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 44),
    _IpsSignatureRevision_Type()
)
ipsSignatureRevision.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsSignatureRevision.setStatus("current")
_IpsMatchCount_Type = Gauge32
_IpsMatchCount_Object = MibTableColumn
ipsMatchCount = _IpsMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 45),
    _IpsMatchCount_Type()
)
ipsMatchCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsMatchCount.setStatus("current")
_IpsSeverity_Type = OctetString
_IpsSeverity_Object = MibTableColumn
ipsSeverity = _IpsSeverity_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 46),
    _IpsSeverity_Type()
)
ipsSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsSeverity.setStatus("current")
_IpsSignatureName_Type = OctetString
_IpsSignatureName_Object = MibTableColumn
ipsSignatureName = _IpsSignatureName_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 47),
    _IpsSignatureName_Type()
)
ipsSignatureName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsSignatureName.setStatus("current")
_IpsReferenceId_Type = OctetString
_IpsReferenceId_Object = MibTableColumn
ipsReferenceId = _IpsReferenceId_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 48),
    _IpsReferenceId_Type()
)
ipsReferenceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsReferenceId.setStatus("current")
_IpsBlockMode_Type = OctetString
_IpsBlockMode_Object = MibTableColumn
ipsBlockMode = _IpsBlockMode_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 49),
    _IpsBlockMode_Type()
)
ipsBlockMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsBlockMode.setStatus("current")
_IpsAttackTarget_Type = OctetString
_IpsAttackTarget_Object = MibTableColumn
ipsAttackTarget = _IpsAttackTarget_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 50),
    _IpsAttackTarget_Type()
)
ipsAttackTarget.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsAttackTarget.setStatus("current")
_IsMalicious_Type = TruthValue
_IsMalicious_Object = MibTableColumn
isMalicious = _IsMalicious_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 51),
    _IsMalicious_Type()
)
isMalicious.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isMalicious.setStatus("current")
_IpsAttackConfirmation_Type = OctetString
_IpsAttackConfirmation_Object = MibTableColumn
ipsAttackConfirmation = _IpsAttackConfirmation_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 52),
    _IpsAttackConfirmation_Type()
)
ipsAttackConfirmation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsAttackConfirmation.setStatus("current")
_IsRetroactive_Type = TruthValue
_IsRetroactive_Object = MibTableColumn
isRetroactive = _IsRetroactive_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 53),
    _IsRetroactive_Type()
)
isRetroactive.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isRetroactive.setStatus("current")
_EventCount_Type = Unsigned32
_EventCount_Object = MibScalar
eventCount = _EventCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 3),
    _EventCount_Type()
)
eventCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventCount.setStatus("current")
_Notifications_ObjectIdentity = ObjectIdentity
notifications = _Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 3)
)
_NotificationPrefix_ObjectIdentity = ObjectIdentity
notificationPrefix = _NotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 3, 0)
)
_FeCommon_ObjectIdentity = ObjectIdentity
feCommon = _FeCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11)
)
_FeSystem_ObjectIdentity = ObjectIdentity
feSystem = _FeSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1)
)
_FeSystemTraps_ObjectIdentity = ObjectIdentity
feSystemTraps = _FeSystemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 0)
)
_FeSystemInfo_ObjectIdentity = ObjectIdentity
feSystemInfo = _FeSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1)
)
_FeSystemStatus_Type = OctetString
_FeSystemStatus_Object = MibScalar
feSystemStatus = _FeSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 1),
    _FeSystemStatus_Type()
)
feSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSystemStatus.setStatus("current")
_FeHardwareModel_Type = OctetString
_FeHardwareModel_Object = MibScalar
feHardwareModel = _FeHardwareModel_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 2),
    _FeHardwareModel_Type()
)
feHardwareModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feHardwareModel.setStatus("current")
_FeSerialNumber_Type = OctetString
_FeSerialNumber_Object = MibScalar
feSerialNumber = _FeSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 3),
    _FeSerialNumber_Type()
)
feSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSerialNumber.setStatus("current")
_FeTemperatureValue_Type = Integer32
_FeTemperatureValue_Object = MibScalar
feTemperatureValue = _FeTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 4),
    _FeTemperatureValue_Type()
)
feTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTemperatureValue.setStatus("current")
_FeTemperatureStatus_Type = OctetString
_FeTemperatureStatus_Object = MibScalar
feTemperatureStatus = _FeTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 5),
    _FeTemperatureStatus_Type()
)
feTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTemperatureStatus.setStatus("current")
_FeTemperatureIsHealthy_Type = TruthValue
_FeTemperatureIsHealthy_Object = MibScalar
feTemperatureIsHealthy = _FeTemperatureIsHealthy_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 6),
    _FeTemperatureIsHealthy_Type()
)
feTemperatureIsHealthy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTemperatureIsHealthy.setStatus("current")
_FeIfLinkChangeIfname_Type = OctetString
_FeIfLinkChangeIfname_Object = MibScalar
feIfLinkChangeIfname = _FeIfLinkChangeIfname_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 7),
    _FeIfLinkChangeIfname_Type()
)
feIfLinkChangeIfname.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feIfLinkChangeIfname.setStatus("current")
_FeIfLinkChangeOldAdminUp_Type = TruthValue
_FeIfLinkChangeOldAdminUp_Object = MibScalar
feIfLinkChangeOldAdminUp = _FeIfLinkChangeOldAdminUp_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 8),
    _FeIfLinkChangeOldAdminUp_Type()
)
feIfLinkChangeOldAdminUp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feIfLinkChangeOldAdminUp.setStatus("current")
_FeIfLinkChangeNewAdminUp_Type = TruthValue
_FeIfLinkChangeNewAdminUp_Object = MibScalar
feIfLinkChangeNewAdminUp = _FeIfLinkChangeNewAdminUp_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 9),
    _FeIfLinkChangeNewAdminUp_Type()
)
feIfLinkChangeNewAdminUp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feIfLinkChangeNewAdminUp.setStatus("current")
_FeIfLinkChangeOldLinkUp_Type = TruthValue
_FeIfLinkChangeOldLinkUp_Object = MibScalar
feIfLinkChangeOldLinkUp = _FeIfLinkChangeOldLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 10),
    _FeIfLinkChangeOldLinkUp_Type()
)
feIfLinkChangeOldLinkUp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feIfLinkChangeOldLinkUp.setStatus("current")
_FeIfLinkChangeNewLinkUp_Type = TruthValue
_FeIfLinkChangeNewLinkUp_Object = MibScalar
feIfLinkChangeNewLinkUp = _FeIfLinkChangeNewLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 11),
    _FeIfLinkChangeNewLinkUp_Type()
)
feIfLinkChangeNewLinkUp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feIfLinkChangeNewLinkUp.setStatus("current")
_FeIfLinkChangeOldSpeed_Type = Integer32
_FeIfLinkChangeOldSpeed_Object = MibScalar
feIfLinkChangeOldSpeed = _FeIfLinkChangeOldSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 12),
    _FeIfLinkChangeOldSpeed_Type()
)
feIfLinkChangeOldSpeed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feIfLinkChangeOldSpeed.setStatus("current")
_FeIfLinkChangeNewSpeed_Type = Integer32
_FeIfLinkChangeNewSpeed_Object = MibScalar
feIfLinkChangeNewSpeed = _FeIfLinkChangeNewSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 13),
    _FeIfLinkChangeNewSpeed_Type()
)
feIfLinkChangeNewSpeed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feIfLinkChangeNewSpeed.setStatus("current")
_FeIfLinkChangeOldDuplex_Type = Integer32
_FeIfLinkChangeOldDuplex_Object = MibScalar
feIfLinkChangeOldDuplex = _FeIfLinkChangeOldDuplex_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 14),
    _FeIfLinkChangeOldDuplex_Type()
)
feIfLinkChangeOldDuplex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feIfLinkChangeOldDuplex.setStatus("current")
_FeIfLinkChangeNewDuplex_Type = Integer32
_FeIfLinkChangeNewDuplex_Object = MibScalar
feIfLinkChangeNewDuplex = _FeIfLinkChangeNewDuplex_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 15),
    _FeIfLinkChangeNewDuplex_Type()
)
feIfLinkChangeNewDuplex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feIfLinkChangeNewDuplex.setStatus("current")
_FeIfLinkChangeOldAutoNeg_Type = TruthValue
_FeIfLinkChangeOldAutoNeg_Object = MibScalar
feIfLinkChangeOldAutoNeg = _FeIfLinkChangeOldAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 16),
    _FeIfLinkChangeOldAutoNeg_Type()
)
feIfLinkChangeOldAutoNeg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feIfLinkChangeOldAutoNeg.setStatus("current")
_FeIfLinkChangeNewAutoNeg_Type = TruthValue
_FeIfLinkChangeNewAutoNeg_Object = MibScalar
feIfLinkChangeNewAutoNeg = _FeIfLinkChangeNewAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 17),
    _FeIfLinkChangeNewAutoNeg_Type()
)
feIfLinkChangeNewAutoNeg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feIfLinkChangeNewAutoNeg.setStatus("current")
_FeFaasVpnConnected_Type = TruthValue
_FeFaasVpnConnected_Object = MibScalar
feFaasVpnConnected = _FeFaasVpnConnected_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 18),
    _FeFaasVpnConnected_Type()
)
feFaasVpnConnected.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feFaasVpnConnected.setStatus("current")
_FeProcessCrashName_Type = OctetString
_FeProcessCrashName_Object = MibScalar
feProcessCrashName = _FeProcessCrashName_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 19),
    _FeProcessCrashName_Type()
)
feProcessCrashName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feProcessCrashName.setStatus("current")
_FeProcessCrashNumFailures_Type = Gauge32
_FeProcessCrashNumFailures_Object = MibScalar
feProcessCrashNumFailures = _FeProcessCrashNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 20),
    _FeProcessCrashNumFailures_Type()
)
feProcessCrashNumFailures.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feProcessCrashNumFailures.setStatus("current")
_FeProcessCrashLive_Type = TruthValue
_FeProcessCrashLive_Object = MibScalar
feProcessCrashLive = _FeProcessCrashLive_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 21),
    _FeProcessCrashLive_Type()
)
feProcessCrashLive.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feProcessCrashLive.setStatus("current")
_FeSyslogRotationReason_Type = OctetString
_FeSyslogRotationReason_Object = MibScalar
feSyslogRotationReason = _FeSyslogRotationReason_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 22),
    _FeSyslogRotationReason_Type()
)
feSyslogRotationReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feSyslogRotationReason.setStatus("current")
_FeLoginUsername_Type = OctetString
_FeLoginUsername_Object = MibScalar
feLoginUsername = _FeLoginUsername_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 23),
    _FeLoginUsername_Type()
)
feLoginUsername.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feLoginUsername.setStatus("current")
_FeLoginUsernameLocal_Type = OctetString
_FeLoginUsernameLocal_Object = MibScalar
feLoginUsernameLocal = _FeLoginUsernameLocal_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 26),
    _FeLoginUsernameLocal_Type()
)
feLoginUsernameLocal.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feLoginUsernameLocal.setStatus("current")
_FeLoginTimestamp_Type = DateAndTime
_FeLoginTimestamp_Object = MibScalar
feLoginTimestamp = _FeLoginTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 27),
    _FeLoginTimestamp_Type()
)
feLoginTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feLoginTimestamp.setStatus("current")
_FeLoginRemoteAddr_Type = IpAddress
_FeLoginRemoteAddr_Object = MibScalar
feLoginRemoteAddr = _FeLoginRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 28),
    _FeLoginRemoteAddr_Type()
)
feLoginRemoteAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feLoginRemoteAddr.setStatus("current")
_FeLoginRemoteInetAddrType_Type = InetAddressType
_FeLoginRemoteInetAddrType_Object = MibScalar
feLoginRemoteInetAddrType = _FeLoginRemoteInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 29),
    _FeLoginRemoteInetAddrType_Type()
)
feLoginRemoteInetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feLoginRemoteInetAddrType.setStatus("current")
_FeLoginRemoteInetAddr_Type = InetAddress
_FeLoginRemoteInetAddr_Object = MibScalar
feLoginRemoteInetAddr = _FeLoginRemoteInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 30),
    _FeLoginRemoteInetAddr_Type()
)
feLoginRemoteInetAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feLoginRemoteInetAddr.setStatus("current")
_FeLoginRemoteHostname_Type = OctetString
_FeLoginRemoteHostname_Object = MibScalar
feLoginRemoteHostname = _FeLoginRemoteHostname_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 31),
    _FeLoginRemoteHostname_Type()
)
feLoginRemoteHostname.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feLoginRemoteHostname.setStatus("current")
_FeLoginPeerId_Type = OctetString
_FeLoginPeerId_Object = MibScalar
feLoginPeerId = _FeLoginPeerId_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 32),
    _FeLoginPeerId_Type()
)
feLoginPeerId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feLoginPeerId.setStatus("current")
_FeLoginClientDescr_Type = OctetString
_FeLoginClientDescr_Object = MibScalar
feLoginClientDescr = _FeLoginClientDescr_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 33),
    _FeLoginClientDescr_Type()
)
feLoginClientDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feLoginClientDescr.setStatus("current")
_FeLoginSessionId_Type = Unsigned32
_FeLoginSessionId_Object = MibScalar
feLoginSessionId = _FeLoginSessionId_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 34),
    _FeLoginSessionId_Type()
)
feLoginSessionId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feLoginSessionId.setStatus("current")
_FeLoginTimestampOrigAuth_Type = DateAndTime
_FeLoginTimestampOrigAuth_Object = MibScalar
feLoginTimestampOrigAuth = _FeLoginTimestampOrigAuth_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 35),
    _FeLoginTimestampOrigAuth_Type()
)
feLoginTimestampOrigAuth.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feLoginTimestampOrigAuth.setStatus("current")
_FeLoginAuthMethod_Type = OctetString
_FeLoginAuthMethod_Object = MibScalar
feLoginAuthMethod = _FeLoginAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 36),
    _FeLoginAuthMethod_Type()
)
feLoginAuthMethod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feLoginAuthMethod.setStatus("current")
_FeLoginTrusted_Type = TruthValue
_FeLoginTrusted_Object = MibScalar
feLoginTrusted = _FeLoginTrusted_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 37),
    _FeLoginTrusted_Type()
)
feLoginTrusted.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feLoginTrusted.setStatus("current")
_FeLoginAuthSubmethod_Type = OctetString
_FeLoginAuthSubmethod_Object = MibScalar
feLoginAuthSubmethod = _FeLoginAuthSubmethod_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 38),
    _FeLoginAuthSubmethod_Type()
)
feLoginAuthSubmethod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feLoginAuthSubmethod.setStatus("current")
_FeLoginRole_Type = OctetString
_FeLoginRole_Object = MibScalar
feLoginRole = _FeLoginRole_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 39),
    _FeLoginRole_Type()
)
feLoginRole.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feLoginRole.setStatus("current")
_FeAwsInstanceId_Type = OctetString
_FeAwsInstanceId_Object = MibScalar
feAwsInstanceId = _FeAwsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 40),
    _FeAwsInstanceId_Type()
)
feAwsInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feAwsInstanceId.setStatus("current")
_FeAwsInstanceType_Type = OctetString
_FeAwsInstanceType_Object = MibScalar
feAwsInstanceType = _FeAwsInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 41),
    _FeAwsInstanceType_Type()
)
feAwsInstanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feAwsInstanceType.setStatus("current")
_FeAwsImageId_Type = OctetString
_FeAwsImageId_Object = MibScalar
feAwsImageId = _FeAwsImageId_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 42),
    _FeAwsImageId_Type()
)
feAwsImageId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feAwsImageId.setStatus("current")
_FeStorage_ObjectIdentity = ObjectIdentity
feStorage = _FeStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2)
)
_FeStorageTraps_ObjectIdentity = ObjectIdentity
feStorageTraps = _FeStorageTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 0)
)
_FeStorageInfo_ObjectIdentity = ObjectIdentity
feStorageInfo = _FeStorageInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 1)
)
_FeRaidStatus_Type = OctetString
_FeRaidStatus_Object = MibScalar
feRaidStatus = _FeRaidStatus_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 1, 1),
    _FeRaidStatus_Type()
)
feRaidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feRaidStatus.setStatus("current")
_FeRaidIsHealthy_Type = TruthValue
_FeRaidIsHealthy_Object = MibScalar
feRaidIsHealthy = _FeRaidIsHealthy_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 1, 2),
    _FeRaidIsHealthy_Type()
)
feRaidIsHealthy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feRaidIsHealthy.setStatus("current")
_FePhysicalDiskTable_Object = MibTable
fePhysicalDiskTable = _FePhysicalDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 1, 3)
)
if mibBuilder.loadTexts:
    fePhysicalDiskTable.setStatus("current")
_FePhysicalDiskEntry_Object = MibTableRow
fePhysicalDiskEntry = _FePhysicalDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 1, 3, 1)
)
fePhysicalDiskEntry.setIndexNames(
    (0, "FE-FIREEYE-MIB", "fePhysicalDiskIndex"),
)
if mibBuilder.loadTexts:
    fePhysicalDiskEntry.setStatus("current")
_FePhysicalDiskIndex_Type = Unsigned32
_FePhysicalDiskIndex_Object = MibTableColumn
fePhysicalDiskIndex = _FePhysicalDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 1, 3, 1, 1),
    _FePhysicalDiskIndex_Type()
)
fePhysicalDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePhysicalDiskIndex.setStatus("current")
_FePhysicalDiskName_Type = OctetString
_FePhysicalDiskName_Object = MibTableColumn
fePhysicalDiskName = _FePhysicalDiskName_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 1, 3, 1, 2),
    _FePhysicalDiskName_Type()
)
fePhysicalDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePhysicalDiskName.setStatus("current")
_FePhysicalDiskStatus_Type = OctetString
_FePhysicalDiskStatus_Object = MibTableColumn
fePhysicalDiskStatus = _FePhysicalDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 1, 3, 1, 3),
    _FePhysicalDiskStatus_Type()
)
fePhysicalDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePhysicalDiskStatus.setStatus("current")
_FePhysicalDiskIsHealthy_Type = TruthValue
_FePhysicalDiskIsHealthy_Object = MibTableColumn
fePhysicalDiskIsHealthy = _FePhysicalDiskIsHealthy_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 1, 3, 1, 4),
    _FePhysicalDiskIsHealthy_Type()
)
fePhysicalDiskIsHealthy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePhysicalDiskIsHealthy.setStatus("current")
_FePhysicalDiskDeviceSupport_Type = OctetString
_FePhysicalDiskDeviceSupport_Object = MibTableColumn
fePhysicalDiskDeviceSupport = _FePhysicalDiskDeviceSupport_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 1, 3, 1, 5),
    _FePhysicalDiskDeviceSupport_Type()
)
fePhysicalDiskDeviceSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePhysicalDiskDeviceSupport.setStatus("current")
_FePhysicalDiskSelfAssess_Type = OctetString
_FePhysicalDiskSelfAssess_Object = MibTableColumn
fePhysicalDiskSelfAssess = _FePhysicalDiskSelfAssess_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 1, 3, 1, 6),
    _FePhysicalDiskSelfAssess_Type()
)
fePhysicalDiskSelfAssess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePhysicalDiskSelfAssess.setStatus("current")
_FePhysicalDiskTotalBytes_Type = OctetString
_FePhysicalDiskTotalBytes_Object = MibTableColumn
fePhysicalDiskTotalBytes = _FePhysicalDiskTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 1, 3, 1, 7),
    _FePhysicalDiskTotalBytes_Type()
)
fePhysicalDiskTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePhysicalDiskTotalBytes.setStatus("current")
_FePowerSupply_ObjectIdentity = ObjectIdentity
fePowerSupply = _FePowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 3)
)
_FePowerSupplyTraps_ObjectIdentity = ObjectIdentity
fePowerSupplyTraps = _FePowerSupplyTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 3, 0)
)
_FePowerSupplyInfo_ObjectIdentity = ObjectIdentity
fePowerSupplyInfo = _FePowerSupplyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 3, 1)
)
_FePowerSupplyOverallStatus_Type = OctetString
_FePowerSupplyOverallStatus_Object = MibScalar
fePowerSupplyOverallStatus = _FePowerSupplyOverallStatus_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 3, 1, 1),
    _FePowerSupplyOverallStatus_Type()
)
fePowerSupplyOverallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePowerSupplyOverallStatus.setStatus("current")
_FePowerSupplyOverallIsHealthy_Type = TruthValue
_FePowerSupplyOverallIsHealthy_Object = MibScalar
fePowerSupplyOverallIsHealthy = _FePowerSupplyOverallIsHealthy_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 3, 1, 2),
    _FePowerSupplyOverallIsHealthy_Type()
)
fePowerSupplyOverallIsHealthy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePowerSupplyOverallIsHealthy.setStatus("current")
_FePowerSupplyTable_Object = MibTable
fePowerSupplyTable = _FePowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 3, 1, 3)
)
if mibBuilder.loadTexts:
    fePowerSupplyTable.setStatus("current")
_FePowerSupplyEntry_Object = MibTableRow
fePowerSupplyEntry = _FePowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 3, 1, 3, 1)
)
fePowerSupplyEntry.setIndexNames(
    (0, "FE-FIREEYE-MIB", "fePowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    fePowerSupplyEntry.setStatus("deprecated")
_FePowerSupplyIndex_Type = Unsigned32
_FePowerSupplyIndex_Object = MibTableColumn
fePowerSupplyIndex = _FePowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 3, 1, 3, 1, 1),
    _FePowerSupplyIndex_Type()
)
fePowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePowerSupplyIndex.setStatus("deprecated")
_FePowerSupplyStatus_Type = OctetString
_FePowerSupplyStatus_Object = MibTableColumn
fePowerSupplyStatus = _FePowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 3, 1, 3, 1, 2),
    _FePowerSupplyStatus_Type()
)
fePowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePowerSupplyStatus.setStatus("deprecated")
_FePowerSupplyIsHealthy_Type = TruthValue
_FePowerSupplyIsHealthy_Object = MibTableColumn
fePowerSupplyIsHealthy = _FePowerSupplyIsHealthy_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 3, 1, 3, 1, 3),
    _FePowerSupplyIsHealthy_Type()
)
fePowerSupplyIsHealthy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePowerSupplyIsHealthy.setStatus("deprecated")
_FeFanHealth_ObjectIdentity = ObjectIdentity
feFanHealth = _FeFanHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4)
)
_FeFanHealthTraps_ObjectIdentity = ObjectIdentity
feFanHealthTraps = _FeFanHealthTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4, 0)
)
_FeFanHealthInfo_ObjectIdentity = ObjectIdentity
feFanHealthInfo = _FeFanHealthInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4, 1)
)
_FeFanOverallStatus_Type = OctetString
_FeFanOverallStatus_Object = MibScalar
feFanOverallStatus = _FeFanOverallStatus_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4, 1, 1),
    _FeFanOverallStatus_Type()
)
feFanOverallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feFanOverallStatus.setStatus("current")
_FeFanOverallIsHealthy_Type = TruthValue
_FeFanOverallIsHealthy_Object = MibScalar
feFanOverallIsHealthy = _FeFanOverallIsHealthy_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4, 1, 2),
    _FeFanOverallIsHealthy_Type()
)
feFanOverallIsHealthy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feFanOverallIsHealthy.setStatus("current")
_FeFanStatusTable_Object = MibTable
feFanStatusTable = _FeFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4, 1, 3)
)
if mibBuilder.loadTexts:
    feFanStatusTable.setStatus("current")
_FeFanStatusEntry_Object = MibTableRow
feFanStatusEntry = _FeFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4, 1, 3, 1)
)
feFanStatusEntry.setIndexNames(
    (0, "FE-FIREEYE-MIB", "feFanIndex"),
)
if mibBuilder.loadTexts:
    feFanStatusEntry.setStatus("current")
_FeFanIndex_Type = Unsigned32
_FeFanIndex_Object = MibTableColumn
feFanIndex = _FeFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4, 1, 3, 1, 1),
    _FeFanIndex_Type()
)
feFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feFanIndex.setStatus("current")
_FeFanStatus_Type = OctetString
_FeFanStatus_Object = MibTableColumn
feFanStatus = _FeFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4, 1, 3, 1, 2),
    _FeFanStatus_Type()
)
feFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feFanStatus.setStatus("current")
_FeFanIsHealthy_Type = TruthValue
_FeFanIsHealthy_Object = MibTableColumn
feFanIsHealthy = _FeFanIsHealthy_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4, 1, 3, 1, 3),
    _FeFanIsHealthy_Type()
)
feFanIsHealthy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feFanIsHealthy.setStatus("current")
_FeFanSpeed_Type = Unsigned32
_FeFanSpeed_Object = MibTableColumn
feFanSpeed = _FeFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4, 1, 3, 1, 4),
    _FeFanSpeed_Type()
)
feFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feFanSpeed.setStatus("current")
_FeFanName_Type = OctetString
_FeFanName_Object = MibTableColumn
feFanName = _FeFanName_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4, 1, 3, 1, 5),
    _FeFanName_Type()
)
feFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feFanName.setStatus("current")
_FeApplication_ObjectIdentity = ObjectIdentity
feApplication = _FeApplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5)
)
_FeApplicationTraps_ObjectIdentity = ObjectIdentity
feApplicationTraps = _FeApplicationTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 0)
)
_FeApplicationInfo_ObjectIdentity = ObjectIdentity
feApplicationInfo = _FeApplicationInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1)
)
_FeInstalledSystemImage_Type = OctetString
_FeInstalledSystemImage_Object = MibScalar
feInstalledSystemImage = _FeInstalledSystemImage_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 1),
    _FeInstalledSystemImage_Type()
)
feInstalledSystemImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feInstalledSystemImage.setStatus("current")
_FeSystemImageVersionCurrent_Type = OctetString
_FeSystemImageVersionCurrent_Object = MibScalar
feSystemImageVersionCurrent = _FeSystemImageVersionCurrent_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 2),
    _FeSystemImageVersionCurrent_Type()
)
feSystemImageVersionCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSystemImageVersionCurrent.setStatus("current")
_FeSystemImageVersionLatest_Type = OctetString
_FeSystemImageVersionLatest_Object = MibScalar
feSystemImageVersionLatest = _FeSystemImageVersionLatest_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 3),
    _FeSystemImageVersionLatest_Type()
)
feSystemImageVersionLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSystemImageVersionLatest.setStatus("current")
_FeIsSystemImageLatest_Type = TruthValue
_FeIsSystemImageLatest_Object = MibScalar
feIsSystemImageLatest = _FeIsSystemImageLatest_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 4),
    _FeIsSystemImageLatest_Type()
)
feIsSystemImageLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feIsSystemImageLatest.setStatus("current")
_FeSecurityContentVersion_Type = OctetString
_FeSecurityContentVersion_Object = MibScalar
feSecurityContentVersion = _FeSecurityContentVersion_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 5),
    _FeSecurityContentVersion_Type()
)
feSecurityContentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSecurityContentVersion.setStatus("current")
_FeLastContentUpdatePassed_Type = TruthValue
_FeLastContentUpdatePassed_Object = MibScalar
feLastContentUpdatePassed = _FeLastContentUpdatePassed_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 6),
    _FeLastContentUpdatePassed_Type()
)
feLastContentUpdatePassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feLastContentUpdatePassed.setStatus("current")
_FeLastContentUpdateTime_Type = OctetString
_FeLastContentUpdateTime_Object = MibScalar
feLastContentUpdateTime = _FeLastContentUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 7),
    _FeLastContentUpdateTime_Type()
)
feLastContentUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feLastContentUpdateTime.setStatus("current")
_FeGIVersionTable_Object = MibTable
feGIVersionTable = _FeGIVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 8)
)
if mibBuilder.loadTexts:
    feGIVersionTable.setStatus("current")
_FeGIVersionEntry_Object = MibTableRow
feGIVersionEntry = _FeGIVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 8, 1)
)
feGIVersionEntry.setIndexNames(
    (0, "FE-FIREEYE-MIB", "feGIIndex"),
)
if mibBuilder.loadTexts:
    feGIVersionEntry.setStatus("current")
_FeGIIndex_Type = Unsigned32
_FeGIIndex_Object = MibTableColumn
feGIIndex = _FeGIIndex_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 8, 1, 1),
    _FeGIIndex_Type()
)
feGIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feGIIndex.setStatus("current")
_FeGIName_Type = OctetString
_FeGIName_Object = MibTableColumn
feGIName = _FeGIName_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 8, 1, 2),
    _FeGIName_Type()
)
feGIName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feGIName.setStatus("current")
_FeGIVersion_Type = OctetString
_FeGIVersion_Object = MibTableColumn
feGIVersion = _FeGIVersion_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 8, 1, 3),
    _FeGIVersion_Type()
)
feGIVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feGIVersion.setStatus("current")
_FeGIEnabled_Type = TruthValue
_FeGIEnabled_Object = MibTableColumn
feGIEnabled = _FeGIEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 8, 1, 4),
    _FeGIEnabled_Type()
)
feGIEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feGIEnabled.setStatus("current")
_FeGIInstallDateTime_Type = OctetString
_FeGIInstallDateTime_Object = MibTableColumn
feGIInstallDateTime = _FeGIInstallDateTime_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 8, 1, 5),
    _FeGIInstallDateTime_Type()
)
feGIInstallDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feGIInstallDateTime.setStatus("current")
_FeActiveVMs_Type = Unsigned32
_FeActiveVMs_Object = MibScalar
feActiveVMs = _FeActiveVMs_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 9),
    _FeActiveVMs_Type()
)
feActiveVMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feActiveVMs.setStatus("current")
_FeProductLicenseActive_Type = TruthValue
_FeProductLicenseActive_Object = MibScalar
feProductLicenseActive = _FeProductLicenseActive_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 10),
    _FeProductLicenseActive_Type()
)
feProductLicenseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feProductLicenseActive.setStatus("current")
_FeContentLicenseActive_Type = TruthValue
_FeContentLicenseActive_Object = MibScalar
feContentLicenseActive = _FeContentLicenseActive_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 11),
    _FeContentLicenseActive_Type()
)
feContentLicenseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feContentLicenseActive.setStatus("current")
_FeSupportLicenseActive_Type = TruthValue
_FeSupportLicenseActive_Object = MibScalar
feSupportLicenseActive = _FeSupportLicenseActive_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 12),
    _FeSupportLicenseActive_Type()
)
feSupportLicenseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSupportLicenseActive.setStatus("current")
_FeLicenseFeatureName_Type = OctetString
_FeLicenseFeatureName_Object = MibScalar
feLicenseFeatureName = _FeLicenseFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 13),
    _FeLicenseFeatureName_Type()
)
feLicenseFeatureName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feLicenseFeatureName.setStatus("current")
_FeLicenseNewActiveState_Type = TruthValue
_FeLicenseNewActiveState_Object = MibScalar
feLicenseNewActiveState = _FeLicenseNewActiveState_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 14),
    _FeLicenseNewActiveState_Type()
)
feLicenseNewActiveState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feLicenseNewActiveState.setStatus("current")
_FeLicenseOldActiveState_Type = TruthValue
_FeLicenseOldActiveState_Object = MibScalar
feLicenseOldActiveState = _FeLicenseOldActiveState_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 15),
    _FeLicenseOldActiveState_Type()
)
feLicenseOldActiveState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feLicenseOldActiveState.setStatus("current")
_FeLicenseFeatureTable_Object = MibTable
feLicenseFeatureTable = _FeLicenseFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 16)
)
if mibBuilder.loadTexts:
    feLicenseFeatureTable.setStatus("current")
_FeLicenseFeatureEntry_Object = MibTableRow
feLicenseFeatureEntry = _FeLicenseFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 16, 1)
)
feLicenseFeatureEntry.setIndexNames(
    (0, "FE-FIREEYE-MIB", "feLicenseFeature"),
)
if mibBuilder.loadTexts:
    feLicenseFeatureEntry.setStatus("current")


class _FeLicenseFeature_Type(OctetString):
    """Custom type feLicenseFeature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FeLicenseFeature_Type.__name__ = "OctetString"
_FeLicenseFeature_Object = MibTableColumn
feLicenseFeature = _FeLicenseFeature_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 16, 1, 1),
    _FeLicenseFeature_Type()
)
feLicenseFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feLicenseFeature.setStatus("current")
_FeLicenseFeatureDescr_Type = OctetString
_FeLicenseFeatureDescr_Object = MibTableColumn
feLicenseFeatureDescr = _FeLicenseFeatureDescr_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 16, 1, 2),
    _FeLicenseFeatureDescr_Type()
)
feLicenseFeatureDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feLicenseFeatureDescr.setStatus("current")
_FeLicenseActive_Type = TruthValue
_FeLicenseActive_Object = MibTableColumn
feLicenseActive = _FeLicenseActive_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 16, 1, 3),
    _FeLicenseActive_Type()
)
feLicenseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feLicenseActive.setStatus("current")
_FeLicenseExpiration_Type = DateAndTime
_FeLicenseExpiration_Object = MibTableColumn
feLicenseExpiration = _FeLicenseExpiration_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 16, 1, 4),
    _FeLicenseExpiration_Type()
)
feLicenseExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feLicenseExpiration.setStatus("current")
_FeLicenseDaysUntilExpiration_Type = Integer32
_FeLicenseDaysUntilExpiration_Object = MibTableColumn
feLicenseDaysUntilExpiration = _FeLicenseDaysUntilExpiration_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 16, 1, 5),
    _FeLicenseDaysUntilExpiration_Type()
)
feLicenseDaysUntilExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feLicenseDaysUntilExpiration.setStatus("current")
_FeTokenFailureReason_Type = OctetString
_FeTokenFailureReason_Object = MibScalar
feTokenFailureReason = _FeTokenFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 17),
    _FeTokenFailureReason_Type()
)
feTokenFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feTokenFailureReason.setStatus("current")
_FeTokenApplianceId_Type = OctetString
_FeTokenApplianceId_Object = MibScalar
feTokenApplianceId = _FeTokenApplianceId_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 18),
    _FeTokenApplianceId_Type()
)
feTokenApplianceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feTokenApplianceId.setStatus("current")
_FeTokenLeaseDuration_Type = TimeTicks
_FeTokenLeaseDuration_Object = MibScalar
feTokenLeaseDuration = _FeTokenLeaseDuration_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 19),
    _FeTokenLeaseDuration_Type()
)
feTokenLeaseDuration.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feTokenLeaseDuration.setStatus("current")
_FeTokenLeaseIsActive_Type = TruthValue
_FeTokenLeaseIsActive_Object = MibScalar
feTokenLeaseIsActive = _FeTokenLeaseIsActive_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 20),
    _FeTokenLeaseIsActive_Type()
)
feTokenLeaseIsActive.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feTokenLeaseIsActive.setStatus("current")
_FeTokenLeaseTimeRemaining_Type = TimeTicks
_FeTokenLeaseTimeRemaining_Object = MibScalar
feTokenLeaseTimeRemaining = _FeTokenLeaseTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 21),
    _FeTokenLeaseTimeRemaining_Type()
)
feTokenLeaseTimeRemaining.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feTokenLeaseTimeRemaining.setStatus("current")
_FeTokenGraceDuration_Type = TimeTicks
_FeTokenGraceDuration_Object = MibScalar
feTokenGraceDuration = _FeTokenGraceDuration_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 22),
    _FeTokenGraceDuration_Type()
)
feTokenGraceDuration.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feTokenGraceDuration.setStatus("current")
_FeTokenGraceIsActive_Type = TruthValue
_FeTokenGraceIsActive_Object = MibScalar
feTokenGraceIsActive = _FeTokenGraceIsActive_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 23),
    _FeTokenGraceIsActive_Type()
)
feTokenGraceIsActive.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feTokenGraceIsActive.setStatus("current")
_FeTokenGraceTimeRemaining_Type = TimeTicks
_FeTokenGraceTimeRemaining_Object = MibScalar
feTokenGraceTimeRemaining = _FeTokenGraceTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 24),
    _FeTokenGraceTimeRemaining_Type()
)
feTokenGraceTimeRemaining.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feTokenGraceTimeRemaining.setStatus("current")
_FeTokenLicenseExpiryTime_Type = OctetString
_FeTokenLicenseExpiryTime_Object = MibScalar
feTokenLicenseExpiryTime = _FeTokenLicenseExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 25),
    _FeTokenLicenseExpiryTime_Type()
)
feTokenLicenseExpiryTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feTokenLicenseExpiryTime.setStatus("current")
_FeTokenLicenseExpiryRequired_Type = TruthValue
_FeTokenLicenseExpiryRequired_Object = MibScalar
feTokenLicenseExpiryRequired = _FeTokenLicenseExpiryRequired_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 26),
    _FeTokenLicenseExpiryRequired_Type()
)
feTokenLicenseExpiryRequired.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feTokenLicenseExpiryRequired.setStatus("current")
_FeTokenLicenseIsActive_Type = TruthValue
_FeTokenLicenseIsActive_Object = MibScalar
feTokenLicenseIsActive = _FeTokenLicenseIsActive_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 27),
    _FeTokenLicenseIsActive_Type()
)
feTokenLicenseIsActive.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feTokenLicenseIsActive.setStatus("current")
_FeTokenLocalUuid_Type = OctetString
_FeTokenLocalUuid_Object = MibScalar
feTokenLocalUuid = _FeTokenLocalUuid_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 28),
    _FeTokenLocalUuid_Type()
)
feTokenLocalUuid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feTokenLocalUuid.setStatus("current")
_FeTokenLocalActiveDuration_Type = OctetString
_FeTokenLocalActiveDuration_Object = MibScalar
feTokenLocalActiveDuration = _FeTokenLocalActiveDuration_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 29),
    _FeTokenLocalActiveDuration_Type()
)
feTokenLocalActiveDuration.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feTokenLocalActiveDuration.setStatus("current")
_FeTokenWinnerUuid_Type = OctetString
_FeTokenWinnerUuid_Object = MibScalar
feTokenWinnerUuid = _FeTokenWinnerUuid_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 30),
    _FeTokenWinnerUuid_Type()
)
feTokenWinnerUuid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feTokenWinnerUuid.setStatus("current")
_FeTokenUuidList_Type = OctetString
_FeTokenUuidList_Object = MibScalar
feTokenUuidList = _FeTokenUuidList_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 31),
    _FeTokenUuidList_Type()
)
feTokenUuidList.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feTokenUuidList.setStatus("current")
_FeTokenUuidActiveDuration_Type = OctetString
_FeTokenUuidActiveDuration_Object = MibScalar
feTokenUuidActiveDuration = _FeTokenUuidActiveDuration_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 32),
    _FeTokenUuidActiveDuration_Type()
)
feTokenUuidActiveDuration.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feTokenUuidActiveDuration.setStatus("current")
_FeSubmission_ObjectIdentity = ObjectIdentity
feSubmission = _FeSubmission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 6)
)
_FeSubmissionInfo_ObjectIdentity = ObjectIdentity
feSubmissionInfo = _FeSubmissionInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 6, 1)
)
_FeSubmissionCountL_Type = Unsigned32
_FeSubmissionCountL_Object = MibScalar
feSubmissionCountL = _FeSubmissionCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 6, 1, 1),
    _FeSubmissionCountL_Type()
)
feSubmissionCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSubmissionCountL.setStatus("current")
_FeSubmissionCountH_Type = Unsigned32
_FeSubmissionCountH_Object = MibScalar
feSubmissionCountH = _FeSubmissionCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 6, 1, 2),
    _FeSubmissionCountH_Type()
)
feSubmissionCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSubmissionCountH.setStatus("current")
_FeSubmissionDoneCountL_Type = Unsigned32
_FeSubmissionDoneCountL_Object = MibScalar
feSubmissionDoneCountL = _FeSubmissionDoneCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 6, 1, 3),
    _FeSubmissionDoneCountL_Type()
)
feSubmissionDoneCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSubmissionDoneCountL.setStatus("current")
_FeSubmissionDoneCountH_Type = Unsigned32
_FeSubmissionDoneCountH_Object = MibScalar
feSubmissionDoneCountH = _FeSubmissionDoneCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 6, 1, 4),
    _FeSubmissionDoneCountH_Type()
)
feSubmissionDoneCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSubmissionDoneCountH.setStatus("current")
_FeSubmissionTimedOutCountL_Type = Unsigned32
_FeSubmissionTimedOutCountL_Object = MibScalar
feSubmissionTimedOutCountL = _FeSubmissionTimedOutCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 6, 1, 5),
    _FeSubmissionTimedOutCountL_Type()
)
feSubmissionTimedOutCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSubmissionTimedOutCountL.setStatus("current")
_FeSubmissionTimedOutCountH_Type = Unsigned32
_FeSubmissionTimedOutCountH_Object = MibScalar
feSubmissionTimedOutCountH = _FeSubmissionTimedOutCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 6, 1, 6),
    _FeSubmissionTimedOutCountH_Type()
)
feSubmissionTimedOutCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSubmissionTimedOutCountH.setStatus("current")
_FeSubmissionAging50to74CntL_Type = Unsigned32
_FeSubmissionAging50to74CntL_Object = MibScalar
feSubmissionAging50to74CntL = _FeSubmissionAging50to74CntL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 6, 1, 7),
    _FeSubmissionAging50to74CntL_Type()
)
feSubmissionAging50to74CntL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSubmissionAging50to74CntL.setStatus("current")
_FeSubmissionAging50to74CntH_Type = Unsigned32
_FeSubmissionAging50to74CntH_Object = MibScalar
feSubmissionAging50to74CntH = _FeSubmissionAging50to74CntH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 6, 1, 8),
    _FeSubmissionAging50to74CntH_Type()
)
feSubmissionAging50to74CntH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSubmissionAging50to74CntH.setStatus("current")
_FeSubmissionAging75to100CntL_Type = Unsigned32
_FeSubmissionAging75to100CntL_Object = MibScalar
feSubmissionAging75to100CntL = _FeSubmissionAging75to100CntL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 6, 1, 9),
    _FeSubmissionAging75to100CntL_Type()
)
feSubmissionAging75to100CntL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSubmissionAging75to100CntL.setStatus("current")
_FeSubmissionAging75to100CntH_Type = Unsigned32
_FeSubmissionAging75to100CntH_Object = MibScalar
feSubmissionAging75to100CntH = _FeSubmissionAging75to100CntH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 6, 1, 10),
    _FeSubmissionAging75to100CntH_Type()
)
feSubmissionAging75to100CntH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSubmissionAging75to100CntH.setStatus("current")
_FeCMS_ObjectIdentity = ObjectIdentity
feCMS = _FeCMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 12)
)
_FeCMSTraps_ObjectIdentity = ObjectIdentity
feCMSTraps = _FeCMSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 12, 0)
)
_FeCMSInfo_ObjectIdentity = ObjectIdentity
feCMSInfo = _FeCMSInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1)
)
_FeTotalAppliancesAttached_Type = Unsigned32
_FeTotalAppliancesAttached_Object = MibScalar
feTotalAppliancesAttached = _FeTotalAppliancesAttached_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 1),
    _FeTotalAppliancesAttached_Type()
)
feTotalAppliancesAttached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalAppliancesAttached.setStatus("current")
_FeTotalWMPSAttached_Type = Unsigned32
_FeTotalWMPSAttached_Object = MibScalar
feTotalWMPSAttached = _FeTotalWMPSAttached_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 2),
    _FeTotalWMPSAttached_Type()
)
feTotalWMPSAttached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalWMPSAttached.setStatus("current")
_FeTotalEMPSAttached_Type = Unsigned32
_FeTotalEMPSAttached_Object = MibScalar
feTotalEMPSAttached = _FeTotalEMPSAttached_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 3),
    _FeTotalEMPSAttached_Type()
)
feTotalEMPSAttached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEMPSAttached.setStatus("current")
_FeTotalFMPSAttached_Type = Unsigned32
_FeTotalFMPSAttached_Object = MibScalar
feTotalFMPSAttached = _FeTotalFMPSAttached_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 4),
    _FeTotalFMPSAttached_Type()
)
feTotalFMPSAttached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalFMPSAttached.setStatus("current")
_FeTotalMASAttached_Type = Unsigned32
_FeTotalMASAttached_Object = MibScalar
feTotalMASAttached = _FeTotalMASAttached_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 5),
    _FeTotalMASAttached_Type()
)
feTotalMASAttached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMASAttached.setStatus("current")
_FeCMSApplianceTable_Object = MibTable
feCMSApplianceTable = _FeCMSApplianceTable_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 6)
)
if mibBuilder.loadTexts:
    feCMSApplianceTable.setStatus("current")
_FeCMSApplianceEntry_Object = MibTableRow
feCMSApplianceEntry = _FeCMSApplianceEntry_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 6, 1)
)
feCMSApplianceEntry.setIndexNames(
    (0, "FE-FIREEYE-MIB", "feCMSApplianceIndex"),
)
if mibBuilder.loadTexts:
    feCMSApplianceEntry.setStatus("current")
_FeCMSApplianceIndex_Type = Unsigned32
_FeCMSApplianceIndex_Object = MibTableColumn
feCMSApplianceIndex = _FeCMSApplianceIndex_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 6, 1, 1),
    _FeCMSApplianceIndex_Type()
)
feCMSApplianceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feCMSApplianceIndex.setStatus("current")
_FeCMSApplianceName_Type = OctetString
_FeCMSApplianceName_Object = MibTableColumn
feCMSApplianceName = _FeCMSApplianceName_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 6, 1, 2),
    _FeCMSApplianceName_Type()
)
feCMSApplianceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feCMSApplianceName.setStatus("current")
_FeCMSApplianceDiskSpacePassed_Type = TruthValue
_FeCMSApplianceDiskSpacePassed_Object = MibTableColumn
feCMSApplianceDiskSpacePassed = _FeCMSApplianceDiskSpacePassed_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 6, 1, 3),
    _FeCMSApplianceDiskSpacePassed_Type()
)
feCMSApplianceDiskSpacePassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feCMSApplianceDiskSpacePassed.setStatus("current")
_FeCMSApplianceFanPassed_Type = TruthValue
_FeCMSApplianceFanPassed_Object = MibTableColumn
feCMSApplianceFanPassed = _FeCMSApplianceFanPassed_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 6, 1, 4),
    _FeCMSApplianceFanPassed_Type()
)
feCMSApplianceFanPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feCMSApplianceFanPassed.setStatus("current")
_FeCMSAppliancePowerSupplyPassed_Type = TruthValue
_FeCMSAppliancePowerSupplyPassed_Object = MibTableColumn
feCMSAppliancePowerSupplyPassed = _FeCMSAppliancePowerSupplyPassed_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 6, 1, 5),
    _FeCMSAppliancePowerSupplyPassed_Type()
)
feCMSAppliancePowerSupplyPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feCMSAppliancePowerSupplyPassed.setStatus("current")
_FeCMSApplianceRaidPassed_Type = TruthValue
_FeCMSApplianceRaidPassed_Object = MibTableColumn
feCMSApplianceRaidPassed = _FeCMSApplianceRaidPassed_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 6, 1, 6),
    _FeCMSApplianceRaidPassed_Type()
)
feCMSApplianceRaidPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feCMSApplianceRaidPassed.setStatus("current")
_FeCMSApplianceTemperaturePassed_Type = TruthValue
_FeCMSApplianceTemperaturePassed_Object = MibTableColumn
feCMSApplianceTemperaturePassed = _FeCMSApplianceTemperaturePassed_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 6, 1, 7),
    _FeCMSApplianceTemperaturePassed_Type()
)
feCMSApplianceTemperaturePassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feCMSApplianceTemperaturePassed.setStatus("current")
_FeCMSHANxHealthFailureName_Type = OctetString
_FeCMSHANxHealthFailureName_Object = MibScalar
feCMSHANxHealthFailureName = _FeCMSHANxHealthFailureName_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 7),
    _FeCMSHANxHealthFailureName_Type()
)
feCMSHANxHealthFailureName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feCMSHANxHealthFailureName.setStatus("current")
_FeCMSHANxHealthFailureType_Type = OctetString
_FeCMSHANxHealthFailureType_Object = MibScalar
feCMSHANxHealthFailureType = _FeCMSHANxHealthFailureType_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 8),
    _FeCMSHANxHealthFailureType_Type()
)
feCMSHANxHealthFailureType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feCMSHANxHealthFailureType.setStatus("current")
_FeCMSHANxHealthFailureNx1_Type = OctetString
_FeCMSHANxHealthFailureNx1_Object = MibScalar
feCMSHANxHealthFailureNx1 = _FeCMSHANxHealthFailureNx1_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 9),
    _FeCMSHANxHealthFailureNx1_Type()
)
feCMSHANxHealthFailureNx1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feCMSHANxHealthFailureNx1.setStatus("current")
_FeCMSHANxHealthFailureNx2_Type = OctetString
_FeCMSHANxHealthFailureNx2_Object = MibScalar
feCMSHANxHealthFailureNx2 = _FeCMSHANxHealthFailureNx2_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 10),
    _FeCMSHANxHealthFailureNx2_Type()
)
feCMSHANxHealthFailureNx2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feCMSHANxHealthFailureNx2.setStatus("current")
_FeCMSHANxHealthFailureReason_Type = OctetString
_FeCMSHANxHealthFailureReason_Object = MibScalar
feCMSHANxHealthFailureReason = _FeCMSHANxHealthFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 11),
    _FeCMSHANxHealthFailureReason_Type()
)
feCMSHANxHealthFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feCMSHANxHealthFailureReason.setStatus("current")
_FeCMSHANxHealthFailureDesc_Type = OctetString
_FeCMSHANxHealthFailureDesc_Object = MibScalar
feCMSHANxHealthFailureDesc = _FeCMSHANxHealthFailureDesc_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 12),
    _FeCMSHANxHealthFailureDesc_Type()
)
feCMSHANxHealthFailureDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feCMSHANxHealthFailureDesc.setStatus("current")
_FeMVXClusterName_Type = OctetString
_FeMVXClusterName_Object = MibScalar
feMVXClusterName = _FeMVXClusterName_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 13),
    _FeMVXClusterName_Type()
)
feMVXClusterName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feMVXClusterName.setStatus("current")
_FeMVXClusterStateChangeDesc_Type = OctetString
_FeMVXClusterStateChangeDesc_Object = MibScalar
feMVXClusterStateChangeDesc = _FeMVXClusterStateChangeDesc_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 14),
    _FeMVXClusterStateChangeDesc_Type()
)
feMVXClusterStateChangeDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feMVXClusterStateChangeDesc.setStatus("current")
_FeMVXClusterUtilExceedAlarmId_Type = OctetString
_FeMVXClusterUtilExceedAlarmId_Object = MibScalar
feMVXClusterUtilExceedAlarmId = _FeMVXClusterUtilExceedAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 15),
    _FeMVXClusterUtilExceedAlarmId_Type()
)
feMVXClusterUtilExceedAlarmId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feMVXClusterUtilExceedAlarmId.setStatus("current")
_FeMVXClusterUtilExceedDataValue_Type = OctetString
_FeMVXClusterUtilExceedDataValue_Object = MibScalar
feMVXClusterUtilExceedDataValue = _FeMVXClusterUtilExceedDataValue_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 16),
    _FeMVXClusterUtilExceedDataValue_Type()
)
feMVXClusterUtilExceedDataValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feMVXClusterUtilExceedDataValue.setStatus("current")
_FeEMPS_ObjectIdentity = ObjectIdentity
feEMPS = _FeEMPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 13)
)
_FeEMPSTraps_ObjectIdentity = ObjectIdentity
feEMPSTraps = _FeEMPSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 13, 0)
)
_FeEMPSInfo_ObjectIdentity = ObjectIdentity
feEMPSInfo = _FeEMPSInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1)
)
_FeTotalEmailCount_Type = Counter64
_FeTotalEmailCount_Object = MibScalar
feTotalEmailCount = _FeTotalEmailCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 1),
    _FeTotalEmailCount_Type()
)
feTotalEmailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailCount.setStatus("current")
_FeTotalEmailCountH_Type = Counter32
_FeTotalEmailCountH_Object = MibScalar
feTotalEmailCountH = _FeTotalEmailCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 2),
    _FeTotalEmailCountH_Type()
)
feTotalEmailCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailCountH.setStatus("current")
_FeTotalEmailCountL_Type = Counter32
_FeTotalEmailCountL_Object = MibScalar
feTotalEmailCountL = _FeTotalEmailCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 3),
    _FeTotalEmailCountL_Type()
)
feTotalEmailCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailCountL.setStatus("current")
_FeInfectedEmailCount_Type = Counter64
_FeInfectedEmailCount_Object = MibScalar
feInfectedEmailCount = _FeInfectedEmailCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 4),
    _FeInfectedEmailCount_Type()
)
feInfectedEmailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feInfectedEmailCount.setStatus("current")
_FeInfectedEmailCountH_Type = Counter32
_FeInfectedEmailCountH_Object = MibScalar
feInfectedEmailCountH = _FeInfectedEmailCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 5),
    _FeInfectedEmailCountH_Type()
)
feInfectedEmailCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feInfectedEmailCountH.setStatus("current")
_FeInfectedEmailCountL_Type = Counter32
_FeInfectedEmailCountL_Object = MibScalar
feInfectedEmailCountL = _FeInfectedEmailCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 6),
    _FeInfectedEmailCountL_Type()
)
feInfectedEmailCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feInfectedEmailCountL.setStatus("current")
_FeAnalyzedEmailCount_Type = Counter64
_FeAnalyzedEmailCount_Object = MibScalar
feAnalyzedEmailCount = _FeAnalyzedEmailCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 7),
    _FeAnalyzedEmailCount_Type()
)
feAnalyzedEmailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feAnalyzedEmailCount.setStatus("current")
_FeAnalyzedEmailCountH_Type = Counter32
_FeAnalyzedEmailCountH_Object = MibScalar
feAnalyzedEmailCountH = _FeAnalyzedEmailCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 8),
    _FeAnalyzedEmailCountH_Type()
)
feAnalyzedEmailCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feAnalyzedEmailCountH.setStatus("current")
_FeAnalyzedEmailCountL_Type = Counter32
_FeAnalyzedEmailCountL_Object = MibScalar
feAnalyzedEmailCountL = _FeAnalyzedEmailCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 9),
    _FeAnalyzedEmailCountL_Type()
)
feAnalyzedEmailCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feAnalyzedEmailCountL.setStatus("current")
_FeTotalUrlCount_Type = Counter64
_FeTotalUrlCount_Object = MibScalar
feTotalUrlCount = _FeTotalUrlCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 10),
    _FeTotalUrlCount_Type()
)
feTotalUrlCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalUrlCount.setStatus("current")
_FeTotalUrlCountH_Type = Counter32
_FeTotalUrlCountH_Object = MibScalar
feTotalUrlCountH = _FeTotalUrlCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 11),
    _FeTotalUrlCountH_Type()
)
feTotalUrlCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalUrlCountH.setStatus("current")
_FeTotalUrlCountL_Type = Counter32
_FeTotalUrlCountL_Object = MibScalar
feTotalUrlCountL = _FeTotalUrlCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 12),
    _FeTotalUrlCountL_Type()
)
feTotalUrlCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalUrlCountL.setStatus("current")
_FeInfectedUrlCount_Type = Counter64
_FeInfectedUrlCount_Object = MibScalar
feInfectedUrlCount = _FeInfectedUrlCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 13),
    _FeInfectedUrlCount_Type()
)
feInfectedUrlCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feInfectedUrlCount.setStatus("current")
_FeInfectedUrlCountH_Type = Counter32
_FeInfectedUrlCountH_Object = MibScalar
feInfectedUrlCountH = _FeInfectedUrlCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 14),
    _FeInfectedUrlCountH_Type()
)
feInfectedUrlCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feInfectedUrlCountH.setStatus("current")
_FeInfectedUrlCountL_Type = Counter32
_FeInfectedUrlCountL_Object = MibScalar
feInfectedUrlCountL = _FeInfectedUrlCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 15),
    _FeInfectedUrlCountL_Type()
)
feInfectedUrlCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feInfectedUrlCountL.setStatus("current")
_FeAnalyzedUrlCount_Type = Counter64
_FeAnalyzedUrlCount_Object = MibScalar
feAnalyzedUrlCount = _FeAnalyzedUrlCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 16),
    _FeAnalyzedUrlCount_Type()
)
feAnalyzedUrlCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feAnalyzedUrlCount.setStatus("current")
_FeAnalyzedUrlCountH_Type = Counter32
_FeAnalyzedUrlCountH_Object = MibScalar
feAnalyzedUrlCountH = _FeAnalyzedUrlCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 17),
    _FeAnalyzedUrlCountH_Type()
)
feAnalyzedUrlCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feAnalyzedUrlCountH.setStatus("current")
_FeAnalyzedUrlCountL_Type = Counter32
_FeAnalyzedUrlCountL_Object = MibScalar
feAnalyzedUrlCountL = _FeAnalyzedUrlCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 18),
    _FeAnalyzedUrlCountL_Type()
)
feAnalyzedUrlCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feAnalyzedUrlCountL.setStatus("current")
_FeTotalAttachmentCount_Type = Counter64
_FeTotalAttachmentCount_Object = MibScalar
feTotalAttachmentCount = _FeTotalAttachmentCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 19),
    _FeTotalAttachmentCount_Type()
)
feTotalAttachmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalAttachmentCount.setStatus("current")
_FeTotalAttachmentCountH_Type = Counter32
_FeTotalAttachmentCountH_Object = MibScalar
feTotalAttachmentCountH = _FeTotalAttachmentCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 20),
    _FeTotalAttachmentCountH_Type()
)
feTotalAttachmentCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalAttachmentCountH.setStatus("current")
_FeTotalAttachmentCountL_Type = Counter32
_FeTotalAttachmentCountL_Object = MibScalar
feTotalAttachmentCountL = _FeTotalAttachmentCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 21),
    _FeTotalAttachmentCountL_Type()
)
feTotalAttachmentCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalAttachmentCountL.setStatus("current")
_FeInfectedAttachmentCount_Type = Counter64
_FeInfectedAttachmentCount_Object = MibScalar
feInfectedAttachmentCount = _FeInfectedAttachmentCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 22),
    _FeInfectedAttachmentCount_Type()
)
feInfectedAttachmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feInfectedAttachmentCount.setStatus("current")
_FeInfectedAttachmentCountH_Type = Counter32
_FeInfectedAttachmentCountH_Object = MibScalar
feInfectedAttachmentCountH = _FeInfectedAttachmentCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 23),
    _FeInfectedAttachmentCountH_Type()
)
feInfectedAttachmentCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feInfectedAttachmentCountH.setStatus("current")
_FeInfectedAttachmentCountL_Type = Counter32
_FeInfectedAttachmentCountL_Object = MibScalar
feInfectedAttachmentCountL = _FeInfectedAttachmentCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 24),
    _FeInfectedAttachmentCountL_Type()
)
feInfectedAttachmentCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feInfectedAttachmentCountL.setStatus("current")
_FeAnalyzedAttachmentCount_Type = Counter64
_FeAnalyzedAttachmentCount_Object = MibScalar
feAnalyzedAttachmentCount = _FeAnalyzedAttachmentCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 25),
    _FeAnalyzedAttachmentCount_Type()
)
feAnalyzedAttachmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feAnalyzedAttachmentCount.setStatus("current")
_FeAnalyzedAttachmentCountH_Type = Counter32
_FeAnalyzedAttachmentCountH_Object = MibScalar
feAnalyzedAttachmentCountH = _FeAnalyzedAttachmentCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 26),
    _FeAnalyzedAttachmentCountH_Type()
)
feAnalyzedAttachmentCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feAnalyzedAttachmentCountH.setStatus("current")
_FeAnalyzedAttachmentCountL_Type = Counter32
_FeAnalyzedAttachmentCountL_Object = MibScalar
feAnalyzedAttachmentCountL = _FeAnalyzedAttachmentCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 27),
    _FeAnalyzedAttachmentCountL_Type()
)
feAnalyzedAttachmentCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feAnalyzedAttachmentCountL.setStatus("current")
_FeTotalEmailHasAttachment_Type = Counter64
_FeTotalEmailHasAttachment_Object = MibScalar
feTotalEmailHasAttachment = _FeTotalEmailHasAttachment_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 28),
    _FeTotalEmailHasAttachment_Type()
)
feTotalEmailHasAttachment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailHasAttachment.setStatus("current")
_FeTotalEmailHasAttachmentH_Type = Counter32
_FeTotalEmailHasAttachmentH_Object = MibScalar
feTotalEmailHasAttachmentH = _FeTotalEmailHasAttachmentH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 29),
    _FeTotalEmailHasAttachmentH_Type()
)
feTotalEmailHasAttachmentH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailHasAttachmentH.setStatus("current")
_FeTotalEmailHasAttachmentL_Type = Counter32
_FeTotalEmailHasAttachmentL_Object = MibScalar
feTotalEmailHasAttachmentL = _FeTotalEmailHasAttachmentL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 30),
    _FeTotalEmailHasAttachmentL_Type()
)
feTotalEmailHasAttachmentL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailHasAttachmentL.setStatus("current")
_FeTotalEmailHasUrl_Type = Counter64
_FeTotalEmailHasUrl_Object = MibScalar
feTotalEmailHasUrl = _FeTotalEmailHasUrl_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 31),
    _FeTotalEmailHasUrl_Type()
)
feTotalEmailHasUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailHasUrl.setStatus("current")
_FeTotalEmailHasUrlH_Type = Counter32
_FeTotalEmailHasUrlH_Object = MibScalar
feTotalEmailHasUrlH = _FeTotalEmailHasUrlH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 32),
    _FeTotalEmailHasUrlH_Type()
)
feTotalEmailHasUrlH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailHasUrlH.setStatus("current")
_FeTotalEmailHasUrlL_Type = Counter32
_FeTotalEmailHasUrlL_Object = MibScalar
feTotalEmailHasUrlL = _FeTotalEmailHasUrlL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 33),
    _FeTotalEmailHasUrlL_Type()
)
feTotalEmailHasUrlL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailHasUrlL.setStatus("current")
_FeTotalEmailHasBadAttachment_Type = Counter64
_FeTotalEmailHasBadAttachment_Object = MibScalar
feTotalEmailHasBadAttachment = _FeTotalEmailHasBadAttachment_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 34),
    _FeTotalEmailHasBadAttachment_Type()
)
feTotalEmailHasBadAttachment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailHasBadAttachment.setStatus("current")
_FeTotalEmailHasBadAttachmentH_Type = Counter32
_FeTotalEmailHasBadAttachmentH_Object = MibScalar
feTotalEmailHasBadAttachmentH = _FeTotalEmailHasBadAttachmentH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 35),
    _FeTotalEmailHasBadAttachmentH_Type()
)
feTotalEmailHasBadAttachmentH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailHasBadAttachmentH.setStatus("current")
_FeTotalEmailHasBadAttachmentL_Type = Counter32
_FeTotalEmailHasBadAttachmentL_Object = MibScalar
feTotalEmailHasBadAttachmentL = _FeTotalEmailHasBadAttachmentL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 36),
    _FeTotalEmailHasBadAttachmentL_Type()
)
feTotalEmailHasBadAttachmentL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailHasBadAttachmentL.setStatus("current")
_FeTotalEmailHasBadUrl_Type = Counter64
_FeTotalEmailHasBadUrl_Object = MibScalar
feTotalEmailHasBadUrl = _FeTotalEmailHasBadUrl_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 37),
    _FeTotalEmailHasBadUrl_Type()
)
feTotalEmailHasBadUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailHasBadUrl.setStatus("current")
_FeTotalEmailHasBadUrlH_Type = Counter32
_FeTotalEmailHasBadUrlH_Object = MibScalar
feTotalEmailHasBadUrlH = _FeTotalEmailHasBadUrlH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 38),
    _FeTotalEmailHasBadUrlH_Type()
)
feTotalEmailHasBadUrlH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailHasBadUrlH.setStatus("current")
_FeTotalEmailHasBadUrlL_Type = Counter32
_FeTotalEmailHasBadUrlL_Object = MibScalar
feTotalEmailHasBadUrlL = _FeTotalEmailHasBadUrlL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 39),
    _FeTotalEmailHasBadUrlL_Type()
)
feTotalEmailHasBadUrlL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailHasBadUrlL.setStatus("current")


class _FeeQuarantineUsage_Type(Unsigned32):
    """Custom type feeQuarantineUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FeeQuarantineUsage_Type.__name__ = "Unsigned32"
_FeeQuarantineUsage_Object = MibScalar
feeQuarantineUsage = _FeeQuarantineUsage_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 40),
    _FeeQuarantineUsage_Type()
)
feeQuarantineUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feeQuarantineUsage.setStatus("current")
_FeBypassEmailCount_Type = Counter64
_FeBypassEmailCount_Object = MibScalar
feBypassEmailCount = _FeBypassEmailCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 41),
    _FeBypassEmailCount_Type()
)
feBypassEmailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feBypassEmailCount.setStatus("current")
_FeBypassEmailCountH_Type = Counter32
_FeBypassEmailCountH_Object = MibScalar
feBypassEmailCountH = _FeBypassEmailCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 42),
    _FeBypassEmailCountH_Type()
)
feBypassEmailCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feBypassEmailCountH.setStatus("current")
_FeBypassEmailCountL_Type = Counter32
_FeBypassEmailCountL_Object = MibScalar
feBypassEmailCountL = _FeBypassEmailCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 43),
    _FeBypassEmailCountL_Type()
)
feBypassEmailCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feBypassEmailCountL.setStatus("current")
_FeDeferredEmailCount_Type = Unsigned32
_FeDeferredEmailCount_Object = MibScalar
feDeferredEmailCount = _FeDeferredEmailCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 44),
    _FeDeferredEmailCount_Type()
)
feDeferredEmailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feDeferredEmailCount.setStatus("current")
_FeHoldQueueEmailCount_Type = Unsigned32
_FeHoldQueueEmailCount_Object = MibScalar
feHoldQueueEmailCount = _FeHoldQueueEmailCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 45),
    _FeHoldQueueEmailCount_Type()
)
feHoldQueueEmailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feHoldQueueEmailCount.setStatus("current")
_FeOpenSmtpConnections_Type = Unsigned32
_FeOpenSmtpConnections_Object = MibScalar
feOpenSmtpConnections = _FeOpenSmtpConnections_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 46),
    _FeOpenSmtpConnections_Type()
)
feOpenSmtpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feOpenSmtpConnections.setStatus("current")
_FeIncomingEmailCount_Type = Unsigned32
_FeIncomingEmailCount_Object = MibScalar
feIncomingEmailCount = _FeIncomingEmailCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 47),
    _FeIncomingEmailCount_Type()
)
feIncomingEmailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feIncomingEmailCount.setStatus("current")
_FeActiveEmailCount_Type = Unsigned32
_FeActiveEmailCount_Object = MibScalar
feActiveEmailCount = _FeActiveEmailCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 48),
    _FeActiveEmailCount_Type()
)
feActiveEmailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feActiveEmailCount.setStatus("current")
_FeDropEmailCount_Type = Unsigned32
_FeDropEmailCount_Object = MibScalar
feDropEmailCount = _FeDropEmailCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 49),
    _FeDropEmailCount_Type()
)
feDropEmailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feDropEmailCount.setStatus("current")
_FeSamplingEmailStartTime_Type = OctetString
_FeSamplingEmailStartTime_Object = MibScalar
feSamplingEmailStartTime = _FeSamplingEmailStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 50),
    _FeSamplingEmailStartTime_Type()
)
feSamplingEmailStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSamplingEmailStartTime.setStatus("current")
_FeSamplingEmailEndTime_Type = OctetString
_FeSamplingEmailEndTime_Object = MibScalar
feSamplingEmailEndTime = _FeSamplingEmailEndTime_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 51),
    _FeSamplingEmailEndTime_Type()
)
feSamplingEmailEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSamplingEmailEndTime.setStatus("current")
_FeSamplingEmailReceivedRate_Type = Unsigned32
_FeSamplingEmailReceivedRate_Object = MibScalar
feSamplingEmailReceivedRate = _FeSamplingEmailReceivedRate_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 52),
    _FeSamplingEmailReceivedRate_Type()
)
feSamplingEmailReceivedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSamplingEmailReceivedRate.setStatus("current")
_FeWMPS_ObjectIdentity = ObjectIdentity
feWMPS = _FeWMPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 14)
)
_FeWMPSTraps_ObjectIdentity = ObjectIdentity
feWMPSTraps = _FeWMPSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 14, 0)
)
_FeWMPSInfo_ObjectIdentity = ObjectIdentity
feWMPSInfo = _FeWMPSInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1)
)
_FeDeploymentCheckStatus_Type = OctetString
_FeDeploymentCheckStatus_Object = MibScalar
feDeploymentCheckStatus = _FeDeploymentCheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 1),
    _FeDeploymentCheckStatus_Type()
)
feDeploymentCheckStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feDeploymentCheckStatus.setStatus("current")
_FeDeploymentCheckIsHealthy_Type = Unsigned32
_FeDeploymentCheckIsHealthy_Object = MibScalar
feDeploymentCheckIsHealthy = _FeDeploymentCheckIsHealthy_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 2),
    _FeDeploymentCheckIsHealthy_Type()
)
feDeploymentCheckIsHealthy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feDeploymentCheckIsHealthy.setStatus("current")
_FeDeploymentCheckMessage_Type = OctetString
_FeDeploymentCheckMessage_Object = MibScalar
feDeploymentCheckMessage = _FeDeploymentCheckMessage_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 3),
    _FeDeploymentCheckMessage_Type()
)
feDeploymentCheckMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feDeploymentCheckMessage.setStatus("current")
_FeDeploymentCheckStartTime_Type = OctetString
_FeDeploymentCheckStartTime_Object = MibScalar
feDeploymentCheckStartTime = _FeDeploymentCheckStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 4),
    _FeDeploymentCheckStartTime_Type()
)
feDeploymentCheckStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feDeploymentCheckStartTime.setStatus("current")
_FeDeploymentCheckEndTime_Type = OctetString
_FeDeploymentCheckEndTime_Object = MibScalar
feDeploymentCheckEndTime = _FeDeploymentCheckEndTime_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 5),
    _FeDeploymentCheckEndTime_Type()
)
feDeploymentCheckEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feDeploymentCheckEndTime.setStatus("current")
_FeDeploymentCheckDataSize_Type = CounterBasedGauge64
_FeDeploymentCheckDataSize_Object = MibScalar
feDeploymentCheckDataSize = _FeDeploymentCheckDataSize_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 6),
    _FeDeploymentCheckDataSize_Type()
)
feDeploymentCheckDataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feDeploymentCheckDataSize.setStatus("current")
_FeDeploymentCheckPktCount_Type = CounterBasedGauge64
_FeDeploymentCheckPktCount_Object = MibScalar
feDeploymentCheckPktCount = _FeDeploymentCheckPktCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 7),
    _FeDeploymentCheckPktCount_Type()
)
feDeploymentCheckPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feDeploymentCheckPktCount.setStatus("current")
_FeDeploymentCheckReTransPktCount_Type = CounterBasedGauge64
_FeDeploymentCheckReTransPktCount_Object = MibScalar
feDeploymentCheckReTransPktCount = _FeDeploymentCheckReTransPktCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 8),
    _FeDeploymentCheckReTransPktCount_Type()
)
feDeploymentCheckReTransPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feDeploymentCheckReTransPktCount.setStatus("current")
_FeDeploymentCheckDupAckPktCount_Type = CounterBasedGauge64
_FeDeploymentCheckDupAckPktCount_Object = MibScalar
feDeploymentCheckDupAckPktCount = _FeDeploymentCheckDupAckPktCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 9),
    _FeDeploymentCheckDupAckPktCount_Type()
)
feDeploymentCheckDupAckPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feDeploymentCheckDupAckPktCount.setStatus("current")
_FeDeploymentCheckOOOPktCount_Type = CounterBasedGauge64
_FeDeploymentCheckOOOPktCount_Object = MibScalar
feDeploymentCheckOOOPktCount = _FeDeploymentCheckOOOPktCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 10),
    _FeDeploymentCheckOOOPktCount_Type()
)
feDeploymentCheckOOOPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feDeploymentCheckOOOPktCount.setStatus("current")
_FeDeploymentCheckAckUsnPktCount_Type = CounterBasedGauge64
_FeDeploymentCheckAckUsnPktCount_Object = MibScalar
feDeploymentCheckAckUsnPktCount = _FeDeploymentCheckAckUsnPktCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 11),
    _FeDeploymentCheckAckUsnPktCount_Type()
)
feDeploymentCheckAckUsnPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feDeploymentCheckAckUsnPktCount.setStatus("current")
_FeDeploymentCheckPSegNCPktCount_Type = CounterBasedGauge64
_FeDeploymentCheckPSegNCPktCount_Object = MibScalar
feDeploymentCheckPSegNCPktCount = _FeDeploymentCheckPSegNCPktCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 12),
    _FeDeploymentCheckPSegNCPktCount_Type()
)
feDeploymentCheckPSegNCPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feDeploymentCheckPSegNCPktCount.setStatus("current")
_FeDeploymentCheckMFormedPktCount_Type = CounterBasedGauge64
_FeDeploymentCheckMFormedPktCount_Object = MibScalar
feDeploymentCheckMFormedPktCount = _FeDeploymentCheckMFormedPktCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 13),
    _FeDeploymentCheckMFormedPktCount_Type()
)
feDeploymentCheckMFormedPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feDeploymentCheckMFormedPktCount.setStatus("current")
_FeDeploymentCheckStreamCount_Type = CounterBasedGauge64
_FeDeploymentCheckStreamCount_Object = MibScalar
feDeploymentCheckStreamCount = _FeDeploymentCheckStreamCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 14),
    _FeDeploymentCheckStreamCount_Type()
)
feDeploymentCheckStreamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feDeploymentCheckStreamCount.setStatus("current")
_FeDeploymentCheckAsymStreamCount_Type = CounterBasedGauge64
_FeDeploymentCheckAsymStreamCount_Object = MibScalar
feDeploymentCheckAsymStreamCount = _FeDeploymentCheckAsymStreamCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 15),
    _FeDeploymentCheckAsymStreamCount_Type()
)
feDeploymentCheckAsymStreamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feDeploymentCheckAsymStreamCount.setStatus("current")
_FeWMPSDetection_ObjectIdentity = ObjectIdentity
feWMPSDetection = _FeWMPSDetection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16)
)
_FeWMPSDetectionStatsTable_Object = MibTable
feWMPSDetectionStatsTable = _FeWMPSDetectionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 1)
)
if mibBuilder.loadTexts:
    feWMPSDetectionStatsTable.setStatus("current")
_FeWMPSDetectionStatsEntry_Object = MibTableRow
feWMPSDetectionStatsEntry = _FeWMPSDetectionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 1, 1)
)
feWMPSDetectionStatsEntry.setIndexNames(
    (0, "FE-FIREEYE-MIB", "feWMPSDetectionStatsIndex"),
)
if mibBuilder.loadTexts:
    feWMPSDetectionStatsEntry.setStatus("current")


class _FeWMPSDetectionStatsTimeSpan_Type(OctetString):
    """Custom type feWMPSDetectionStatsTimeSpan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FeWMPSDetectionStatsTimeSpan_Type.__name__ = "OctetString"
_FeWMPSDetectionStatsTimeSpan_Object = MibTableColumn
feWMPSDetectionStatsTimeSpan = _FeWMPSDetectionStatsTimeSpan_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 1, 1, 1),
    _FeWMPSDetectionStatsTimeSpan_Type()
)
feWMPSDetectionStatsTimeSpan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSDetectionStatsTimeSpan.setStatus("current")
_FeWMPSAPTAttackCount_Type = Counter64
_FeWMPSAPTAttackCount_Object = MibTableColumn
feWMPSAPTAttackCount = _FeWMPSAPTAttackCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 1, 1, 2),
    _FeWMPSAPTAttackCount_Type()
)
feWMPSAPTAttackCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSAPTAttackCount.setStatus("current")
_FeWMPSAPTAttackCountH_Type = Counter32
_FeWMPSAPTAttackCountH_Object = MibTableColumn
feWMPSAPTAttackCountH = _FeWMPSAPTAttackCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 1, 1, 3),
    _FeWMPSAPTAttackCountH_Type()
)
feWMPSAPTAttackCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSAPTAttackCountH.setStatus("current")
_FeWMPSAPTAttackCountL_Type = Counter32
_FeWMPSAPTAttackCountL_Object = MibTableColumn
feWMPSAPTAttackCountL = _FeWMPSAPTAttackCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 1, 1, 4),
    _FeWMPSAPTAttackCountL_Type()
)
feWMPSAPTAttackCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSAPTAttackCountL.setStatus("current")
_FeWMPSNewGlobalThreatCount_Type = Counter64
_FeWMPSNewGlobalThreatCount_Object = MibTableColumn
feWMPSNewGlobalThreatCount = _FeWMPSNewGlobalThreatCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 1, 1, 5),
    _FeWMPSNewGlobalThreatCount_Type()
)
feWMPSNewGlobalThreatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSNewGlobalThreatCount.setStatus("current")
_FeWMPSNewGlobalThreatCountH_Type = Counter32
_FeWMPSNewGlobalThreatCountH_Object = MibTableColumn
feWMPSNewGlobalThreatCountH = _FeWMPSNewGlobalThreatCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 1, 1, 6),
    _FeWMPSNewGlobalThreatCountH_Type()
)
feWMPSNewGlobalThreatCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSNewGlobalThreatCountH.setStatus("current")
_FeWMPSNewGlobalThreatCountL_Type = Counter32
_FeWMPSNewGlobalThreatCountL_Object = MibTableColumn
feWMPSNewGlobalThreatCountL = _FeWMPSNewGlobalThreatCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 1, 1, 7),
    _FeWMPSNewGlobalThreatCountL_Type()
)
feWMPSNewGlobalThreatCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSNewGlobalThreatCountL.setStatus("current")
_FeWMPSInfectedHostCount_Type = Counter64
_FeWMPSInfectedHostCount_Object = MibTableColumn
feWMPSInfectedHostCount = _FeWMPSInfectedHostCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 1, 1, 8),
    _FeWMPSInfectedHostCount_Type()
)
feWMPSInfectedHostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSInfectedHostCount.setStatus("current")
_FeWMPSInfectedHostCountH_Type = Counter32
_FeWMPSInfectedHostCountH_Object = MibTableColumn
feWMPSInfectedHostCountH = _FeWMPSInfectedHostCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 1, 1, 9),
    _FeWMPSInfectedHostCountH_Type()
)
feWMPSInfectedHostCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSInfectedHostCountH.setStatus("current")
_FeWMPSInfectedHostCountL_Type = Counter32
_FeWMPSInfectedHostCountL_Object = MibTableColumn
feWMPSInfectedHostCountL = _FeWMPSInfectedHostCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 1, 1, 10),
    _FeWMPSInfectedHostCountL_Type()
)
feWMPSInfectedHostCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSInfectedHostCountL.setStatus("current")
_FeWMPSObjectsAnalyzedCount_Type = Counter64
_FeWMPSObjectsAnalyzedCount_Object = MibTableColumn
feWMPSObjectsAnalyzedCount = _FeWMPSObjectsAnalyzedCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 1, 1, 11),
    _FeWMPSObjectsAnalyzedCount_Type()
)
feWMPSObjectsAnalyzedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSObjectsAnalyzedCount.setStatus("current")
_FeWMPSObjectsAnalyzedCountH_Type = Counter32
_FeWMPSObjectsAnalyzedCountH_Object = MibTableColumn
feWMPSObjectsAnalyzedCountH = _FeWMPSObjectsAnalyzedCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 1, 1, 12),
    _FeWMPSObjectsAnalyzedCountH_Type()
)
feWMPSObjectsAnalyzedCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSObjectsAnalyzedCountH.setStatus("current")
_FeWMPSObjectsAnalyzedCountL_Type = Counter32
_FeWMPSObjectsAnalyzedCountL_Object = MibTableColumn
feWMPSObjectsAnalyzedCountL = _FeWMPSObjectsAnalyzedCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 1, 1, 13),
    _FeWMPSObjectsAnalyzedCountL_Type()
)
feWMPSObjectsAnalyzedCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSObjectsAnalyzedCountL.setStatus("current")
_FeWMPSURLsAnalyzedCount_Type = Counter64
_FeWMPSURLsAnalyzedCount_Object = MibTableColumn
feWMPSURLsAnalyzedCount = _FeWMPSURLsAnalyzedCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 1, 1, 14),
    _FeWMPSURLsAnalyzedCount_Type()
)
feWMPSURLsAnalyzedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSURLsAnalyzedCount.setStatus("current")
_FeWMPSURLsAnalyzedCountH_Type = Counter32
_FeWMPSURLsAnalyzedCountH_Object = MibTableColumn
feWMPSURLsAnalyzedCountH = _FeWMPSURLsAnalyzedCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 1, 1, 15),
    _FeWMPSURLsAnalyzedCountH_Type()
)
feWMPSURLsAnalyzedCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSURLsAnalyzedCountH.setStatus("current")
_FeWMPSURLsAnalyzedCountL_Type = Counter32
_FeWMPSURLsAnalyzedCountL_Object = MibTableColumn
feWMPSURLsAnalyzedCountL = _FeWMPSURLsAnalyzedCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 1, 1, 16),
    _FeWMPSURLsAnalyzedCountL_Type()
)
feWMPSURLsAnalyzedCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSURLsAnalyzedCountL.setStatus("current")
_FeWMPSURLsMaliciousCount_Type = Counter64
_FeWMPSURLsMaliciousCount_Object = MibTableColumn
feWMPSURLsMaliciousCount = _FeWMPSURLsMaliciousCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 1, 1, 17),
    _FeWMPSURLsMaliciousCount_Type()
)
feWMPSURLsMaliciousCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSURLsMaliciousCount.setStatus("current")
_FeWMPSURLsMaliciousCountH_Type = Counter32
_FeWMPSURLsMaliciousCountH_Object = MibTableColumn
feWMPSURLsMaliciousCountH = _FeWMPSURLsMaliciousCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 1, 1, 18),
    _FeWMPSURLsMaliciousCountH_Type()
)
feWMPSURLsMaliciousCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSURLsMaliciousCountH.setStatus("current")
_FeWMPSURLsMaliciousCountL_Type = Counter32
_FeWMPSURLsMaliciousCountL_Object = MibTableColumn
feWMPSURLsMaliciousCountL = _FeWMPSURLsMaliciousCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 1, 1, 19),
    _FeWMPSURLsMaliciousCountL_Type()
)
feWMPSURLsMaliciousCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSURLsMaliciousCountL.setStatus("current")
_FeWMPSDetectionStatsIndex_Type = Unsigned32
_FeWMPSDetectionStatsIndex_Object = MibTableColumn
feWMPSDetectionStatsIndex = _FeWMPSDetectionStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 1, 1, 20),
    _FeWMPSDetectionStatsIndex_Type()
)
feWMPSDetectionStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSDetectionStatsIndex.setStatus("current")
_FeWMPSAlertTable_Object = MibTable
feWMPSAlertTable = _FeWMPSAlertTable_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 2)
)
if mibBuilder.loadTexts:
    feWMPSAlertTable.setStatus("current")
_FeWMPSAlertEntry_Object = MibTableRow
feWMPSAlertEntry = _FeWMPSAlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 2, 1)
)
feWMPSAlertEntry.setIndexNames(
    (0, "FE-FIREEYE-MIB", "feWMPSAlertIndex1"),
    (0, "FE-FIREEYE-MIB", "feWMPSAlertIndex2"),
)
if mibBuilder.loadTexts:
    feWMPSAlertEntry.setStatus("current")


class _FeWMPSAlertTimeSpan_Type(OctetString):
    """Custom type feWMPSAlertTimeSpan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FeWMPSAlertTimeSpan_Type.__name__ = "OctetString"
_FeWMPSAlertTimeSpan_Object = MibTableColumn
feWMPSAlertTimeSpan = _FeWMPSAlertTimeSpan_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 2, 1, 1),
    _FeWMPSAlertTimeSpan_Type()
)
feWMPSAlertTimeSpan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSAlertTimeSpan.setStatus("current")


class _FeWMPSAlertName_Type(OctetString):
    """Custom type feWMPSAlertName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FeWMPSAlertName_Type.__name__ = "OctetString"
_FeWMPSAlertName_Object = MibTableColumn
feWMPSAlertName = _FeWMPSAlertName_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 2, 1, 2),
    _FeWMPSAlertName_Type()
)
feWMPSAlertName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSAlertName.setStatus("current")
_FeWMPSAlertCount_Type = Counter64
_FeWMPSAlertCount_Object = MibTableColumn
feWMPSAlertCount = _FeWMPSAlertCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 2, 1, 3),
    _FeWMPSAlertCount_Type()
)
feWMPSAlertCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSAlertCount.setStatus("current")
_FeWMPSAlertCountH_Type = Counter32
_FeWMPSAlertCountH_Object = MibTableColumn
feWMPSAlertCountH = _FeWMPSAlertCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 2, 1, 4),
    _FeWMPSAlertCountH_Type()
)
feWMPSAlertCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSAlertCountH.setStatus("current")
_FeWMPSAlertCountL_Type = Counter32
_FeWMPSAlertCountL_Object = MibTableColumn
feWMPSAlertCountL = _FeWMPSAlertCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 2, 1, 5),
    _FeWMPSAlertCountL_Type()
)
feWMPSAlertCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSAlertCountL.setStatus("current")
_FeWMPSAlertIndex1_Type = Unsigned32
_FeWMPSAlertIndex1_Object = MibTableColumn
feWMPSAlertIndex1 = _FeWMPSAlertIndex1_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 2, 1, 6),
    _FeWMPSAlertIndex1_Type()
)
feWMPSAlertIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSAlertIndex1.setStatus("current")
_FeWMPSAlertIndex2_Type = Unsigned32
_FeWMPSAlertIndex2_Object = MibTableColumn
feWMPSAlertIndex2 = _FeWMPSAlertIndex2_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 2, 1, 7),
    _FeWMPSAlertIndex2_Type()
)
feWMPSAlertIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSAlertIndex2.setStatus("current")
_FeWMPSThreatTable_Object = MibTable
feWMPSThreatTable = _FeWMPSThreatTable_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 3)
)
if mibBuilder.loadTexts:
    feWMPSThreatTable.setStatus("current")
_FeWMPSThreatEntry_Object = MibTableRow
feWMPSThreatEntry = _FeWMPSThreatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 3, 1)
)
feWMPSThreatEntry.setIndexNames(
    (0, "FE-FIREEYE-MIB", "feWMPSThreatIndex1"),
    (0, "FE-FIREEYE-MIB", "feWMPSThreatIndex2"),
)
if mibBuilder.loadTexts:
    feWMPSThreatEntry.setStatus("current")


class _FeWMPSThreatTimeSpan_Type(OctetString):
    """Custom type feWMPSThreatTimeSpan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FeWMPSThreatTimeSpan_Type.__name__ = "OctetString"
_FeWMPSThreatTimeSpan_Object = MibTableColumn
feWMPSThreatTimeSpan = _FeWMPSThreatTimeSpan_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 3, 1, 1),
    _FeWMPSThreatTimeSpan_Type()
)
feWMPSThreatTimeSpan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSThreatTimeSpan.setStatus("current")


class _FeWMPSThreatName_Type(OctetString):
    """Custom type feWMPSThreatName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FeWMPSThreatName_Type.__name__ = "OctetString"
_FeWMPSThreatName_Object = MibTableColumn
feWMPSThreatName = _FeWMPSThreatName_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 3, 1, 2),
    _FeWMPSThreatName_Type()
)
feWMPSThreatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSThreatName.setStatus("current")
_FeWMPSThreatCount_Type = Counter64
_FeWMPSThreatCount_Object = MibTableColumn
feWMPSThreatCount = _FeWMPSThreatCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 3, 1, 3),
    _FeWMPSThreatCount_Type()
)
feWMPSThreatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSThreatCount.setStatus("current")
_FeWMPSThreatCountH_Type = Counter32
_FeWMPSThreatCountH_Object = MibTableColumn
feWMPSThreatCountH = _FeWMPSThreatCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 3, 1, 4),
    _FeWMPSThreatCountH_Type()
)
feWMPSThreatCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSThreatCountH.setStatus("current")
_FeWMPSThreatCountL_Type = Counter32
_FeWMPSThreatCountL_Object = MibTableColumn
feWMPSThreatCountL = _FeWMPSThreatCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 3, 1, 5),
    _FeWMPSThreatCountL_Type()
)
feWMPSThreatCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSThreatCountL.setStatus("current")
_FeWMPSThreatIndex1_Type = Unsigned32
_FeWMPSThreatIndex1_Object = MibTableColumn
feWMPSThreatIndex1 = _FeWMPSThreatIndex1_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 3, 1, 6),
    _FeWMPSThreatIndex1_Type()
)
feWMPSThreatIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSThreatIndex1.setStatus("current")
_FeWMPSThreatIndex2_Type = Unsigned32
_FeWMPSThreatIndex2_Object = MibTableColumn
feWMPSThreatIndex2 = _FeWMPSThreatIndex2_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 3, 1, 7),
    _FeWMPSThreatIndex2_Type()
)
feWMPSThreatIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSThreatIndex2.setStatus("current")
_FeWMPSFileTypeTable_Object = MibTable
feWMPSFileTypeTable = _FeWMPSFileTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 4)
)
if mibBuilder.loadTexts:
    feWMPSFileTypeTable.setStatus("current")
_FeWMPSFileTypeEntry_Object = MibTableRow
feWMPSFileTypeEntry = _FeWMPSFileTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 4, 1)
)
feWMPSFileTypeEntry.setIndexNames(
    (0, "FE-FIREEYE-MIB", "feWMPSFileTypeIndex1"),
    (0, "FE-FIREEYE-MIB", "feWMPSFileTypeIndex2"),
)
if mibBuilder.loadTexts:
    feWMPSFileTypeEntry.setStatus("current")


class _FeWMPSFileTypeTimeSpan_Type(OctetString):
    """Custom type feWMPSFileTypeTimeSpan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FeWMPSFileTypeTimeSpan_Type.__name__ = "OctetString"
_FeWMPSFileTypeTimeSpan_Object = MibTableColumn
feWMPSFileTypeTimeSpan = _FeWMPSFileTypeTimeSpan_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 4, 1, 1),
    _FeWMPSFileTypeTimeSpan_Type()
)
feWMPSFileTypeTimeSpan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSFileTypeTimeSpan.setStatus("current")


class _FeWMPSFileTypeName_Type(OctetString):
    """Custom type feWMPSFileTypeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FeWMPSFileTypeName_Type.__name__ = "OctetString"
_FeWMPSFileTypeName_Object = MibTableColumn
feWMPSFileTypeName = _FeWMPSFileTypeName_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 4, 1, 2),
    _FeWMPSFileTypeName_Type()
)
feWMPSFileTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSFileTypeName.setStatus("current")
_FeWMPSFileTypeCount_Type = Counter64
_FeWMPSFileTypeCount_Object = MibTableColumn
feWMPSFileTypeCount = _FeWMPSFileTypeCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 4, 1, 3),
    _FeWMPSFileTypeCount_Type()
)
feWMPSFileTypeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSFileTypeCount.setStatus("current")
_FeWMPSFileTypeCountH_Type = Counter32
_FeWMPSFileTypeCountH_Object = MibTableColumn
feWMPSFileTypeCountH = _FeWMPSFileTypeCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 4, 1, 4),
    _FeWMPSFileTypeCountH_Type()
)
feWMPSFileTypeCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSFileTypeCountH.setStatus("current")
_FeWMPSFileTypeCountL_Type = Counter32
_FeWMPSFileTypeCountL_Object = MibTableColumn
feWMPSFileTypeCountL = _FeWMPSFileTypeCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 4, 1, 5),
    _FeWMPSFileTypeCountL_Type()
)
feWMPSFileTypeCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSFileTypeCountL.setStatus("current")
_FeWMPSFileTypeIndex1_Type = Unsigned32
_FeWMPSFileTypeIndex1_Object = MibTableColumn
feWMPSFileTypeIndex1 = _FeWMPSFileTypeIndex1_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 4, 1, 6),
    _FeWMPSFileTypeIndex1_Type()
)
feWMPSFileTypeIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSFileTypeIndex1.setStatus("current")
_FeWMPSFileTypeIndex2_Type = Unsigned32
_FeWMPSFileTypeIndex2_Object = MibTableColumn
feWMPSFileTypeIndex2 = _FeWMPSFileTypeIndex2_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 16, 4, 1, 7),
    _FeWMPSFileTypeIndex2_Type()
)
feWMPSFileTypeIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSFileTypeIndex2.setStatus("current")
_FeWMPSSizing_ObjectIdentity = ObjectIdentity
feWMPSSizing = _FeWMPSSizing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 17)
)
_FeWMPSUtilizationSummary_Type = Counter32
_FeWMPSUtilizationSummary_Object = MibScalar
feWMPSUtilizationSummary = _FeWMPSUtilizationSummary_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 17, 1),
    _FeWMPSUtilizationSummary_Type()
)
feWMPSUtilizationSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSUtilizationSummary.setStatus("current")
_FeWMPSWebAnalysisUtilization_Type = Counter32
_FeWMPSWebAnalysisUtilization_Object = MibScalar
feWMPSWebAnalysisUtilization = _FeWMPSWebAnalysisUtilization_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 17, 2),
    _FeWMPSWebAnalysisUtilization_Type()
)
feWMPSWebAnalysisUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSWebAnalysisUtilization.setStatus("current")
_FeWMPSWebAnalysisUtilizationStat_Type = Counter32
_FeWMPSWebAnalysisUtilizationStat_Object = MibScalar
feWMPSWebAnalysisUtilizationStat = _FeWMPSWebAnalysisUtilizationStat_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 17, 3),
    _FeWMPSWebAnalysisUtilizationStat_Type()
)
feWMPSWebAnalysisUtilizationStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSWebAnalysisUtilizationStat.setStatus("current")
_FeWMPSBinaryAnalysisBacklog_Type = Counter32
_FeWMPSBinaryAnalysisBacklog_Object = MibScalar
feWMPSBinaryAnalysisBacklog = _FeWMPSBinaryAnalysisBacklog_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 17, 4),
    _FeWMPSBinaryAnalysisBacklog_Type()
)
feWMPSBinaryAnalysisBacklog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSBinaryAnalysisBacklog.setStatus("current")
_FeWMPSBinaryAnalysisBacklogStat_Type = Counter32
_FeWMPSBinaryAnalysisBacklogStat_Object = MibScalar
feWMPSBinaryAnalysisBacklogStat = _FeWMPSBinaryAnalysisBacklogStat_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 17, 5),
    _FeWMPSBinaryAnalysisBacklogStat_Type()
)
feWMPSBinaryAnalysisBacklogStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSBinaryAnalysisBacklogStat.setStatus("current")
_FeWMPSCurrentWebSessions_Type = Counter32
_FeWMPSCurrentWebSessions_Object = MibScalar
feWMPSCurrentWebSessions = _FeWMPSCurrentWebSessions_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 17, 6),
    _FeWMPSCurrentWebSessions_Type()
)
feWMPSCurrentWebSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSCurrentWebSessions.setStatus("current")
_FeWMPSCurrentWebSessionStat_Type = Counter32
_FeWMPSCurrentWebSessionStat_Object = MibScalar
feWMPSCurrentWebSessionStat = _FeWMPSCurrentWebSessionStat_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 17, 7),
    _FeWMPSCurrentWebSessionStat_Type()
)
feWMPSCurrentWebSessionStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSCurrentWebSessionStat.setStatus("current")
_FeWMPSTotalBandwidth_Type = Counter32
_FeWMPSTotalBandwidth_Object = MibScalar
feWMPSTotalBandwidth = _FeWMPSTotalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 17, 8),
    _FeWMPSTotalBandwidth_Type()
)
feWMPSTotalBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSTotalBandwidth.setStatus("current")
_FeWMPSTotalBandwidthStat_Type = Counter32
_FeWMPSTotalBandwidthStat_Object = MibScalar
feWMPSTotalBandwidthStat = _FeWMPSTotalBandwidthStat_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 17, 9),
    _FeWMPSTotalBandwidthStat_Type()
)
feWMPSTotalBandwidthStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSTotalBandwidthStat.setStatus("current")
_FeMVXEnrollmentFailureTime_Type = OctetString
_FeMVXEnrollmentFailureTime_Object = MibScalar
feMVXEnrollmentFailureTime = _FeMVXEnrollmentFailureTime_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 18),
    _FeMVXEnrollmentFailureTime_Type()
)
feMVXEnrollmentFailureTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feMVXEnrollmentFailureTime.setStatus("current")
_FeMVXEnrollmentFailureReason_Type = OctetString
_FeMVXEnrollmentFailureReason_Object = MibScalar
feMVXEnrollmentFailureReason = _FeMVXEnrollmentFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 19),
    _FeMVXEnrollmentFailureReason_Type()
)
feMVXEnrollmentFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feMVXEnrollmentFailureReason.setStatus("current")
_FeWMPSSubmission_ObjectIdentity = ObjectIdentity
feWMPSSubmission = _FeWMPSSubmission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 20)
)
_FeWMPSSubmissionCountL_Type = Unsigned32
_FeWMPSSubmissionCountL_Object = MibScalar
feWMPSSubmissionCountL = _FeWMPSSubmissionCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 20, 1),
    _FeWMPSSubmissionCountL_Type()
)
feWMPSSubmissionCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSSubmissionCountL.setStatus("deprecated")
_FeWMPSSubmissionCountH_Type = Unsigned32
_FeWMPSSubmissionCountH_Object = MibScalar
feWMPSSubmissionCountH = _FeWMPSSubmissionCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 20, 2),
    _FeWMPSSubmissionCountH_Type()
)
feWMPSSubmissionCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSSubmissionCountH.setStatus("deprecated")
_FeWMPSSubmissionDoneCountL_Type = Unsigned32
_FeWMPSSubmissionDoneCountL_Object = MibScalar
feWMPSSubmissionDoneCountL = _FeWMPSSubmissionDoneCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 20, 3),
    _FeWMPSSubmissionDoneCountL_Type()
)
feWMPSSubmissionDoneCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSSubmissionDoneCountL.setStatus("deprecated")
_FeWMPSSubmissionDoneCountH_Type = Unsigned32
_FeWMPSSubmissionDoneCountH_Object = MibScalar
feWMPSSubmissionDoneCountH = _FeWMPSSubmissionDoneCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 20, 4),
    _FeWMPSSubmissionDoneCountH_Type()
)
feWMPSSubmissionDoneCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSSubmissionDoneCountH.setStatus("deprecated")
_FeWMPSSubmissionTimedOutCountL_Type = Unsigned32
_FeWMPSSubmissionTimedOutCountL_Object = MibScalar
feWMPSSubmissionTimedOutCountL = _FeWMPSSubmissionTimedOutCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 20, 5),
    _FeWMPSSubmissionTimedOutCountL_Type()
)
feWMPSSubmissionTimedOutCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSSubmissionTimedOutCountL.setStatus("deprecated")
_FeWMPSSubmissionTimedOutCountH_Type = Unsigned32
_FeWMPSSubmissionTimedOutCountH_Object = MibScalar
feWMPSSubmissionTimedOutCountH = _FeWMPSSubmissionTimedOutCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 20, 6),
    _FeWMPSSubmissionTimedOutCountH_Type()
)
feWMPSSubmissionTimedOutCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSSubmissionTimedOutCountH.setStatus("deprecated")
_FeWMPSSubmissionAging50to74CntL_Type = Unsigned32
_FeWMPSSubmissionAging50to74CntL_Object = MibScalar
feWMPSSubmissionAging50to74CntL = _FeWMPSSubmissionAging50to74CntL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 20, 7),
    _FeWMPSSubmissionAging50to74CntL_Type()
)
feWMPSSubmissionAging50to74CntL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSSubmissionAging50to74CntL.setStatus("deprecated")
_FeWMPSSubmissionAging50to74CntH_Type = Unsigned32
_FeWMPSSubmissionAging50to74CntH_Object = MibScalar
feWMPSSubmissionAging50to74CntH = _FeWMPSSubmissionAging50to74CntH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 20, 8),
    _FeWMPSSubmissionAging50to74CntH_Type()
)
feWMPSSubmissionAging50to74CntH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSSubmissionAging50to74CntH.setStatus("deprecated")
_FeWMPSSubmissionAging75to100CntL_Type = Unsigned32
_FeWMPSSubmissionAging75to100CntL_Object = MibScalar
feWMPSSubmissionAging75to100CntL = _FeWMPSSubmissionAging75to100CntL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 20, 9),
    _FeWMPSSubmissionAging75to100CntL_Type()
)
feWMPSSubmissionAging75to100CntL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSSubmissionAging75to100CntL.setStatus("deprecated")
_FeWMPSSubmissionAging75to100CntH_Type = Unsigned32
_FeWMPSSubmissionAging75to100CntH_Object = MibScalar
feWMPSSubmissionAging75to100CntH = _FeWMPSSubmissionAging75to100CntH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 20, 10),
    _FeWMPSSubmissionAging75to100CntH_Type()
)
feWMPSSubmissionAging75to100CntH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWMPSSubmissionAging75to100CntH.setStatus("deprecated")
_FePercentageInputTrafficLost_Type = OctetString
_FePercentageInputTrafficLost_Object = MibScalar
fePercentageInputTrafficLost = _FePercentageInputTrafficLost_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 21),
    _FePercentageInputTrafficLost_Type()
)
fePercentageInputTrafficLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePercentageInputTrafficLost.setStatus("current")
_FePercentageFlowIncompleteData_Type = OctetString
_FePercentageFlowIncompleteData_Object = MibScalar
fePercentageFlowIncompleteData = _FePercentageFlowIncompleteData_Object(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1, 22),
    _FePercentageFlowIncompleteData_Type()
)
fePercentageFlowIncompleteData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePercentageFlowIncompleteData.setStatus("current")
_FeMAS_ObjectIdentity = ObjectIdentity
feMAS = _FeMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 15)
)
_FeMASTraps_ObjectIdentity = ObjectIdentity
feMASTraps = _FeMASTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 15, 0)
)
_FeMASInfo_ObjectIdentity = ObjectIdentity
feMASInfo = _FeMASInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1)
)
_FeTotalObjectAnalyzedCount_Type = Counter64
_FeTotalObjectAnalyzedCount_Object = MibScalar
feTotalObjectAnalyzedCount = _FeTotalObjectAnalyzedCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 1),
    _FeTotalObjectAnalyzedCount_Type()
)
feTotalObjectAnalyzedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalObjectAnalyzedCount.setStatus("current")
_FeTotalObjectAnalyzedCountH_Type = Counter32
_FeTotalObjectAnalyzedCountH_Object = MibScalar
feTotalObjectAnalyzedCountH = _FeTotalObjectAnalyzedCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 2),
    _FeTotalObjectAnalyzedCountH_Type()
)
feTotalObjectAnalyzedCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalObjectAnalyzedCountH.setStatus("current")
_FeTotalObjectAnalyzedCountL_Type = Counter32
_FeTotalObjectAnalyzedCountL_Object = MibScalar
feTotalObjectAnalyzedCountL = _FeTotalObjectAnalyzedCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 3),
    _FeTotalObjectAnalyzedCountL_Type()
)
feTotalObjectAnalyzedCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalObjectAnalyzedCountL.setStatus("current")
_FeTotalMaliciousObjectCount_Type = Counter64
_FeTotalMaliciousObjectCount_Object = MibScalar
feTotalMaliciousObjectCount = _FeTotalMaliciousObjectCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 4),
    _FeTotalMaliciousObjectCount_Type()
)
feTotalMaliciousObjectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMaliciousObjectCount.setStatus("current")
_FeTotalMaliciousObjectCountH_Type = Counter32
_FeTotalMaliciousObjectCountH_Object = MibScalar
feTotalMaliciousObjectCountH = _FeTotalMaliciousObjectCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 5),
    _FeTotalMaliciousObjectCountH_Type()
)
feTotalMaliciousObjectCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMaliciousObjectCountH.setStatus("current")
_FeTotalMaliciousObjectCountL_Type = Counter32
_FeTotalMaliciousObjectCountL_Object = MibScalar
feTotalMaliciousObjectCountL = _FeTotalMaliciousObjectCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 6),
    _FeTotalMaliciousObjectCountL_Type()
)
feTotalMaliciousObjectCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMaliciousObjectCountL.setStatus("current")
_FeTotalUrlAnalyzedCount_Type = Counter64
_FeTotalUrlAnalyzedCount_Object = MibScalar
feTotalUrlAnalyzedCount = _FeTotalUrlAnalyzedCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 7),
    _FeTotalUrlAnalyzedCount_Type()
)
feTotalUrlAnalyzedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalUrlAnalyzedCount.setStatus("current")
_FeTotalUrlAnalyzedCountH_Type = Counter32
_FeTotalUrlAnalyzedCountH_Object = MibScalar
feTotalUrlAnalyzedCountH = _FeTotalUrlAnalyzedCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 8),
    _FeTotalUrlAnalyzedCountH_Type()
)
feTotalUrlAnalyzedCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalUrlAnalyzedCountH.setStatus("current")
_FeTotalUrlAnalyzedCountL_Type = Counter32
_FeTotalUrlAnalyzedCountL_Object = MibScalar
feTotalUrlAnalyzedCountL = _FeTotalUrlAnalyzedCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 9),
    _FeTotalUrlAnalyzedCountL_Type()
)
feTotalUrlAnalyzedCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalUrlAnalyzedCountL.setStatus("current")
_FeTotalMaliciousUrlCount_Type = Counter64
_FeTotalMaliciousUrlCount_Object = MibScalar
feTotalMaliciousUrlCount = _FeTotalMaliciousUrlCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 10),
    _FeTotalMaliciousUrlCount_Type()
)
feTotalMaliciousUrlCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMaliciousUrlCount.setStatus("current")
_FeTotalMaliciousUrlCountH_Type = Counter32
_FeTotalMaliciousUrlCountH_Object = MibScalar
feTotalMaliciousUrlCountH = _FeTotalMaliciousUrlCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 11),
    _FeTotalMaliciousUrlCountH_Type()
)
feTotalMaliciousUrlCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMaliciousUrlCountH.setStatus("current")
_FeTotalMaliciousUrlCountL_Type = Counter32
_FeTotalMaliciousUrlCountL_Object = MibScalar
feTotalMaliciousUrlCountL = _FeTotalMaliciousUrlCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 12),
    _FeTotalMaliciousUrlCountL_Type()
)
feTotalMaliciousUrlCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMaliciousUrlCountL.setStatus("current")
_FeTotalFileUploadedCount_Type = Counter64
_FeTotalFileUploadedCount_Object = MibScalar
feTotalFileUploadedCount = _FeTotalFileUploadedCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 13),
    _FeTotalFileUploadedCount_Type()
)
feTotalFileUploadedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalFileUploadedCount.setStatus("current")
_FeTotalFileUploadedCountH_Type = Counter32
_FeTotalFileUploadedCountH_Object = MibScalar
feTotalFileUploadedCountH = _FeTotalFileUploadedCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 14),
    _FeTotalFileUploadedCountH_Type()
)
feTotalFileUploadedCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalFileUploadedCountH.setStatus("current")
_FeTotalFileUploadedCountL_Type = Counter32
_FeTotalFileUploadedCountL_Object = MibScalar
feTotalFileUploadedCountL = _FeTotalFileUploadedCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 15),
    _FeTotalFileUploadedCountL_Type()
)
feTotalFileUploadedCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalFileUploadedCountL.setStatus("current")
_FeTotalMaliciousFileCount_Type = Counter64
_FeTotalMaliciousFileCount_Object = MibScalar
feTotalMaliciousFileCount = _FeTotalMaliciousFileCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 16),
    _FeTotalMaliciousFileCount_Type()
)
feTotalMaliciousFileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMaliciousFileCount.setStatus("current")
_FeTotalMaliciousFileCountH_Type = Counter32
_FeTotalMaliciousFileCountH_Object = MibScalar
feTotalMaliciousFileCountH = _FeTotalMaliciousFileCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 17),
    _FeTotalMaliciousFileCountH_Type()
)
feTotalMaliciousFileCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMaliciousFileCountH.setStatus("current")
_FeTotalMaliciousFileCountL_Type = Counter32
_FeTotalMaliciousFileCountL_Object = MibScalar
feTotalMaliciousFileCountL = _FeTotalMaliciousFileCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 18),
    _FeTotalMaliciousFileCountL_Type()
)
feTotalMaliciousFileCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMaliciousFileCountL.setStatus("current")
_FeTotalLiveModeCount_Type = Counter64
_FeTotalLiveModeCount_Object = MibScalar
feTotalLiveModeCount = _FeTotalLiveModeCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 19),
    _FeTotalLiveModeCount_Type()
)
feTotalLiveModeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalLiveModeCount.setStatus("current")
_FeTotalLiveModeCountH_Type = Counter32
_FeTotalLiveModeCountH_Object = MibScalar
feTotalLiveModeCountH = _FeTotalLiveModeCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 20),
    _FeTotalLiveModeCountH_Type()
)
feTotalLiveModeCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalLiveModeCountH.setStatus("current")
_FeTotalLiveModeCountL_Type = Counter32
_FeTotalLiveModeCountL_Object = MibScalar
feTotalLiveModeCountL = _FeTotalLiveModeCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 21),
    _FeTotalLiveModeCountL_Type()
)
feTotalLiveModeCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalLiveModeCountL.setStatus("current")
_FeTotalMaliciousLiveModeCount_Type = Counter64
_FeTotalMaliciousLiveModeCount_Object = MibScalar
feTotalMaliciousLiveModeCount = _FeTotalMaliciousLiveModeCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 22),
    _FeTotalMaliciousLiveModeCount_Type()
)
feTotalMaliciousLiveModeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMaliciousLiveModeCount.setStatus("current")
_FeTotalMaliciousLiveModeCountH_Type = Counter32
_FeTotalMaliciousLiveModeCountH_Object = MibScalar
feTotalMaliciousLiveModeCountH = _FeTotalMaliciousLiveModeCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 23),
    _FeTotalMaliciousLiveModeCountH_Type()
)
feTotalMaliciousLiveModeCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMaliciousLiveModeCountH.setStatus("current")
_FeTotalMaliciousLiveModeCountL_Type = Counter32
_FeTotalMaliciousLiveModeCountL_Object = MibScalar
feTotalMaliciousLiveModeCountL = _FeTotalMaliciousLiveModeCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 24),
    _FeTotalMaliciousLiveModeCountL_Type()
)
feTotalMaliciousLiveModeCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMaliciousLiveModeCountL.setStatus("current")
_FeMaid_Type = CounterBasedGauge64
_FeMaid_Object = MibScalar
feMaid = _FeMaid_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 25),
    _FeMaid_Type()
)
feMaid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feMaid.setStatus("current")
_FeMSM_ObjectIdentity = ObjectIdentity
feMSM = _FeMSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 16)
)
_FeMSMTraps_ObjectIdentity = ObjectIdentity
feMSMTraps = _FeMSMTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 16, 0)
)
_FeMSMInfo_ObjectIdentity = ObjectIdentity
feMSMInfo = _FeMSMInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 16, 1)
)
_FeMibAdminInfo_ObjectIdentity = ObjectIdentity
feMibAdminInfo = _FeMibAdminInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 20)
)
_FeMibCompliances_ObjectIdentity = ObjectIdentity
feMibCompliances = _FeMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 20, 2)
)
_FeMibGroups_ObjectIdentity = ObjectIdentity
feMibGroups = _FeMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3)
)
_FeMibDeprecatedGroups_ObjectIdentity = ObjectIdentity
feMibDeprecatedGroups = _FeMibDeprecatedGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 20, 4)
)

# Managed Objects groups

feVariablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 1)
)
feVariablesGroup.setObjects(
      *(("FE-FIREEYE-MIB", "lmsVersion"),
        ("FE-FIREEYE-MIB", "eventCount"),
        ("FE-FIREEYE-MIB", "eventIndex"),
        ("FE-FIREEYE-MIB", "eventId"),
        ("FE-FIREEYE-MIB", "eventType"),
        ("FE-FIREEYE-MIB", "eventDate"),
        ("FE-FIREEYE-MIB", "eventTime"),
        ("FE-FIREEYE-MIB", "eventTraceId"),
        ("FE-FIREEYE-MIB", "eventSrcIp"),
        ("FE-FIREEYE-MIB", "eventDstIp"),
        ("FE-FIREEYE-MIB", "eventSrcMac"),
        ("FE-FIREEYE-MIB", "eventDstMac"),
        ("FE-FIREEYE-MIB", "eventDstPort"),
        ("FE-FIREEYE-MIB", "eventVlan"),
        ("FE-FIREEYE-MIB", "eventProtocol"),
        ("FE-FIREEYE-MIB", "eventProfileId"),
        ("FE-FIREEYE-MIB", "eventOsInfo"),
        ("FE-FIREEYE-MIB", "eventService"),
        ("FE-FIREEYE-MIB", "eventAttackType"),
        ("FE-FIREEYE-MIB", "eventSignatureName"),
        ("FE-FIREEYE-MIB", "eventSignatureType"),
        ("FE-FIREEYE-MIB", "eventSrcHost"),
        ("FE-FIREEYE-MIB", "eventCncNo"),
        ("FE-FIREEYE-MIB", "alertSignatureId"),
        ("FE-FIREEYE-MIB", "alertCncHost"),
        ("FE-FIREEYE-MIB", "alertCncPort"),
        ("FE-FIREEYE-MIB", "alertChecksum"),
        ("FE-FIREEYE-MIB", "alertAnalysisType"),
        ("FE-FIREEYE-MIB", "alertProfile"),
        ("FE-FIREEYE-MIB", "alertAction"),
        ("FE-FIREEYE-MIB", "alertInterface"),
        ("FE-FIREEYE-MIB", "alertSensorIp"),
        ("FE-FIREEYE-MIB", "alertSensorHost"),
        ("FE-FIREEYE-MIB", "alertSensorProduct"),
        ("FE-FIREEYE-MIB", "alertSensorRelease"),
        ("FE-FIREEYE-MIB", "alertUrl"),
        ("FE-FIREEYE-MIB", "eventSrcAddrType"),
        ("FE-FIREEYE-MIB", "eventSrcAddr"),
        ("FE-FIREEYE-MIB", "eventDstAddrType"),
        ("FE-FIREEYE-MIB", "eventDstAddr"),
        ("FE-FIREEYE-MIB", "eventSensorAddrType"),
        ("FE-FIREEYE-MIB", "eventSensorAddr"),
        ("FE-FIREEYE-MIB", "eventSrcPort"),
        ("FE-FIREEYE-MIB", "eventDateTime"),
        ("FE-FIREEYE-MIB", "ipsSignatureId"),
        ("FE-FIREEYE-MIB", "ipsSignatureRevision"),
        ("FE-FIREEYE-MIB", "ipsMatchCount"),
        ("FE-FIREEYE-MIB", "ipsSeverity"),
        ("FE-FIREEYE-MIB", "ipsSignatureName"),
        ("FE-FIREEYE-MIB", "ipsReferenceId"),
        ("FE-FIREEYE-MIB", "ipsBlockMode"),
        ("FE-FIREEYE-MIB", "ipsAttackTarget"),
        ("FE-FIREEYE-MIB", "isMalicious"),
        ("FE-FIREEYE-MIB", "ipsAttackConfirmation"),
        ("FE-FIREEYE-MIB", "isRetroactive"))
)
if mibBuilder.loadTexts:
    feVariablesGroup.setStatus("current")

feSystemInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 11)
)
feSystemInfoGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feSystemStatus"),
        ("FE-FIREEYE-MIB", "feHardwareModel"),
        ("FE-FIREEYE-MIB", "feSerialNumber"),
        ("FE-FIREEYE-MIB", "feTemperatureValue"),
        ("FE-FIREEYE-MIB", "feTemperatureStatus"),
        ("FE-FIREEYE-MIB", "feTemperatureIsHealthy"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeIfname"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeIfname"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeOldAdminUp"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeNewAdminUp"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeOldLinkUp"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeNewLinkUp"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeOldSpeed"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeNewSpeed"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeOldDuplex"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeNewDuplex"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeOldAutoNeg"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeNewAutoNeg"),
        ("FE-FIREEYE-MIB", "feFaasVpnConnected"),
        ("FE-FIREEYE-MIB", "feProcessCrashName"),
        ("FE-FIREEYE-MIB", "feProcessCrashNumFailures"),
        ("FE-FIREEYE-MIB", "feProcessCrashLive"),
        ("FE-FIREEYE-MIB", "feSyslogRotationReason"),
        ("FE-FIREEYE-MIB", "feLoginUsername"),
        ("FE-FIREEYE-MIB", "feLoginUsernameLocal"),
        ("FE-FIREEYE-MIB", "feLoginTimestamp"),
        ("FE-FIREEYE-MIB", "feLoginRemoteAddr"),
        ("FE-FIREEYE-MIB", "feLoginRemoteInetAddrType"),
        ("FE-FIREEYE-MIB", "feLoginRemoteInetAddr"),
        ("FE-FIREEYE-MIB", "feLoginRemoteHostname"),
        ("FE-FIREEYE-MIB", "feLoginPeerId"),
        ("FE-FIREEYE-MIB", "feLoginClientDescr"),
        ("FE-FIREEYE-MIB", "feLoginSessionId"),
        ("FE-FIREEYE-MIB", "feLoginTimestampOrigAuth"),
        ("FE-FIREEYE-MIB", "feLoginAuthMethod"),
        ("FE-FIREEYE-MIB", "feLoginTrusted"),
        ("FE-FIREEYE-MIB", "feLoginAuthSubmethod"),
        ("FE-FIREEYE-MIB", "feLoginRole"),
        ("FE-FIREEYE-MIB", "feAwsInstanceId"),
        ("FE-FIREEYE-MIB", "feAwsInstanceType"),
        ("FE-FIREEYE-MIB", "feAwsImageId"))
)
if mibBuilder.loadTexts:
    feSystemInfoGroup.setStatus("current")

feStorageInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 13)
)
feStorageInfoGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feRaidStatus"),
        ("FE-FIREEYE-MIB", "feRaidIsHealthy"),
        ("FE-FIREEYE-MIB", "fePhysicalDiskIndex"),
        ("FE-FIREEYE-MIB", "fePhysicalDiskName"),
        ("FE-FIREEYE-MIB", "fePhysicalDiskStatus"),
        ("FE-FIREEYE-MIB", "fePhysicalDiskIsHealthy"),
        ("FE-FIREEYE-MIB", "fePhysicalDiskDeviceSupport"),
        ("FE-FIREEYE-MIB", "fePhysicalDiskSelfAssess"),
        ("FE-FIREEYE-MIB", "fePhysicalDiskTotalBytes"))
)
if mibBuilder.loadTexts:
    feStorageInfoGroup.setStatus("current")

fePowerSupplyInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 15)
)
fePowerSupplyInfoGroup.setObjects(
      *(("FE-FIREEYE-MIB", "fePowerSupplyOverallStatus"),
        ("FE-FIREEYE-MIB", "fePowerSupplyOverallIsHealthy"))
)
if mibBuilder.loadTexts:
    fePowerSupplyInfoGroup.setStatus("current")

feFanHealthInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 17)
)
feFanHealthInfoGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feFanOverallStatus"),
        ("FE-FIREEYE-MIB", "feFanOverallIsHealthy"),
        ("FE-FIREEYE-MIB", "feFanIndex"),
        ("FE-FIREEYE-MIB", "feFanStatus"),
        ("FE-FIREEYE-MIB", "feFanIsHealthy"),
        ("FE-FIREEYE-MIB", "feFanSpeed"),
        ("FE-FIREEYE-MIB", "feFanName"))
)
if mibBuilder.loadTexts:
    feFanHealthInfoGroup.setStatus("current")

feApplicationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 19)
)
feApplicationInfoGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feInstalledSystemImage"),
        ("FE-FIREEYE-MIB", "feSystemImageVersionCurrent"),
        ("FE-FIREEYE-MIB", "feSystemImageVersionLatest"),
        ("FE-FIREEYE-MIB", "feIsSystemImageLatest"),
        ("FE-FIREEYE-MIB", "feSecurityContentVersion"),
        ("FE-FIREEYE-MIB", "feLastContentUpdatePassed"),
        ("FE-FIREEYE-MIB", "feLastContentUpdateTime"),
        ("FE-FIREEYE-MIB", "feGIIndex"),
        ("FE-FIREEYE-MIB", "feGIName"),
        ("FE-FIREEYE-MIB", "feGIVersion"),
        ("FE-FIREEYE-MIB", "feGIEnabled"),
        ("FE-FIREEYE-MIB", "feGIInstallDateTime"),
        ("FE-FIREEYE-MIB", "feActiveVMs"),
        ("FE-FIREEYE-MIB", "feProductLicenseActive"),
        ("FE-FIREEYE-MIB", "feContentLicenseActive"),
        ("FE-FIREEYE-MIB", "feSupportLicenseActive"),
        ("FE-FIREEYE-MIB", "feLicenseFeatureName"),
        ("FE-FIREEYE-MIB", "feLicenseNewActiveState"),
        ("FE-FIREEYE-MIB", "feLicenseOldActiveState"),
        ("FE-FIREEYE-MIB", "feLicenseFeature"),
        ("FE-FIREEYE-MIB", "feLicenseFeatureDescr"),
        ("FE-FIREEYE-MIB", "feLicenseActive"),
        ("FE-FIREEYE-MIB", "feLicenseExpiration"),
        ("FE-FIREEYE-MIB", "feLicenseDaysUntilExpiration"),
        ("FE-FIREEYE-MIB", "feTokenFailureReason"),
        ("FE-FIREEYE-MIB", "feTokenApplianceId"),
        ("FE-FIREEYE-MIB", "feTokenLeaseDuration"),
        ("FE-FIREEYE-MIB", "feTokenLeaseIsActive"),
        ("FE-FIREEYE-MIB", "feTokenLeaseTimeRemaining"),
        ("FE-FIREEYE-MIB", "feTokenGraceDuration"),
        ("FE-FIREEYE-MIB", "feTokenGraceIsActive"),
        ("FE-FIREEYE-MIB", "feTokenGraceTimeRemaining"),
        ("FE-FIREEYE-MIB", "feTokenLicenseExpiryTime"),
        ("FE-FIREEYE-MIB", "feTokenLicenseExpiryRequired"),
        ("FE-FIREEYE-MIB", "feTokenLicenseIsActive"),
        ("FE-FIREEYE-MIB", "feTokenLocalUuid"),
        ("FE-FIREEYE-MIB", "feTokenLocalActiveDuration"),
        ("FE-FIREEYE-MIB", "feTokenWinnerUuid"),
        ("FE-FIREEYE-MIB", "feTokenUuidList"),
        ("FE-FIREEYE-MIB", "feTokenUuidActiveDuration"))
)
if mibBuilder.loadTexts:
    feApplicationInfoGroup.setStatus("current")

feCMSInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 21)
)
feCMSInfoGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feTotalAppliancesAttached"),
        ("FE-FIREEYE-MIB", "feTotalWMPSAttached"),
        ("FE-FIREEYE-MIB", "feTotalEMPSAttached"),
        ("FE-FIREEYE-MIB", "feTotalFMPSAttached"),
        ("FE-FIREEYE-MIB", "feTotalMASAttached"),
        ("FE-FIREEYE-MIB", "feCMSApplianceIndex"),
        ("FE-FIREEYE-MIB", "feCMSApplianceName"),
        ("FE-FIREEYE-MIB", "feCMSApplianceDiskSpacePassed"),
        ("FE-FIREEYE-MIB", "feCMSApplianceFanPassed"),
        ("FE-FIREEYE-MIB", "feCMSAppliancePowerSupplyPassed"),
        ("FE-FIREEYE-MIB", "feCMSApplianceRaidPassed"),
        ("FE-FIREEYE-MIB", "feCMSApplianceTemperaturePassed"),
        ("FE-FIREEYE-MIB", "feCMSHANxHealthFailureName"),
        ("FE-FIREEYE-MIB", "feCMSHANxHealthFailureType"),
        ("FE-FIREEYE-MIB", "feCMSHANxHealthFailureNx1"),
        ("FE-FIREEYE-MIB", "feCMSHANxHealthFailureNx2"),
        ("FE-FIREEYE-MIB", "feCMSHANxHealthFailureReason"),
        ("FE-FIREEYE-MIB", "feCMSHANxHealthFailureDesc"),
        ("FE-FIREEYE-MIB", "feMVXClusterName"),
        ("FE-FIREEYE-MIB", "feMVXClusterStateChangeDesc"),
        ("FE-FIREEYE-MIB", "feMVXClusterUtilExceedAlarmId"),
        ("FE-FIREEYE-MIB", "feMVXClusterUtilExceedDataValue"))
)
if mibBuilder.loadTexts:
    feCMSInfoGroup.setStatus("current")

feEMPSInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 23)
)
feEMPSInfoGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feTotalEmailCount"),
        ("FE-FIREEYE-MIB", "feTotalEmailCountH"),
        ("FE-FIREEYE-MIB", "feTotalEmailCountL"),
        ("FE-FIREEYE-MIB", "feInfectedEmailCount"),
        ("FE-FIREEYE-MIB", "feInfectedEmailCountH"),
        ("FE-FIREEYE-MIB", "feInfectedEmailCountL"),
        ("FE-FIREEYE-MIB", "feAnalyzedEmailCount"),
        ("FE-FIREEYE-MIB", "feAnalyzedEmailCountH"),
        ("FE-FIREEYE-MIB", "feAnalyzedEmailCountL"),
        ("FE-FIREEYE-MIB", "feTotalUrlCount"),
        ("FE-FIREEYE-MIB", "feTotalUrlCountH"),
        ("FE-FIREEYE-MIB", "feTotalUrlCountL"),
        ("FE-FIREEYE-MIB", "feInfectedUrlCount"),
        ("FE-FIREEYE-MIB", "feInfectedUrlCountH"),
        ("FE-FIREEYE-MIB", "feInfectedUrlCountL"),
        ("FE-FIREEYE-MIB", "feAnalyzedUrlCount"),
        ("FE-FIREEYE-MIB", "feAnalyzedUrlCountH"),
        ("FE-FIREEYE-MIB", "feAnalyzedUrlCountL"),
        ("FE-FIREEYE-MIB", "feTotalAttachmentCount"),
        ("FE-FIREEYE-MIB", "feTotalAttachmentCountH"),
        ("FE-FIREEYE-MIB", "feTotalAttachmentCountL"),
        ("FE-FIREEYE-MIB", "feInfectedAttachmentCount"),
        ("FE-FIREEYE-MIB", "feInfectedAttachmentCountH"),
        ("FE-FIREEYE-MIB", "feInfectedAttachmentCountL"),
        ("FE-FIREEYE-MIB", "feAnalyzedAttachmentCount"),
        ("FE-FIREEYE-MIB", "feAnalyzedAttachmentCountH"),
        ("FE-FIREEYE-MIB", "feAnalyzedAttachmentCountL"),
        ("FE-FIREEYE-MIB", "feTotalEmailHasAttachment"),
        ("FE-FIREEYE-MIB", "feTotalEmailHasAttachmentH"),
        ("FE-FIREEYE-MIB", "feTotalEmailHasAttachmentL"),
        ("FE-FIREEYE-MIB", "feTotalEmailHasUrl"),
        ("FE-FIREEYE-MIB", "feTotalEmailHasUrlH"),
        ("FE-FIREEYE-MIB", "feTotalEmailHasUrlL"),
        ("FE-FIREEYE-MIB", "feTotalEmailHasBadAttachment"),
        ("FE-FIREEYE-MIB", "feTotalEmailHasBadAttachmentH"),
        ("FE-FIREEYE-MIB", "feTotalEmailHasBadAttachmentL"),
        ("FE-FIREEYE-MIB", "feTotalEmailHasBadUrl"),
        ("FE-FIREEYE-MIB", "feTotalEmailHasBadUrlH"),
        ("FE-FIREEYE-MIB", "feTotalEmailHasBadUrlL"),
        ("FE-FIREEYE-MIB", "feeQuarantineUsage"),
        ("FE-FIREEYE-MIB", "feBypassEmailCount"),
        ("FE-FIREEYE-MIB", "feBypassEmailCountH"),
        ("FE-FIREEYE-MIB", "feBypassEmailCountL"),
        ("FE-FIREEYE-MIB", "feDeferredEmailCount"),
        ("FE-FIREEYE-MIB", "feHoldQueueEmailCount"),
        ("FE-FIREEYE-MIB", "feOpenSmtpConnections"),
        ("FE-FIREEYE-MIB", "feIncomingEmailCount"),
        ("FE-FIREEYE-MIB", "feActiveEmailCount"),
        ("FE-FIREEYE-MIB", "feDropEmailCount"),
        ("FE-FIREEYE-MIB", "feSamplingEmailStartTime"),
        ("FE-FIREEYE-MIB", "feSamplingEmailEndTime"),
        ("FE-FIREEYE-MIB", "feSamplingEmailReceivedRate"))
)
if mibBuilder.loadTexts:
    feEMPSInfoGroup.setStatus("current")

feWMPSInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 25)
)
feWMPSInfoGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feDeploymentCheckStatus"),
        ("FE-FIREEYE-MIB", "feDeploymentCheckIsHealthy"),
        ("FE-FIREEYE-MIB", "feDeploymentCheckMessage"),
        ("FE-FIREEYE-MIB", "feDeploymentCheckStartTime"),
        ("FE-FIREEYE-MIB", "feDeploymentCheckEndTime"),
        ("FE-FIREEYE-MIB", "feDeploymentCheckDataSize"),
        ("FE-FIREEYE-MIB", "feDeploymentCheckPktCount"),
        ("FE-FIREEYE-MIB", "feDeploymentCheckReTransPktCount"),
        ("FE-FIREEYE-MIB", "feDeploymentCheckDupAckPktCount"),
        ("FE-FIREEYE-MIB", "feDeploymentCheckOOOPktCount"),
        ("FE-FIREEYE-MIB", "feDeploymentCheckAckUsnPktCount"),
        ("FE-FIREEYE-MIB", "feDeploymentCheckPSegNCPktCount"),
        ("FE-FIREEYE-MIB", "feDeploymentCheckMFormedPktCount"),
        ("FE-FIREEYE-MIB", "feDeploymentCheckStreamCount"),
        ("FE-FIREEYE-MIB", "feDeploymentCheckAsymStreamCount"),
        ("FE-FIREEYE-MIB", "feWMPSDetectionStatsTimeSpan"),
        ("FE-FIREEYE-MIB", "feWMPSAPTAttackCount"),
        ("FE-FIREEYE-MIB", "feWMPSAPTAttackCountH"),
        ("FE-FIREEYE-MIB", "feWMPSAPTAttackCountL"),
        ("FE-FIREEYE-MIB", "feWMPSNewGlobalThreatCount"),
        ("FE-FIREEYE-MIB", "feWMPSNewGlobalThreatCountH"),
        ("FE-FIREEYE-MIB", "feWMPSNewGlobalThreatCountL"),
        ("FE-FIREEYE-MIB", "feWMPSInfectedHostCount"),
        ("FE-FIREEYE-MIB", "feWMPSInfectedHostCountH"),
        ("FE-FIREEYE-MIB", "feWMPSInfectedHostCountL"),
        ("FE-FIREEYE-MIB", "feWMPSObjectsAnalyzedCount"),
        ("FE-FIREEYE-MIB", "feWMPSObjectsAnalyzedCountH"),
        ("FE-FIREEYE-MIB", "feWMPSObjectsAnalyzedCountL"),
        ("FE-FIREEYE-MIB", "feWMPSURLsAnalyzedCount"),
        ("FE-FIREEYE-MIB", "feWMPSURLsAnalyzedCountH"),
        ("FE-FIREEYE-MIB", "feWMPSURLsAnalyzedCountL"),
        ("FE-FIREEYE-MIB", "feWMPSURLsMaliciousCount"),
        ("FE-FIREEYE-MIB", "feWMPSURLsMaliciousCountH"),
        ("FE-FIREEYE-MIB", "feWMPSURLsMaliciousCountL"),
        ("FE-FIREEYE-MIB", "feWMPSDetectionStatsIndex"),
        ("FE-FIREEYE-MIB", "feWMPSAlertTimeSpan"),
        ("FE-FIREEYE-MIB", "feWMPSAlertName"),
        ("FE-FIREEYE-MIB", "feWMPSAlertCount"),
        ("FE-FIREEYE-MIB", "feWMPSAlertCountH"),
        ("FE-FIREEYE-MIB", "feWMPSAlertCountL"),
        ("FE-FIREEYE-MIB", "feWMPSAlertIndex1"),
        ("FE-FIREEYE-MIB", "feWMPSAlertIndex2"),
        ("FE-FIREEYE-MIB", "feWMPSThreatTimeSpan"),
        ("FE-FIREEYE-MIB", "feWMPSThreatName"),
        ("FE-FIREEYE-MIB", "feWMPSThreatCount"),
        ("FE-FIREEYE-MIB", "feWMPSThreatCountH"),
        ("FE-FIREEYE-MIB", "feWMPSThreatCountL"),
        ("FE-FIREEYE-MIB", "feWMPSThreatIndex1"),
        ("FE-FIREEYE-MIB", "feWMPSThreatIndex2"),
        ("FE-FIREEYE-MIB", "feWMPSFileTypeTimeSpan"),
        ("FE-FIREEYE-MIB", "feWMPSFileTypeName"),
        ("FE-FIREEYE-MIB", "feWMPSFileTypeCount"),
        ("FE-FIREEYE-MIB", "feWMPSFileTypeCountH"),
        ("FE-FIREEYE-MIB", "feWMPSFileTypeCountL"),
        ("FE-FIREEYE-MIB", "feWMPSFileTypeIndex1"),
        ("FE-FIREEYE-MIB", "feWMPSFileTypeIndex2"),
        ("FE-FIREEYE-MIB", "feWMPSUtilizationSummary"),
        ("FE-FIREEYE-MIB", "feWMPSWebAnalysisUtilization"),
        ("FE-FIREEYE-MIB", "feWMPSWebAnalysisUtilizationStat"),
        ("FE-FIREEYE-MIB", "feWMPSBinaryAnalysisBacklog"),
        ("FE-FIREEYE-MIB", "feWMPSBinaryAnalysisBacklogStat"),
        ("FE-FIREEYE-MIB", "feWMPSCurrentWebSessions"),
        ("FE-FIREEYE-MIB", "feWMPSCurrentWebSessionStat"),
        ("FE-FIREEYE-MIB", "feWMPSTotalBandwidth"),
        ("FE-FIREEYE-MIB", "feWMPSTotalBandwidthStat"),
        ("FE-FIREEYE-MIB", "feMVXEnrollmentFailureTime"),
        ("FE-FIREEYE-MIB", "feMVXEnrollmentFailureReason"),
        ("FE-FIREEYE-MIB", "fePercentageInputTrafficLost"),
        ("FE-FIREEYE-MIB", "fePercentageFlowIncompleteData"))
)
if mibBuilder.loadTexts:
    feWMPSInfoGroup.setStatus("current")

feMASInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 27)
)
feMASInfoGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feTotalObjectAnalyzedCount"),
        ("FE-FIREEYE-MIB", "feTotalObjectAnalyzedCountH"),
        ("FE-FIREEYE-MIB", "feTotalObjectAnalyzedCountL"),
        ("FE-FIREEYE-MIB", "feTotalMaliciousObjectCount"),
        ("FE-FIREEYE-MIB", "feTotalMaliciousObjectCountH"),
        ("FE-FIREEYE-MIB", "feTotalMaliciousObjectCountL"),
        ("FE-FIREEYE-MIB", "feTotalUrlAnalyzedCount"),
        ("FE-FIREEYE-MIB", "feTotalUrlAnalyzedCountH"),
        ("FE-FIREEYE-MIB", "feTotalUrlAnalyzedCountL"),
        ("FE-FIREEYE-MIB", "feTotalMaliciousUrlCount"),
        ("FE-FIREEYE-MIB", "feTotalMaliciousUrlCountH"),
        ("FE-FIREEYE-MIB", "feTotalMaliciousUrlCountL"),
        ("FE-FIREEYE-MIB", "feTotalFileUploadedCount"),
        ("FE-FIREEYE-MIB", "feTotalFileUploadedCountH"),
        ("FE-FIREEYE-MIB", "feTotalFileUploadedCountL"),
        ("FE-FIREEYE-MIB", "feTotalMaliciousFileCount"),
        ("FE-FIREEYE-MIB", "feTotalMaliciousFileCountH"),
        ("FE-FIREEYE-MIB", "feTotalMaliciousFileCountL"),
        ("FE-FIREEYE-MIB", "feTotalLiveModeCount"),
        ("FE-FIREEYE-MIB", "feTotalLiveModeCountH"),
        ("FE-FIREEYE-MIB", "feTotalLiveModeCountL"),
        ("FE-FIREEYE-MIB", "feTotalMaliciousLiveModeCount"),
        ("FE-FIREEYE-MIB", "feTotalMaliciousLiveModeCountH"),
        ("FE-FIREEYE-MIB", "feTotalMaliciousLiveModeCountL"),
        ("FE-FIREEYE-MIB", "feMaid"))
)
if mibBuilder.loadTexts:
    feMASInfoGroup.setStatus("current")

feSubmissionInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 29)
)
feSubmissionInfoGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feSubmissionCountL"),
        ("FE-FIREEYE-MIB", "feSubmissionCountH"),
        ("FE-FIREEYE-MIB", "feSubmissionDoneCountL"),
        ("FE-FIREEYE-MIB", "feSubmissionDoneCountH"),
        ("FE-FIREEYE-MIB", "feSubmissionTimedOutCountL"),
        ("FE-FIREEYE-MIB", "feSubmissionTimedOutCountH"),
        ("FE-FIREEYE-MIB", "feSubmissionAging50to74CntL"),
        ("FE-FIREEYE-MIB", "feSubmissionAging50to74CntH"),
        ("FE-FIREEYE-MIB", "feSubmissionAging75to100CntL"),
        ("FE-FIREEYE-MIB", "feSubmissionAging75to100CntH"))
)
if mibBuilder.loadTexts:
    feSubmissionInfoGroup.setStatus("current")

feDeprecatedSubmissionInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 4, 1)
)
feDeprecatedSubmissionInfoGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feWMPSSubmissionCountL"),
        ("FE-FIREEYE-MIB", "feWMPSSubmissionCountH"),
        ("FE-FIREEYE-MIB", "feWMPSSubmissionDoneCountL"),
        ("FE-FIREEYE-MIB", "feWMPSSubmissionDoneCountH"),
        ("FE-FIREEYE-MIB", "feWMPSSubmissionTimedOutCountL"),
        ("FE-FIREEYE-MIB", "feWMPSSubmissionTimedOutCountH"),
        ("FE-FIREEYE-MIB", "feWMPSSubmissionAging50to74CntL"),
        ("FE-FIREEYE-MIB", "feWMPSSubmissionAging50to74CntH"),
        ("FE-FIREEYE-MIB", "feWMPSSubmissionAging75to100CntL"),
        ("FE-FIREEYE-MIB", "feWMPSSubmissionAging75to100CntH"))
)
if mibBuilder.loadTexts:
    feDeprecatedSubmissionInfoGroup.setStatus("deprecated")

feDeprecatedPowerSupplyInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 4, 2)
)
feDeprecatedPowerSupplyInfoGroup.setObjects(
      *(("FE-FIREEYE-MIB", "fePowerSupplyIndex"),
        ("FE-FIREEYE-MIB", "fePowerSupplyStatus"),
        ("FE-FIREEYE-MIB", "fePowerSupplyIsHealthy"))
)
if mibBuilder.loadTexts:
    feDeprecatedPowerSupplyInfoGroup.setStatus("deprecated")


# Notification objects

fireeyeAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 3, 0, 1)
)
fireeyeAlert.setObjects(
      *(("FE-FIREEYE-MIB", "eventIndex"),
        ("FE-FIREEYE-MIB", "eventId"),
        ("FE-FIREEYE-MIB", "eventType"),
        ("FE-FIREEYE-MIB", "eventDate"),
        ("FE-FIREEYE-MIB", "eventTime"),
        ("FE-FIREEYE-MIB", "eventTraceId"),
        ("FE-FIREEYE-MIB", "eventSrcIp"),
        ("FE-FIREEYE-MIB", "eventDstIp"),
        ("FE-FIREEYE-MIB", "eventSrcMac"),
        ("FE-FIREEYE-MIB", "eventDstMac"),
        ("FE-FIREEYE-MIB", "eventDstPort"),
        ("FE-FIREEYE-MIB", "eventVlan"),
        ("FE-FIREEYE-MIB", "eventProtocol"),
        ("FE-FIREEYE-MIB", "eventProfileId"),
        ("FE-FIREEYE-MIB", "eventOsInfo"),
        ("FE-FIREEYE-MIB", "eventService"),
        ("FE-FIREEYE-MIB", "eventAttackType"),
        ("FE-FIREEYE-MIB", "eventSignatureName"),
        ("FE-FIREEYE-MIB", "eventSignatureType"),
        ("FE-FIREEYE-MIB", "eventSrcHost"),
        ("FE-FIREEYE-MIB", "eventCncNo"),
        ("FE-FIREEYE-MIB", "alertSignatureId"),
        ("FE-FIREEYE-MIB", "alertCncHost"),
        ("FE-FIREEYE-MIB", "alertCncPort"),
        ("FE-FIREEYE-MIB", "alertChecksum"),
        ("FE-FIREEYE-MIB", "alertAnalysisType"),
        ("FE-FIREEYE-MIB", "alertProfile"),
        ("FE-FIREEYE-MIB", "alertAction"),
        ("FE-FIREEYE-MIB", "alertInterface"),
        ("FE-FIREEYE-MIB", "alertSensorIp"),
        ("FE-FIREEYE-MIB", "alertSensorHost"),
        ("FE-FIREEYE-MIB", "alertSensorRelease"),
        ("FE-FIREEYE-MIB", "alertSensorProduct"),
        ("FE-FIREEYE-MIB", "alertUrl"),
        ("FE-FIREEYE-MIB", "eventSrcAddrType"),
        ("FE-FIREEYE-MIB", "eventSrcAddr"),
        ("FE-FIREEYE-MIB", "eventDstAddrType"),
        ("FE-FIREEYE-MIB", "eventDstAddr"),
        ("FE-FIREEYE-MIB", "eventSensorAddrType"),
        ("FE-FIREEYE-MIB", "eventSensorAddr"),
        ("FE-FIREEYE-MIB", "isMalicious"),
        ("FE-FIREEYE-MIB", "isRetroactive"))
)
if mibBuilder.loadTexts:
    fireeyeAlert.setStatus(
        "current"
    )

executionAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 3, 0, 2)
)
executionAnomaly.setObjects(
      *(("FE-FIREEYE-MIB", "eventIndex"),
        ("FE-FIREEYE-MIB", "eventId"),
        ("FE-FIREEYE-MIB", "eventType"),
        ("FE-FIREEYE-MIB", "eventDate"),
        ("FE-FIREEYE-MIB", "eventTime"),
        ("FE-FIREEYE-MIB", "eventTraceId"),
        ("FE-FIREEYE-MIB", "eventSrcIp"),
        ("FE-FIREEYE-MIB", "eventDstIp"),
        ("FE-FIREEYE-MIB", "eventSrcMac"),
        ("FE-FIREEYE-MIB", "eventDstMac"),
        ("FE-FIREEYE-MIB", "eventDstPort"),
        ("FE-FIREEYE-MIB", "eventVlan"),
        ("FE-FIREEYE-MIB", "eventProtocol"),
        ("FE-FIREEYE-MIB", "eventProfileId"),
        ("FE-FIREEYE-MIB", "eventOsInfo"),
        ("FE-FIREEYE-MIB", "eventService"),
        ("FE-FIREEYE-MIB", "eventAttackType"),
        ("FE-FIREEYE-MIB", "eventSrcHost"),
        ("FE-FIREEYE-MIB", "eventSrcAddrType"),
        ("FE-FIREEYE-MIB", "eventSrcAddr"),
        ("FE-FIREEYE-MIB", "eventDstAddrType"),
        ("FE-FIREEYE-MIB", "eventDstAddr"))
)
if mibBuilder.loadTexts:
    executionAnomaly.setStatus(
        "current"
    )

networkAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 3, 0, 3)
)
networkAnomaly.setObjects(
      *(("FE-FIREEYE-MIB", "eventIndex"),
        ("FE-FIREEYE-MIB", "eventId"),
        ("FE-FIREEYE-MIB", "eventType"),
        ("FE-FIREEYE-MIB", "eventDate"),
        ("FE-FIREEYE-MIB", "eventTime"),
        ("FE-FIREEYE-MIB", "eventTraceId"),
        ("FE-FIREEYE-MIB", "eventSrcIp"),
        ("FE-FIREEYE-MIB", "eventDstIp"),
        ("FE-FIREEYE-MIB", "eventSrcMac"),
        ("FE-FIREEYE-MIB", "eventDstMac"),
        ("FE-FIREEYE-MIB", "eventDstPort"),
        ("FE-FIREEYE-MIB", "eventVlan"),
        ("FE-FIREEYE-MIB", "eventProtocol"),
        ("FE-FIREEYE-MIB", "eventProfileId"),
        ("FE-FIREEYE-MIB", "eventOsInfo"),
        ("FE-FIREEYE-MIB", "eventService"),
        ("FE-FIREEYE-MIB", "eventSrcHost"),
        ("FE-FIREEYE-MIB", "eventCncNo"),
        ("FE-FIREEYE-MIB", "eventSrcAddrType"),
        ("FE-FIREEYE-MIB", "eventSrcAddr"),
        ("FE-FIREEYE-MIB", "eventDstAddrType"),
        ("FE-FIREEYE-MIB", "eventDstAddr"))
)
if mibBuilder.loadTexts:
    networkAnomaly.setStatus(
        "current"
    )

signatureMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 3, 0, 4)
)
signatureMatch.setObjects(
      *(("FE-FIREEYE-MIB", "eventIndex"),
        ("FE-FIREEYE-MIB", "eventId"),
        ("FE-FIREEYE-MIB", "eventType"),
        ("FE-FIREEYE-MIB", "eventDate"),
        ("FE-FIREEYE-MIB", "eventTime"),
        ("FE-FIREEYE-MIB", "eventTraceId"),
        ("FE-FIREEYE-MIB", "eventSrcIp"),
        ("FE-FIREEYE-MIB", "eventDstIp"),
        ("FE-FIREEYE-MIB", "eventSrcMac"),
        ("FE-FIREEYE-MIB", "eventDstMac"),
        ("FE-FIREEYE-MIB", "eventDstPort"),
        ("FE-FIREEYE-MIB", "eventVlan"),
        ("FE-FIREEYE-MIB", "eventProtocol"),
        ("FE-FIREEYE-MIB", "eventSignatureName"),
        ("FE-FIREEYE-MIB", "eventSignatureType"),
        ("FE-FIREEYE-MIB", "eventSrcHost"),
        ("FE-FIREEYE-MIB", "eventSrcAddrType"),
        ("FE-FIREEYE-MIB", "eventSrcAddr"),
        ("FE-FIREEYE-MIB", "eventDstAddrType"),
        ("FE-FIREEYE-MIB", "eventDstAddr"))
)
if mibBuilder.loadTexts:
    signatureMatch.setStatus(
        "current"
    )

ccConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 3, 0, 9)
)
ccConnect.setObjects(
      *(("FE-FIREEYE-MIB", "eventIndex"),
        ("FE-FIREEYE-MIB", "eventId"),
        ("FE-FIREEYE-MIB", "eventType"),
        ("FE-FIREEYE-MIB", "eventDate"),
        ("FE-FIREEYE-MIB", "eventTime"),
        ("FE-FIREEYE-MIB", "eventTraceId"),
        ("FE-FIREEYE-MIB", "eventSrcIp"),
        ("FE-FIREEYE-MIB", "eventDstIp"),
        ("FE-FIREEYE-MIB", "eventDstPort"),
        ("FE-FIREEYE-MIB", "eventVlan"),
        ("FE-FIREEYE-MIB", "eventProtocol"),
        ("FE-FIREEYE-MIB", "eventSrcHost"),
        ("FE-FIREEYE-MIB", "eventCncNo"),
        ("FE-FIREEYE-MIB", "eventSrcAddrType"),
        ("FE-FIREEYE-MIB", "eventSrcAddr"),
        ("FE-FIREEYE-MIB", "eventDstAddrType"),
        ("FE-FIREEYE-MIB", "eventDstAddr"))
)
if mibBuilder.loadTexts:
    ccConnect.setStatus(
        "current"
    )

ccSigmatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 3, 0, 10)
)
ccSigmatch.setObjects(
      *(("FE-FIREEYE-MIB", "eventIndex"),
        ("FE-FIREEYE-MIB", "eventId"),
        ("FE-FIREEYE-MIB", "eventType"),
        ("FE-FIREEYE-MIB", "eventDate"),
        ("FE-FIREEYE-MIB", "eventTime"),
        ("FE-FIREEYE-MIB", "eventTraceId"),
        ("FE-FIREEYE-MIB", "eventSrcIp"),
        ("FE-FIREEYE-MIB", "eventDstIp"),
        ("FE-FIREEYE-MIB", "eventDstPort"),
        ("FE-FIREEYE-MIB", "eventVlan"),
        ("FE-FIREEYE-MIB", "eventProtocol"),
        ("FE-FIREEYE-MIB", "eventSrcHost"),
        ("FE-FIREEYE-MIB", "eventCncNo"),
        ("FE-FIREEYE-MIB", "eventSrcAddrType"),
        ("FE-FIREEYE-MIB", "eventSrcAddr"),
        ("FE-FIREEYE-MIB", "eventDstAddrType"),
        ("FE-FIREEYE-MIB", "eventDstAddr"))
)
if mibBuilder.loadTexts:
    ccSigmatch.setStatus(
        "current"
    )

osChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 3, 0, 11)
)
osChange.setObjects(
      *(("FE-FIREEYE-MIB", "eventIndex"),
        ("FE-FIREEYE-MIB", "eventId"),
        ("FE-FIREEYE-MIB", "eventType"),
        ("FE-FIREEYE-MIB", "eventDate"),
        ("FE-FIREEYE-MIB", "eventTime"),
        ("FE-FIREEYE-MIB", "eventTraceId"),
        ("FE-FIREEYE-MIB", "eventSrcIp"),
        ("FE-FIREEYE-MIB", "eventDstIp"),
        ("FE-FIREEYE-MIB", "eventSrcMac"),
        ("FE-FIREEYE-MIB", "eventDstMac"),
        ("FE-FIREEYE-MIB", "eventDstPort"),
        ("FE-FIREEYE-MIB", "eventVlan"),
        ("FE-FIREEYE-MIB", "eventProtocol"),
        ("FE-FIREEYE-MIB", "eventSrcHost"),
        ("FE-FIREEYE-MIB", "eventSrcAddrType"),
        ("FE-FIREEYE-MIB", "eventSrcAddr"),
        ("FE-FIREEYE-MIB", "eventDstAddrType"),
        ("FE-FIREEYE-MIB", "eventDstAddr"))
)
if mibBuilder.loadTexts:
    osChange.setStatus(
        "current"
    )

ipsAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 3, 0, 12)
)
ipsAlert.setObjects(
      *(("FE-FIREEYE-MIB", "eventIndex"),
        ("FE-FIREEYE-MIB", "eventId"),
        ("FE-FIREEYE-MIB", "eventType"),
        ("FE-FIREEYE-MIB", "eventTime"),
        ("FE-FIREEYE-MIB", "eventSrcAddrType"),
        ("FE-FIREEYE-MIB", "eventSrcAddr"),
        ("FE-FIREEYE-MIB", "eventSrcPort"),
        ("FE-FIREEYE-MIB", "eventSrcMac"),
        ("FE-FIREEYE-MIB", "eventDstAddrType"),
        ("FE-FIREEYE-MIB", "eventDstAddr"),
        ("FE-FIREEYE-MIB", "eventDstPort"),
        ("FE-FIREEYE-MIB", "eventDstMac"),
        ("FE-FIREEYE-MIB", "ipsSignatureId"),
        ("FE-FIREEYE-MIB", "ipsSignatureRevision"),
        ("FE-FIREEYE-MIB", "ipsMatchCount"),
        ("FE-FIREEYE-MIB", "ipsSeverity"),
        ("FE-FIREEYE-MIB", "ipsSignatureName"),
        ("FE-FIREEYE-MIB", "ipsReferenceId"),
        ("FE-FIREEYE-MIB", "ipsBlockMode"),
        ("FE-FIREEYE-MIB", "ipsAttackTarget"),
        ("FE-FIREEYE-MIB", "alertSensorProduct"),
        ("FE-FIREEYE-MIB", "alertSensorHost"),
        ("FE-FIREEYE-MIB", "alertSensorRelease"),
        ("FE-FIREEYE-MIB", "alertUrl"),
        ("FE-FIREEYE-MIB", "ipsAttackConfirmation"))
)
if mibBuilder.loadTexts:
    ipsAlert.setStatus(
        "current"
    )

feExcessiveTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 0, 1)
)
feExcessiveTemperature.setObjects(
    ("FE-FIREEYE-MIB", "feTemperatureIsHealthy")
)
if mibBuilder.loadTexts:
    feExcessiveTemperature.setStatus(
        "current"
    )

feNormalTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 0, 2)
)
feNormalTemperature.setObjects(
    ("FE-FIREEYE-MIB", "feTemperatureIsHealthy")
)
if mibBuilder.loadTexts:
    feNormalTemperature.setStatus(
        "current"
    )

feIfLinkChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 0, 3)
)
feIfLinkChange.setObjects(
      *(("FE-FIREEYE-MIB", "feIfLinkChangeIfname"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeOldAdminUp"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeNewAdminUp"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeOldLinkUp"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeNewLinkUp"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeOldSpeed"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeNewSpeed"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeOldDuplex"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeNewDuplex"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeOldAutoNeg"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeNewAutoNeg"))
)
if mibBuilder.loadTexts:
    feIfLinkChange.setStatus(
        "current"
    )

feFaasVpnConnectionChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 0, 4)
)
feFaasVpnConnectionChange.setObjects(
    ("FE-FIREEYE-MIB", "feFaasVpnConnected")
)
if mibBuilder.loadTexts:
    feFaasVpnConnectionChange.setStatus(
        "current"
    )

feProcessCrash = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 0, 5)
)
feProcessCrash.setObjects(
      *(("FE-FIREEYE-MIB", "feProcessCrashName"),
        ("FE-FIREEYE-MIB", "feProcessCrashNumFailures"),
        ("FE-FIREEYE-MIB", "feProcessCrashLive"))
)
if mibBuilder.loadTexts:
    feProcessCrash.setStatus(
        "current"
    )

feSyslogRotation = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 0, 6)
)
feSyslogRotation.setObjects(
    ("FE-FIREEYE-MIB", "feSyslogRotationReason")
)
if mibBuilder.loadTexts:
    feSyslogRotation.setStatus(
        "current"
    )

feLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 0, 7)
)
feLogin.setObjects(
      *(("FE-FIREEYE-MIB", "feLoginUsername"),
        ("FE-FIREEYE-MIB", "feLoginUsernameLocal"),
        ("FE-FIREEYE-MIB", "feLoginTimestamp"),
        ("FE-FIREEYE-MIB", "feLoginRemoteAddr"),
        ("FE-FIREEYE-MIB", "feLoginRemoteInetAddrType"),
        ("FE-FIREEYE-MIB", "feLoginRemoteInetAddr"),
        ("FE-FIREEYE-MIB", "feLoginRemoteHostname"),
        ("FE-FIREEYE-MIB", "feLoginPeerId"),
        ("FE-FIREEYE-MIB", "feLoginClientDescr"),
        ("FE-FIREEYE-MIB", "feLoginSessionId"),
        ("FE-FIREEYE-MIB", "feLoginTimestampOrigAuth"),
        ("FE-FIREEYE-MIB", "feLoginAuthMethod"),
        ("FE-FIREEYE-MIB", "feLoginTrusted"),
        ("FE-FIREEYE-MIB", "feLoginAuthSubmethod"),
        ("FE-FIREEYE-MIB", "feLoginRole"))
)
if mibBuilder.loadTexts:
    feLogin.setStatus(
        "current"
    )

feLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 0, 8)
)
feLogout.setObjects(
      *(("FE-FIREEYE-MIB", "feLoginUsername"),
        ("FE-FIREEYE-MIB", "feLoginUsernameLocal"),
        ("FE-FIREEYE-MIB", "feLoginTimestamp"),
        ("FE-FIREEYE-MIB", "feLoginRemoteAddr"),
        ("FE-FIREEYE-MIB", "feLoginRemoteInetAddrType"),
        ("FE-FIREEYE-MIB", "feLoginRemoteInetAddr"),
        ("FE-FIREEYE-MIB", "feLoginRemoteHostname"),
        ("FE-FIREEYE-MIB", "feLoginPeerId"),
        ("FE-FIREEYE-MIB", "feLoginClientDescr"),
        ("FE-FIREEYE-MIB", "feLoginSessionId"),
        ("FE-FIREEYE-MIB", "feLoginTimestampOrigAuth"),
        ("FE-FIREEYE-MIB", "feLoginAuthMethod"),
        ("FE-FIREEYE-MIB", "feLoginTrusted"),
        ("FE-FIREEYE-MIB", "feLoginAuthSubmethod"),
        ("FE-FIREEYE-MIB", "feLoginRole"))
)
if mibBuilder.loadTexts:
    feLogout.setStatus(
        "current"
    )

feRaidFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 0, 1)
)
feRaidFailure.setObjects(
    ("FE-FIREEYE-MIB", "feRaidIsHealthy")
)
if mibBuilder.loadTexts:
    feRaidFailure.setStatus(
        "current"
    )

feRaidRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 0, 2)
)
feRaidRecover.setObjects(
    ("FE-FIREEYE-MIB", "feRaidIsHealthy")
)
if mibBuilder.loadTexts:
    feRaidRecover.setStatus(
        "current"
    )

fePhysicalDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 0, 3)
)
fePhysicalDiskFailure.setObjects(
    ("FE-FIREEYE-MIB", "fePhysicalDiskIsHealthy")
)
if mibBuilder.loadTexts:
    fePhysicalDiskFailure.setStatus(
        "current"
    )

fePhysicalDiskRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 0, 4)
)
fePhysicalDiskRecover.setObjects(
    ("FE-FIREEYE-MIB", "fePhysicalDiskIsHealthy")
)
if mibBuilder.loadTexts:
    fePhysicalDiskRecover.setStatus(
        "current"
    )

fePowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 3, 0, 1)
)
fePowerSupplyFailure.setObjects(
    ("FE-FIREEYE-MIB", "fePowerSupplyOverallIsHealthy")
)
if mibBuilder.loadTexts:
    fePowerSupplyFailure.setStatus(
        "current"
    )

fePowerSupplyRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 3, 0, 2)
)
fePowerSupplyRecover.setObjects(
    ("FE-FIREEYE-MIB", "fePowerSupplyOverallIsHealthy")
)
if mibBuilder.loadTexts:
    fePowerSupplyRecover.setStatus(
        "current"
    )

feFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4, 0, 1)
)
feFanFailure.setObjects(
    ("FE-FIREEYE-MIB", "feFanOverallIsHealthy")
)
if mibBuilder.loadTexts:
    feFanFailure.setStatus(
        "current"
    )

feFanRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4, 0, 2)
)
feFanRecover.setObjects(
    ("FE-FIREEYE-MIB", "feFanOverallIsHealthy")
)
if mibBuilder.loadTexts:
    feFanRecover.setStatus(
        "current"
    )

feLicenseStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 0, 1)
)
feLicenseStateChanged.setObjects(
      *(("FE-FIREEYE-MIB", "feLicenseFeatureName"),
        ("FE-FIREEYE-MIB", "feLicenseNewActiveState"),
        ("FE-FIREEYE-MIB", "feLicenseOldActiveState"))
)
if mibBuilder.loadTexts:
    feLicenseStateChanged.setStatus(
        "current"
    )

feSecurityUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 0, 2)
)
if mibBuilder.loadTexts:
    feSecurityUpdateFailed.setStatus(
        "current"
    )

feTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 0, 3)
)
if mibBuilder.loadTexts:
    feTestTrap.setStatus(
        "current"
    )

feTokenStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 0, 4)
)
feTokenStateChanged.setObjects(
      *(("FE-FIREEYE-MIB", "feTokenFailureReason"),
        ("FE-FIREEYE-MIB", "feTokenApplianceId"),
        ("FE-FIREEYE-MIB", "feTokenLeaseDuration"),
        ("FE-FIREEYE-MIB", "feTokenLeaseIsActive"),
        ("FE-FIREEYE-MIB", "feTokenLeaseTimeRemaining"),
        ("FE-FIREEYE-MIB", "feTokenGraceDuration"),
        ("FE-FIREEYE-MIB", "feTokenGraceIsActive"),
        ("FE-FIREEYE-MIB", "feTokenGraceTimeRemaining"),
        ("FE-FIREEYE-MIB", "feTokenLicenseExpiryTime"),
        ("FE-FIREEYE-MIB", "feTokenLicenseExpiryRequired"),
        ("FE-FIREEYE-MIB", "feTokenLicenseIsActive"))
)
if mibBuilder.loadTexts:
    feTokenStateChanged.setStatus(
        "current"
    )

feTokenDupeDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 0, 5)
)
feTokenDupeDetected.setObjects(
      *(("FE-FIREEYE-MIB", "feTokenLocalUuid"),
        ("FE-FIREEYE-MIB", "feTokenLocalActiveDuration"),
        ("FE-FIREEYE-MIB", "feTokenWinnerUuid"),
        ("FE-FIREEYE-MIB", "feTokenUuidList"),
        ("FE-FIREEYE-MIB", "feTokenUuidActiveDuration"))
)
if mibBuilder.loadTexts:
    feTokenDupeDetected.setStatus(
        "current"
    )

feTokenServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 0, 6)
)
feTokenServerUnreachable.setObjects(
      *(("FE-FIREEYE-MIB", "feTokenApplianceId"),
        ("FE-FIREEYE-MIB", "feTokenFailureReason"))
)
if mibBuilder.loadTexts:
    feTokenServerUnreachable.setStatus(
        "current"
    )

feTokenServerReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 0, 7)
)
feTokenServerReachable.setObjects(
    ("FE-FIREEYE-MIB", "feTokenApplianceId")
)
if mibBuilder.loadTexts:
    feTokenServerReachable.setStatus(
        "current"
    )

feCMSHAUnexpectedFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 12, 0, 1)
)
if mibBuilder.loadTexts:
    feCMSHAUnexpectedFailover.setStatus(
        "current"
    )

feCMSHAManualFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 12, 0, 2)
)
if mibBuilder.loadTexts:
    feCMSHAManualFailover.setStatus(
        "current"
    )

feCMSHANxHealthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 12, 0, 3)
)
feCMSHANxHealthFailure.setObjects(
      *(("FE-FIREEYE-MIB", "feCMSHANxHealthFailureName"),
        ("FE-FIREEYE-MIB", "feCMSHANxHealthFailureType"),
        ("FE-FIREEYE-MIB", "feCMSHANxHealthFailureNx1"),
        ("FE-FIREEYE-MIB", "feCMSHANxHealthFailureNx2"),
        ("FE-FIREEYE-MIB", "feCMSHANxHealthFailureReason"),
        ("FE-FIREEYE-MIB", "feCMSHANxHealthFailureDesc"))
)
if mibBuilder.loadTexts:
    feCMSHANxHealthFailure.setStatus(
        "current"
    )

feMVXClusterStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 12, 0, 4)
)
feMVXClusterStateChanged.setObjects(
      *(("FE-FIREEYE-MIB", "feMVXClusterName"),
        ("FE-FIREEYE-MIB", "feMVXClusterStateChangeDesc"))
)
if mibBuilder.loadTexts:
    feMVXClusterStateChanged.setStatus(
        "current"
    )

feMVXClusterUtilExceedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 12, 0, 5)
)
feMVXClusterUtilExceedThreshold.setObjects(
      *(("FE-FIREEYE-MIB", "feMVXClusterUtilExceedAlarmId"),
        ("FE-FIREEYE-MIB", "feMVXClusterUtilExceedDataValue"))
)
if mibBuilder.loadTexts:
    feMVXClusterUtilExceedThreshold.setStatus(
        "current"
    )

feDeferredQueueThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 13, 0, 1)
)
feDeferredQueueThreshold.setObjects(
    ("FE-FIREEYE-MIB", "feDeferredEmailCount")
)
if mibBuilder.loadTexts:
    feDeferredQueueThreshold.setStatus(
        "current"
    )

feBypassCountThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 13, 0, 2)
)
if mibBuilder.loadTexts:
    feBypassCountThreshold.setStatus(
        "current"
    )

feSmtpInterfaceRefuseConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 13, 0, 3)
)
if mibBuilder.loadTexts:
    feSmtpInterfaceRefuseConnection.setStatus(
        "current"
    )

feSmtpInterfaceRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 13, 0, 4)
)
if mibBuilder.loadTexts:
    feSmtpInterfaceRecover.setStatus(
        "current"
    )

feEMPSBypassStateEntered = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 13, 0, 5)
)
if mibBuilder.loadTexts:
    feEMPSBypassStateEntered.setStatus(
        "current"
    )

feEMPSBypassStateExited = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 13, 0, 6)
)
if mibBuilder.loadTexts:
    feEMPSBypassStateExited.setStatus(
        "current"
    )

feHttpThroughputNotIncrease = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 14, 0, 1)
)
if mibBuilder.loadTexts:
    feHttpThroughputNotIncrease.setStatus(
        "current"
    )

feHardwareBypassEntered = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 14, 0, 2)
)
if mibBuilder.loadTexts:
    feHardwareBypassEntered.setStatus(
        "current"
    )

feDeploymentCheckFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 14, 0, 3)
)
feDeploymentCheckFailure.setObjects(
    ("FE-FIREEYE-MIB", "feDeploymentCheckIsHealthy")
)
if mibBuilder.loadTexts:
    feDeploymentCheckFailure.setStatus(
        "current"
    )

feDeploymentCheckRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 14, 0, 4)
)
feDeploymentCheckRecover.setObjects(
    ("FE-FIREEYE-MIB", "feDeploymentCheckIsHealthy")
)
if mibBuilder.loadTexts:
    feDeploymentCheckRecover.setStatus(
        "current"
    )

feWMPSSizingThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 14, 0, 5)
)
feWMPSSizingThresholdExceeded.setObjects(
    ("FE-FIREEYE-MIB", "feWMPSUtilizationSummary")
)
if mibBuilder.loadTexts:
    feWMPSSizingThresholdExceeded.setStatus(
        "current"
    )

feWMPSSizingThresholdNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 14, 0, 6)
)
feWMPSSizingThresholdNormal.setObjects(
    ("FE-FIREEYE-MIB", "feWMPSUtilizationSummary")
)
if mibBuilder.loadTexts:
    feWMPSSizingThresholdNormal.setStatus(
        "current"
    )

feMVXEnrollmentFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 14, 0, 7)
)
feMVXEnrollmentFailed.setObjects(
      *(("FE-FIREEYE-MIB", "feMVXEnrollmentFailureTime"),
        ("FE-FIREEYE-MIB", "feMVXEnrollmentFailureReason"))
)
if mibBuilder.loadTexts:
    feMVXEnrollmentFailed.setStatus(
        "current"
    )

feMaliciousMaid = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 15, 0, 1)
)
feMaliciousMaid.setObjects(
    ("FE-FIREEYE-MIB", "feMaid")
)
if mibBuilder.loadTexts:
    feMaliciousMaid.setStatus(
        "current"
    )


# Notifications groups

feNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 2)
)
feNotificationsGroup.setObjects(
      *(("FE-FIREEYE-MIB", "fireeyeAlert"),
        ("FE-FIREEYE-MIB", "executionAnomaly"),
        ("FE-FIREEYE-MIB", "networkAnomaly"),
        ("FE-FIREEYE-MIB", "signatureMatch"),
        ("FE-FIREEYE-MIB", "ccConnect"),
        ("FE-FIREEYE-MIB", "ccSigmatch"),
        ("FE-FIREEYE-MIB", "osChange"),
        ("FE-FIREEYE-MIB", "ipsAlert"))
)
if mibBuilder.loadTexts:
    feNotificationsGroup.setStatus(
        "current"
    )

feSystemTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 12)
)
feSystemTrapGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feExcessiveTemperature"),
        ("FE-FIREEYE-MIB", "feNormalTemperature"),
        ("FE-FIREEYE-MIB", "feIfLinkChange"),
        ("FE-FIREEYE-MIB", "feFaasVpnConnectionChange"),
        ("FE-FIREEYE-MIB", "feProcessCrash"),
        ("FE-FIREEYE-MIB", "feSyslogRotation"),
        ("FE-FIREEYE-MIB", "feLogin"),
        ("FE-FIREEYE-MIB", "feLogout"))
)
if mibBuilder.loadTexts:
    feSystemTrapGroup.setStatus(
        "current"
    )

feStorageTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 14)
)
feStorageTrapGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feRaidFailure"),
        ("FE-FIREEYE-MIB", "feRaidRecover"),
        ("FE-FIREEYE-MIB", "fePhysicalDiskFailure"),
        ("FE-FIREEYE-MIB", "fePhysicalDiskRecover"))
)
if mibBuilder.loadTexts:
    feStorageTrapGroup.setStatus(
        "current"
    )

fePowerSupplyTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 16)
)
fePowerSupplyTrapGroup.setObjects(
      *(("FE-FIREEYE-MIB", "fePowerSupplyFailure"),
        ("FE-FIREEYE-MIB", "fePowerSupplyRecover"))
)
if mibBuilder.loadTexts:
    fePowerSupplyTrapGroup.setStatus(
        "current"
    )

feFanHealthTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 18)
)
feFanHealthTrapGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feFanFailure"),
        ("FE-FIREEYE-MIB", "feFanRecover"))
)
if mibBuilder.loadTexts:
    feFanHealthTrapGroup.setStatus(
        "current"
    )

feApplicationTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 20)
)
feApplicationTrapGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feLicenseStateChanged"),
        ("FE-FIREEYE-MIB", "feSecurityUpdateFailed"),
        ("FE-FIREEYE-MIB", "feTestTrap"),
        ("FE-FIREEYE-MIB", "feTokenStateChanged"),
        ("FE-FIREEYE-MIB", "feTokenDupeDetected"),
        ("FE-FIREEYE-MIB", "feTokenServerUnreachable"),
        ("FE-FIREEYE-MIB", "feTokenServerReachable"))
)
if mibBuilder.loadTexts:
    feApplicationTrapGroup.setStatus(
        "current"
    )

feCMSTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 22)
)
feCMSTrapGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feCMSHAUnexpectedFailover"),
        ("FE-FIREEYE-MIB", "feCMSHAManualFailover"),
        ("FE-FIREEYE-MIB", "feCMSHANxHealthFailure"),
        ("FE-FIREEYE-MIB", "feMVXClusterStateChanged"),
        ("FE-FIREEYE-MIB", "feMVXClusterUtilExceedThreshold"))
)
if mibBuilder.loadTexts:
    feCMSTrapGroup.setStatus(
        "current"
    )

feEMPSTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 24)
)
feEMPSTrapGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feDeferredQueueThreshold"),
        ("FE-FIREEYE-MIB", "feBypassCountThreshold"),
        ("FE-FIREEYE-MIB", "feSmtpInterfaceRefuseConnection"),
        ("FE-FIREEYE-MIB", "feSmtpInterfaceRecover"),
        ("FE-FIREEYE-MIB", "feEMPSBypassStateEntered"),
        ("FE-FIREEYE-MIB", "feEMPSBypassStateExited"))
)
if mibBuilder.loadTexts:
    feEMPSTrapGroup.setStatus(
        "current"
    )

feWMPSTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 26)
)
feWMPSTrapGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feHttpThroughputNotIncrease"),
        ("FE-FIREEYE-MIB", "feHardwareBypassEntered"),
        ("FE-FIREEYE-MIB", "feDeploymentCheckFailure"),
        ("FE-FIREEYE-MIB", "feDeploymentCheckRecover"),
        ("FE-FIREEYE-MIB", "feWMPSSizingThresholdExceeded"),
        ("FE-FIREEYE-MIB", "feWMPSSizingThresholdNormal"),
        ("FE-FIREEYE-MIB", "feMVXEnrollmentFailed"))
)
if mibBuilder.loadTexts:
    feWMPSTrapGroup.setStatus(
        "current"
    )

feMASTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 28)
)
feMASTrapGroup.setObjects(
    ("FE-FIREEYE-MIB", "feMaliciousMaid")
)
if mibBuilder.loadTexts:
    feMASTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

feMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25597, 20, 2, 1)
)
feMibCompliance.setObjects(
      *(("FE-FIREEYE-MIB", "feVariablesGroup"),
        ("FE-FIREEYE-MIB", "feNotificationsGroup"),
        ("FE-FIREEYE-MIB", "feSystemInfoGroup"),
        ("FE-FIREEYE-MIB", "feSystemTrapGroup"),
        ("FE-FIREEYE-MIB", "feStorageInfoGroup"),
        ("FE-FIREEYE-MIB", "feStorageTrapGroup"),
        ("FE-FIREEYE-MIB", "fePowerSupplyInfoGroup"),
        ("FE-FIREEYE-MIB", "fePowerSupplyTrapGroup"),
        ("FE-FIREEYE-MIB", "feFanHealthInfoGroup"),
        ("FE-FIREEYE-MIB", "feFanHealthTrapGroup"),
        ("FE-FIREEYE-MIB", "feApplicationInfoGroup"),
        ("FE-FIREEYE-MIB", "feApplicationTrapGroup"),
        ("FE-FIREEYE-MIB", "feCMSInfoGroup"),
        ("FE-FIREEYE-MIB", "feCMSTrapGroup"),
        ("FE-FIREEYE-MIB", "feEMPSInfoGroup"),
        ("FE-FIREEYE-MIB", "feEMPSTrapGroup"),
        ("FE-FIREEYE-MIB", "feWMPSTrapGroup"),
        ("FE-FIREEYE-MIB", "feMASInfoGroup"),
        ("FE-FIREEYE-MIB", "feMASTrapGroup"),
        ("FE-FIREEYE-MIB", "feWMPSInfoGroup"),
        ("FE-FIREEYE-MIB", "feSubmissionInfoGroup"))
)
if mibBuilder.loadTexts:
    feMibCompliance.setStatus(
        "current"
    )

feMibComplianceDeprecated = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25597, 20, 2, 2)
)
feMibComplianceDeprecated.setObjects(
      *(("FE-FIREEYE-MIB", "feDeprecatedSubmissionInfoGroup"),
        ("FE-FIREEYE-MIB", "feDeprecatedPowerSupplyInfoGroup"))
)
if mibBuilder.loadTexts:
    feMibComplianceDeprecated.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FE-FIREEYE-MIB",
    **{"fireeye": fireeye,
       "variables": variables,
       "lms": lms,
       "lmsVersion": lmsVersion,
       "eventTable": eventTable,
       "eventEntry": eventEntry,
       "eventIndex": eventIndex,
       "eventId": eventId,
       "eventType": eventType,
       "eventDate": eventDate,
       "eventTime": eventTime,
       "eventTraceId": eventTraceId,
       "eventSrcIp": eventSrcIp,
       "eventDstIp": eventDstIp,
       "eventSrcMac": eventSrcMac,
       "eventDstMac": eventDstMac,
       "eventDstPort": eventDstPort,
       "eventVlan": eventVlan,
       "eventProtocol": eventProtocol,
       "eventProfileId": eventProfileId,
       "eventOsInfo": eventOsInfo,
       "eventService": eventService,
       "eventAttackType": eventAttackType,
       "eventSignatureName": eventSignatureName,
       "eventSignatureType": eventSignatureType,
       "eventSrcHost": eventSrcHost,
       "eventCncNo": eventCncNo,
       "alertSignatureId": alertSignatureId,
       "alertCncHost": alertCncHost,
       "alertCncPort": alertCncPort,
       "alertChecksum": alertChecksum,
       "alertAnalysisType": alertAnalysisType,
       "alertProfile": alertProfile,
       "alertAction": alertAction,
       "alertInterface": alertInterface,
       "alertSensorIp": alertSensorIp,
       "alertSensorHost": alertSensorHost,
       "alertSensorProduct": alertSensorProduct,
       "alertSensorRelease": alertSensorRelease,
       "alertUrl": alertUrl,
       "eventSrcAddrType": eventSrcAddrType,
       "eventSrcAddr": eventSrcAddr,
       "eventDstAddrType": eventDstAddrType,
       "eventDstAddr": eventDstAddr,
       "eventSensorAddrType": eventSensorAddrType,
       "eventSensorAddr": eventSensorAddr,
       "eventSrcPort": eventSrcPort,
       "eventDateTime": eventDateTime,
       "ipsSignatureId": ipsSignatureId,
       "ipsSignatureRevision": ipsSignatureRevision,
       "ipsMatchCount": ipsMatchCount,
       "ipsSeverity": ipsSeverity,
       "ipsSignatureName": ipsSignatureName,
       "ipsReferenceId": ipsReferenceId,
       "ipsBlockMode": ipsBlockMode,
       "ipsAttackTarget": ipsAttackTarget,
       "isMalicious": isMalicious,
       "ipsAttackConfirmation": ipsAttackConfirmation,
       "isRetroactive": isRetroactive,
       "eventCount": eventCount,
       "notifications": notifications,
       "notificationPrefix": notificationPrefix,
       "fireeyeAlert": fireeyeAlert,
       "executionAnomaly": executionAnomaly,
       "networkAnomaly": networkAnomaly,
       "signatureMatch": signatureMatch,
       "ccConnect": ccConnect,
       "ccSigmatch": ccSigmatch,
       "osChange": osChange,
       "ipsAlert": ipsAlert,
       "feCommon": feCommon,
       "feSystem": feSystem,
       "feSystemTraps": feSystemTraps,
       "feExcessiveTemperature": feExcessiveTemperature,
       "feNormalTemperature": feNormalTemperature,
       "feIfLinkChange": feIfLinkChange,
       "feFaasVpnConnectionChange": feFaasVpnConnectionChange,
       "feProcessCrash": feProcessCrash,
       "feSyslogRotation": feSyslogRotation,
       "feLogin": feLogin,
       "feLogout": feLogout,
       "feSystemInfo": feSystemInfo,
       "feSystemStatus": feSystemStatus,
       "feHardwareModel": feHardwareModel,
       "feSerialNumber": feSerialNumber,
       "feTemperatureValue": feTemperatureValue,
       "feTemperatureStatus": feTemperatureStatus,
       "feTemperatureIsHealthy": feTemperatureIsHealthy,
       "feIfLinkChangeIfname": feIfLinkChangeIfname,
       "feIfLinkChangeOldAdminUp": feIfLinkChangeOldAdminUp,
       "feIfLinkChangeNewAdminUp": feIfLinkChangeNewAdminUp,
       "feIfLinkChangeOldLinkUp": feIfLinkChangeOldLinkUp,
       "feIfLinkChangeNewLinkUp": feIfLinkChangeNewLinkUp,
       "feIfLinkChangeOldSpeed": feIfLinkChangeOldSpeed,
       "feIfLinkChangeNewSpeed": feIfLinkChangeNewSpeed,
       "feIfLinkChangeOldDuplex": feIfLinkChangeOldDuplex,
       "feIfLinkChangeNewDuplex": feIfLinkChangeNewDuplex,
       "feIfLinkChangeOldAutoNeg": feIfLinkChangeOldAutoNeg,
       "feIfLinkChangeNewAutoNeg": feIfLinkChangeNewAutoNeg,
       "feFaasVpnConnected": feFaasVpnConnected,
       "feProcessCrashName": feProcessCrashName,
       "feProcessCrashNumFailures": feProcessCrashNumFailures,
       "feProcessCrashLive": feProcessCrashLive,
       "feSyslogRotationReason": feSyslogRotationReason,
       "feLoginUsername": feLoginUsername,
       "feLoginUsernameLocal": feLoginUsernameLocal,
       "feLoginTimestamp": feLoginTimestamp,
       "feLoginRemoteAddr": feLoginRemoteAddr,
       "feLoginRemoteInetAddrType": feLoginRemoteInetAddrType,
       "feLoginRemoteInetAddr": feLoginRemoteInetAddr,
       "feLoginRemoteHostname": feLoginRemoteHostname,
       "feLoginPeerId": feLoginPeerId,
       "feLoginClientDescr": feLoginClientDescr,
       "feLoginSessionId": feLoginSessionId,
       "feLoginTimestampOrigAuth": feLoginTimestampOrigAuth,
       "feLoginAuthMethod": feLoginAuthMethod,
       "feLoginTrusted": feLoginTrusted,
       "feLoginAuthSubmethod": feLoginAuthSubmethod,
       "feLoginRole": feLoginRole,
       "feAwsInstanceId": feAwsInstanceId,
       "feAwsInstanceType": feAwsInstanceType,
       "feAwsImageId": feAwsImageId,
       "feStorage": feStorage,
       "feStorageTraps": feStorageTraps,
       "feRaidFailure": feRaidFailure,
       "feRaidRecover": feRaidRecover,
       "fePhysicalDiskFailure": fePhysicalDiskFailure,
       "fePhysicalDiskRecover": fePhysicalDiskRecover,
       "feStorageInfo": feStorageInfo,
       "feRaidStatus": feRaidStatus,
       "feRaidIsHealthy": feRaidIsHealthy,
       "fePhysicalDiskTable": fePhysicalDiskTable,
       "fePhysicalDiskEntry": fePhysicalDiskEntry,
       "fePhysicalDiskIndex": fePhysicalDiskIndex,
       "fePhysicalDiskName": fePhysicalDiskName,
       "fePhysicalDiskStatus": fePhysicalDiskStatus,
       "fePhysicalDiskIsHealthy": fePhysicalDiskIsHealthy,
       "fePhysicalDiskDeviceSupport": fePhysicalDiskDeviceSupport,
       "fePhysicalDiskSelfAssess": fePhysicalDiskSelfAssess,
       "fePhysicalDiskTotalBytes": fePhysicalDiskTotalBytes,
       "fePowerSupply": fePowerSupply,
       "fePowerSupplyTraps": fePowerSupplyTraps,
       "fePowerSupplyFailure": fePowerSupplyFailure,
       "fePowerSupplyRecover": fePowerSupplyRecover,
       "fePowerSupplyInfo": fePowerSupplyInfo,
       "fePowerSupplyOverallStatus": fePowerSupplyOverallStatus,
       "fePowerSupplyOverallIsHealthy": fePowerSupplyOverallIsHealthy,
       "fePowerSupplyTable": fePowerSupplyTable,
       "fePowerSupplyEntry": fePowerSupplyEntry,
       "fePowerSupplyIndex": fePowerSupplyIndex,
       "fePowerSupplyStatus": fePowerSupplyStatus,
       "fePowerSupplyIsHealthy": fePowerSupplyIsHealthy,
       "feFanHealth": feFanHealth,
       "feFanHealthTraps": feFanHealthTraps,
       "feFanFailure": feFanFailure,
       "feFanRecover": feFanRecover,
       "feFanHealthInfo": feFanHealthInfo,
       "feFanOverallStatus": feFanOverallStatus,
       "feFanOverallIsHealthy": feFanOverallIsHealthy,
       "feFanStatusTable": feFanStatusTable,
       "feFanStatusEntry": feFanStatusEntry,
       "feFanIndex": feFanIndex,
       "feFanStatus": feFanStatus,
       "feFanIsHealthy": feFanIsHealthy,
       "feFanSpeed": feFanSpeed,
       "feFanName": feFanName,
       "feApplication": feApplication,
       "feApplicationTraps": feApplicationTraps,
       "feLicenseStateChanged": feLicenseStateChanged,
       "feSecurityUpdateFailed": feSecurityUpdateFailed,
       "feTestTrap": feTestTrap,
       "feTokenStateChanged": feTokenStateChanged,
       "feTokenDupeDetected": feTokenDupeDetected,
       "feTokenServerUnreachable": feTokenServerUnreachable,
       "feTokenServerReachable": feTokenServerReachable,
       "feApplicationInfo": feApplicationInfo,
       "feInstalledSystemImage": feInstalledSystemImage,
       "feSystemImageVersionCurrent": feSystemImageVersionCurrent,
       "feSystemImageVersionLatest": feSystemImageVersionLatest,
       "feIsSystemImageLatest": feIsSystemImageLatest,
       "feSecurityContentVersion": feSecurityContentVersion,
       "feLastContentUpdatePassed": feLastContentUpdatePassed,
       "feLastContentUpdateTime": feLastContentUpdateTime,
       "feGIVersionTable": feGIVersionTable,
       "feGIVersionEntry": feGIVersionEntry,
       "feGIIndex": feGIIndex,
       "feGIName": feGIName,
       "feGIVersion": feGIVersion,
       "feGIEnabled": feGIEnabled,
       "feGIInstallDateTime": feGIInstallDateTime,
       "feActiveVMs": feActiveVMs,
       "feProductLicenseActive": feProductLicenseActive,
       "feContentLicenseActive": feContentLicenseActive,
       "feSupportLicenseActive": feSupportLicenseActive,
       "feLicenseFeatureName": feLicenseFeatureName,
       "feLicenseNewActiveState": feLicenseNewActiveState,
       "feLicenseOldActiveState": feLicenseOldActiveState,
       "feLicenseFeatureTable": feLicenseFeatureTable,
       "feLicenseFeatureEntry": feLicenseFeatureEntry,
       "feLicenseFeature": feLicenseFeature,
       "feLicenseFeatureDescr": feLicenseFeatureDescr,
       "feLicenseActive": feLicenseActive,
       "feLicenseExpiration": feLicenseExpiration,
       "feLicenseDaysUntilExpiration": feLicenseDaysUntilExpiration,
       "feTokenFailureReason": feTokenFailureReason,
       "feTokenApplianceId": feTokenApplianceId,
       "feTokenLeaseDuration": feTokenLeaseDuration,
       "feTokenLeaseIsActive": feTokenLeaseIsActive,
       "feTokenLeaseTimeRemaining": feTokenLeaseTimeRemaining,
       "feTokenGraceDuration": feTokenGraceDuration,
       "feTokenGraceIsActive": feTokenGraceIsActive,
       "feTokenGraceTimeRemaining": feTokenGraceTimeRemaining,
       "feTokenLicenseExpiryTime": feTokenLicenseExpiryTime,
       "feTokenLicenseExpiryRequired": feTokenLicenseExpiryRequired,
       "feTokenLicenseIsActive": feTokenLicenseIsActive,
       "feTokenLocalUuid": feTokenLocalUuid,
       "feTokenLocalActiveDuration": feTokenLocalActiveDuration,
       "feTokenWinnerUuid": feTokenWinnerUuid,
       "feTokenUuidList": feTokenUuidList,
       "feTokenUuidActiveDuration": feTokenUuidActiveDuration,
       "feSubmission": feSubmission,
       "feSubmissionInfo": feSubmissionInfo,
       "feSubmissionCountL": feSubmissionCountL,
       "feSubmissionCountH": feSubmissionCountH,
       "feSubmissionDoneCountL": feSubmissionDoneCountL,
       "feSubmissionDoneCountH": feSubmissionDoneCountH,
       "feSubmissionTimedOutCountL": feSubmissionTimedOutCountL,
       "feSubmissionTimedOutCountH": feSubmissionTimedOutCountH,
       "feSubmissionAging50to74CntL": feSubmissionAging50to74CntL,
       "feSubmissionAging50to74CntH": feSubmissionAging50to74CntH,
       "feSubmissionAging75to100CntL": feSubmissionAging75to100CntL,
       "feSubmissionAging75to100CntH": feSubmissionAging75to100CntH,
       "feCMS": feCMS,
       "feCMSTraps": feCMSTraps,
       "feCMSHAUnexpectedFailover": feCMSHAUnexpectedFailover,
       "feCMSHAManualFailover": feCMSHAManualFailover,
       "feCMSHANxHealthFailure": feCMSHANxHealthFailure,
       "feMVXClusterStateChanged": feMVXClusterStateChanged,
       "feMVXClusterUtilExceedThreshold": feMVXClusterUtilExceedThreshold,
       "feCMSInfo": feCMSInfo,
       "feTotalAppliancesAttached": feTotalAppliancesAttached,
       "feTotalWMPSAttached": feTotalWMPSAttached,
       "feTotalEMPSAttached": feTotalEMPSAttached,
       "feTotalFMPSAttached": feTotalFMPSAttached,
       "feTotalMASAttached": feTotalMASAttached,
       "feCMSApplianceTable": feCMSApplianceTable,
       "feCMSApplianceEntry": feCMSApplianceEntry,
       "feCMSApplianceIndex": feCMSApplianceIndex,
       "feCMSApplianceName": feCMSApplianceName,
       "feCMSApplianceDiskSpacePassed": feCMSApplianceDiskSpacePassed,
       "feCMSApplianceFanPassed": feCMSApplianceFanPassed,
       "feCMSAppliancePowerSupplyPassed": feCMSAppliancePowerSupplyPassed,
       "feCMSApplianceRaidPassed": feCMSApplianceRaidPassed,
       "feCMSApplianceTemperaturePassed": feCMSApplianceTemperaturePassed,
       "feCMSHANxHealthFailureName": feCMSHANxHealthFailureName,
       "feCMSHANxHealthFailureType": feCMSHANxHealthFailureType,
       "feCMSHANxHealthFailureNx1": feCMSHANxHealthFailureNx1,
       "feCMSHANxHealthFailureNx2": feCMSHANxHealthFailureNx2,
       "feCMSHANxHealthFailureReason": feCMSHANxHealthFailureReason,
       "feCMSHANxHealthFailureDesc": feCMSHANxHealthFailureDesc,
       "feMVXClusterName": feMVXClusterName,
       "feMVXClusterStateChangeDesc": feMVXClusterStateChangeDesc,
       "feMVXClusterUtilExceedAlarmId": feMVXClusterUtilExceedAlarmId,
       "feMVXClusterUtilExceedDataValue": feMVXClusterUtilExceedDataValue,
       "feEMPS": feEMPS,
       "feEMPSTraps": feEMPSTraps,
       "feDeferredQueueThreshold": feDeferredQueueThreshold,
       "feBypassCountThreshold": feBypassCountThreshold,
       "feSmtpInterfaceRefuseConnection": feSmtpInterfaceRefuseConnection,
       "feSmtpInterfaceRecover": feSmtpInterfaceRecover,
       "feEMPSBypassStateEntered": feEMPSBypassStateEntered,
       "feEMPSBypassStateExited": feEMPSBypassStateExited,
       "feEMPSInfo": feEMPSInfo,
       "feTotalEmailCount": feTotalEmailCount,
       "feTotalEmailCountH": feTotalEmailCountH,
       "feTotalEmailCountL": feTotalEmailCountL,
       "feInfectedEmailCount": feInfectedEmailCount,
       "feInfectedEmailCountH": feInfectedEmailCountH,
       "feInfectedEmailCountL": feInfectedEmailCountL,
       "feAnalyzedEmailCount": feAnalyzedEmailCount,
       "feAnalyzedEmailCountH": feAnalyzedEmailCountH,
       "feAnalyzedEmailCountL": feAnalyzedEmailCountL,
       "feTotalUrlCount": feTotalUrlCount,
       "feTotalUrlCountH": feTotalUrlCountH,
       "feTotalUrlCountL": feTotalUrlCountL,
       "feInfectedUrlCount": feInfectedUrlCount,
       "feInfectedUrlCountH": feInfectedUrlCountH,
       "feInfectedUrlCountL": feInfectedUrlCountL,
       "feAnalyzedUrlCount": feAnalyzedUrlCount,
       "feAnalyzedUrlCountH": feAnalyzedUrlCountH,
       "feAnalyzedUrlCountL": feAnalyzedUrlCountL,
       "feTotalAttachmentCount": feTotalAttachmentCount,
       "feTotalAttachmentCountH": feTotalAttachmentCountH,
       "feTotalAttachmentCountL": feTotalAttachmentCountL,
       "feInfectedAttachmentCount": feInfectedAttachmentCount,
       "feInfectedAttachmentCountH": feInfectedAttachmentCountH,
       "feInfectedAttachmentCountL": feInfectedAttachmentCountL,
       "feAnalyzedAttachmentCount": feAnalyzedAttachmentCount,
       "feAnalyzedAttachmentCountH": feAnalyzedAttachmentCountH,
       "feAnalyzedAttachmentCountL": feAnalyzedAttachmentCountL,
       "feTotalEmailHasAttachment": feTotalEmailHasAttachment,
       "feTotalEmailHasAttachmentH": feTotalEmailHasAttachmentH,
       "feTotalEmailHasAttachmentL": feTotalEmailHasAttachmentL,
       "feTotalEmailHasUrl": feTotalEmailHasUrl,
       "feTotalEmailHasUrlH": feTotalEmailHasUrlH,
       "feTotalEmailHasUrlL": feTotalEmailHasUrlL,
       "feTotalEmailHasBadAttachment": feTotalEmailHasBadAttachment,
       "feTotalEmailHasBadAttachmentH": feTotalEmailHasBadAttachmentH,
       "feTotalEmailHasBadAttachmentL": feTotalEmailHasBadAttachmentL,
       "feTotalEmailHasBadUrl": feTotalEmailHasBadUrl,
       "feTotalEmailHasBadUrlH": feTotalEmailHasBadUrlH,
       "feTotalEmailHasBadUrlL": feTotalEmailHasBadUrlL,
       "feeQuarantineUsage": feeQuarantineUsage,
       "feBypassEmailCount": feBypassEmailCount,
       "feBypassEmailCountH": feBypassEmailCountH,
       "feBypassEmailCountL": feBypassEmailCountL,
       "feDeferredEmailCount": feDeferredEmailCount,
       "feHoldQueueEmailCount": feHoldQueueEmailCount,
       "feOpenSmtpConnections": feOpenSmtpConnections,
       "feIncomingEmailCount": feIncomingEmailCount,
       "feActiveEmailCount": feActiveEmailCount,
       "feDropEmailCount": feDropEmailCount,
       "feSamplingEmailStartTime": feSamplingEmailStartTime,
       "feSamplingEmailEndTime": feSamplingEmailEndTime,
       "feSamplingEmailReceivedRate": feSamplingEmailReceivedRate,
       "feWMPS": feWMPS,
       "feWMPSTraps": feWMPSTraps,
       "feHttpThroughputNotIncrease": feHttpThroughputNotIncrease,
       "feHardwareBypassEntered": feHardwareBypassEntered,
       "feDeploymentCheckFailure": feDeploymentCheckFailure,
       "feDeploymentCheckRecover": feDeploymentCheckRecover,
       "feWMPSSizingThresholdExceeded": feWMPSSizingThresholdExceeded,
       "feWMPSSizingThresholdNormal": feWMPSSizingThresholdNormal,
       "feMVXEnrollmentFailed": feMVXEnrollmentFailed,
       "feWMPSInfo": feWMPSInfo,
       "feDeploymentCheckStatus": feDeploymentCheckStatus,
       "feDeploymentCheckIsHealthy": feDeploymentCheckIsHealthy,
       "feDeploymentCheckMessage": feDeploymentCheckMessage,
       "feDeploymentCheckStartTime": feDeploymentCheckStartTime,
       "feDeploymentCheckEndTime": feDeploymentCheckEndTime,
       "feDeploymentCheckDataSize": feDeploymentCheckDataSize,
       "feDeploymentCheckPktCount": feDeploymentCheckPktCount,
       "feDeploymentCheckReTransPktCount": feDeploymentCheckReTransPktCount,
       "feDeploymentCheckDupAckPktCount": feDeploymentCheckDupAckPktCount,
       "feDeploymentCheckOOOPktCount": feDeploymentCheckOOOPktCount,
       "feDeploymentCheckAckUsnPktCount": feDeploymentCheckAckUsnPktCount,
       "feDeploymentCheckPSegNCPktCount": feDeploymentCheckPSegNCPktCount,
       "feDeploymentCheckMFormedPktCount": feDeploymentCheckMFormedPktCount,
       "feDeploymentCheckStreamCount": feDeploymentCheckStreamCount,
       "feDeploymentCheckAsymStreamCount": feDeploymentCheckAsymStreamCount,
       "feWMPSDetection": feWMPSDetection,
       "feWMPSDetectionStatsTable": feWMPSDetectionStatsTable,
       "feWMPSDetectionStatsEntry": feWMPSDetectionStatsEntry,
       "feWMPSDetectionStatsTimeSpan": feWMPSDetectionStatsTimeSpan,
       "feWMPSAPTAttackCount": feWMPSAPTAttackCount,
       "feWMPSAPTAttackCountH": feWMPSAPTAttackCountH,
       "feWMPSAPTAttackCountL": feWMPSAPTAttackCountL,
       "feWMPSNewGlobalThreatCount": feWMPSNewGlobalThreatCount,
       "feWMPSNewGlobalThreatCountH": feWMPSNewGlobalThreatCountH,
       "feWMPSNewGlobalThreatCountL": feWMPSNewGlobalThreatCountL,
       "feWMPSInfectedHostCount": feWMPSInfectedHostCount,
       "feWMPSInfectedHostCountH": feWMPSInfectedHostCountH,
       "feWMPSInfectedHostCountL": feWMPSInfectedHostCountL,
       "feWMPSObjectsAnalyzedCount": feWMPSObjectsAnalyzedCount,
       "feWMPSObjectsAnalyzedCountH": feWMPSObjectsAnalyzedCountH,
       "feWMPSObjectsAnalyzedCountL": feWMPSObjectsAnalyzedCountL,
       "feWMPSURLsAnalyzedCount": feWMPSURLsAnalyzedCount,
       "feWMPSURLsAnalyzedCountH": feWMPSURLsAnalyzedCountH,
       "feWMPSURLsAnalyzedCountL": feWMPSURLsAnalyzedCountL,
       "feWMPSURLsMaliciousCount": feWMPSURLsMaliciousCount,
       "feWMPSURLsMaliciousCountH": feWMPSURLsMaliciousCountH,
       "feWMPSURLsMaliciousCountL": feWMPSURLsMaliciousCountL,
       "feWMPSDetectionStatsIndex": feWMPSDetectionStatsIndex,
       "feWMPSAlertTable": feWMPSAlertTable,
       "feWMPSAlertEntry": feWMPSAlertEntry,
       "feWMPSAlertTimeSpan": feWMPSAlertTimeSpan,
       "feWMPSAlertName": feWMPSAlertName,
       "feWMPSAlertCount": feWMPSAlertCount,
       "feWMPSAlertCountH": feWMPSAlertCountH,
       "feWMPSAlertCountL": feWMPSAlertCountL,
       "feWMPSAlertIndex1": feWMPSAlertIndex1,
       "feWMPSAlertIndex2": feWMPSAlertIndex2,
       "feWMPSThreatTable": feWMPSThreatTable,
       "feWMPSThreatEntry": feWMPSThreatEntry,
       "feWMPSThreatTimeSpan": feWMPSThreatTimeSpan,
       "feWMPSThreatName": feWMPSThreatName,
       "feWMPSThreatCount": feWMPSThreatCount,
       "feWMPSThreatCountH": feWMPSThreatCountH,
       "feWMPSThreatCountL": feWMPSThreatCountL,
       "feWMPSThreatIndex1": feWMPSThreatIndex1,
       "feWMPSThreatIndex2": feWMPSThreatIndex2,
       "feWMPSFileTypeTable": feWMPSFileTypeTable,
       "feWMPSFileTypeEntry": feWMPSFileTypeEntry,
       "feWMPSFileTypeTimeSpan": feWMPSFileTypeTimeSpan,
       "feWMPSFileTypeName": feWMPSFileTypeName,
       "feWMPSFileTypeCount": feWMPSFileTypeCount,
       "feWMPSFileTypeCountH": feWMPSFileTypeCountH,
       "feWMPSFileTypeCountL": feWMPSFileTypeCountL,
       "feWMPSFileTypeIndex1": feWMPSFileTypeIndex1,
       "feWMPSFileTypeIndex2": feWMPSFileTypeIndex2,
       "feWMPSSizing": feWMPSSizing,
       "feWMPSUtilizationSummary": feWMPSUtilizationSummary,
       "feWMPSWebAnalysisUtilization": feWMPSWebAnalysisUtilization,
       "feWMPSWebAnalysisUtilizationStat": feWMPSWebAnalysisUtilizationStat,
       "feWMPSBinaryAnalysisBacklog": feWMPSBinaryAnalysisBacklog,
       "feWMPSBinaryAnalysisBacklogStat": feWMPSBinaryAnalysisBacklogStat,
       "feWMPSCurrentWebSessions": feWMPSCurrentWebSessions,
       "feWMPSCurrentWebSessionStat": feWMPSCurrentWebSessionStat,
       "feWMPSTotalBandwidth": feWMPSTotalBandwidth,
       "feWMPSTotalBandwidthStat": feWMPSTotalBandwidthStat,
       "feMVXEnrollmentFailureTime": feMVXEnrollmentFailureTime,
       "feMVXEnrollmentFailureReason": feMVXEnrollmentFailureReason,
       "feWMPSSubmission": feWMPSSubmission,
       "feWMPSSubmissionCountL": feWMPSSubmissionCountL,
       "feWMPSSubmissionCountH": feWMPSSubmissionCountH,
       "feWMPSSubmissionDoneCountL": feWMPSSubmissionDoneCountL,
       "feWMPSSubmissionDoneCountH": feWMPSSubmissionDoneCountH,
       "feWMPSSubmissionTimedOutCountL": feWMPSSubmissionTimedOutCountL,
       "feWMPSSubmissionTimedOutCountH": feWMPSSubmissionTimedOutCountH,
       "feWMPSSubmissionAging50to74CntL": feWMPSSubmissionAging50to74CntL,
       "feWMPSSubmissionAging50to74CntH": feWMPSSubmissionAging50to74CntH,
       "feWMPSSubmissionAging75to100CntL": feWMPSSubmissionAging75to100CntL,
       "feWMPSSubmissionAging75to100CntH": feWMPSSubmissionAging75to100CntH,
       "fePercentageInputTrafficLost": fePercentageInputTrafficLost,
       "fePercentageFlowIncompleteData": fePercentageFlowIncompleteData,
       "feMAS": feMAS,
       "feMASTraps": feMASTraps,
       "feMaliciousMaid": feMaliciousMaid,
       "feMASInfo": feMASInfo,
       "feTotalObjectAnalyzedCount": feTotalObjectAnalyzedCount,
       "feTotalObjectAnalyzedCountH": feTotalObjectAnalyzedCountH,
       "feTotalObjectAnalyzedCountL": feTotalObjectAnalyzedCountL,
       "feTotalMaliciousObjectCount": feTotalMaliciousObjectCount,
       "feTotalMaliciousObjectCountH": feTotalMaliciousObjectCountH,
       "feTotalMaliciousObjectCountL": feTotalMaliciousObjectCountL,
       "feTotalUrlAnalyzedCount": feTotalUrlAnalyzedCount,
       "feTotalUrlAnalyzedCountH": feTotalUrlAnalyzedCountH,
       "feTotalUrlAnalyzedCountL": feTotalUrlAnalyzedCountL,
       "feTotalMaliciousUrlCount": feTotalMaliciousUrlCount,
       "feTotalMaliciousUrlCountH": feTotalMaliciousUrlCountH,
       "feTotalMaliciousUrlCountL": feTotalMaliciousUrlCountL,
       "feTotalFileUploadedCount": feTotalFileUploadedCount,
       "feTotalFileUploadedCountH": feTotalFileUploadedCountH,
       "feTotalFileUploadedCountL": feTotalFileUploadedCountL,
       "feTotalMaliciousFileCount": feTotalMaliciousFileCount,
       "feTotalMaliciousFileCountH": feTotalMaliciousFileCountH,
       "feTotalMaliciousFileCountL": feTotalMaliciousFileCountL,
       "feTotalLiveModeCount": feTotalLiveModeCount,
       "feTotalLiveModeCountH": feTotalLiveModeCountH,
       "feTotalLiveModeCountL": feTotalLiveModeCountL,
       "feTotalMaliciousLiveModeCount": feTotalMaliciousLiveModeCount,
       "feTotalMaliciousLiveModeCountH": feTotalMaliciousLiveModeCountH,
       "feTotalMaliciousLiveModeCountL": feTotalMaliciousLiveModeCountL,
       "feMaid": feMaid,
       "feMSM": feMSM,
       "feMSMTraps": feMSMTraps,
       "feMSMInfo": feMSMInfo,
       "feMibAdminInfo": feMibAdminInfo,
       "fireeyeMibModule": fireeyeMibModule,
       "feMibCompliances": feMibCompliances,
       "feMibCompliance": feMibCompliance,
       "feMibComplianceDeprecated": feMibComplianceDeprecated,
       "feMibGroups": feMibGroups,
       "feVariablesGroup": feVariablesGroup,
       "feNotificationsGroup": feNotificationsGroup,
       "feSystemInfoGroup": feSystemInfoGroup,
       "feSystemTrapGroup": feSystemTrapGroup,
       "feStorageInfoGroup": feStorageInfoGroup,
       "feStorageTrapGroup": feStorageTrapGroup,
       "fePowerSupplyInfoGroup": fePowerSupplyInfoGroup,
       "fePowerSupplyTrapGroup": fePowerSupplyTrapGroup,
       "feFanHealthInfoGroup": feFanHealthInfoGroup,
       "feFanHealthTrapGroup": feFanHealthTrapGroup,
       "feApplicationInfoGroup": feApplicationInfoGroup,
       "feApplicationTrapGroup": feApplicationTrapGroup,
       "feCMSInfoGroup": feCMSInfoGroup,
       "feCMSTrapGroup": feCMSTrapGroup,
       "feEMPSInfoGroup": feEMPSInfoGroup,
       "feEMPSTrapGroup": feEMPSTrapGroup,
       "feWMPSInfoGroup": feWMPSInfoGroup,
       "feWMPSTrapGroup": feWMPSTrapGroup,
       "feMASInfoGroup": feMASInfoGroup,
       "feMASTrapGroup": feMASTrapGroup,
       "feSubmissionInfoGroup": feSubmissionInfoGroup,
       "feMibDeprecatedGroups": feMibDeprecatedGroups,
       "feDeprecatedSubmissionInfoGroup": feDeprecatedSubmissionInfoGroup,
       "feDeprecatedPowerSupplyInfoGroup": feDeprecatedPowerSupplyInfoGroup}
)
