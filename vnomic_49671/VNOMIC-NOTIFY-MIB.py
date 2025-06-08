# SNMP MIB module (VNOMIC-NOTIFY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/vnomic_49671/VNOMIC-NOTIFY-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 19:13:06 2025
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

(HostStateID,
 HostStateType,
 NotifyType,
 ServiceStateID,
 vnomic) = mibBuilder.importSymbols(
    "VNOMIC-ROOT-MIB",
    "HostStateID",
    "HostStateType",
    "NotifyType",
    "ServiceStateID",
    "vnomic")


# MODULE-IDENTITY

vnomicNotify = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 49671, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VnomicHostEventTable_Object = MibTable
vnomicHostEventTable = _VnomicHostEventTable_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 1)
)
if mibBuilder.loadTexts:
    vnomicHostEventTable.setStatus("current")
_VnomicHostEventEntry_Object = MibTableRow
vnomicHostEventEntry = _VnomicHostEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 1, 1)
)
vnomicHostEventEntry.setIndexNames(
    (0, "VNOMIC-NOTIFY-MIB", "vnHostEventIndex"),
)
if mibBuilder.loadTexts:
    vnomicHostEventEntry.setStatus("current")


class _VnHostEventIndex_Type(Integer32):
    """Custom type vnHostEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VnHostEventIndex_Type.__name__ = "Integer32"
_VnHostEventIndex_Object = MibTableColumn
vnHostEventIndex = _VnHostEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 1, 1, 1),
    _VnHostEventIndex_Type()
)
vnHostEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vnHostEventIndex.setStatus("current")
_VnHostname_Type = OctetString
_VnHostname_Object = MibTableColumn
vnHostname = _VnHostname_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 1, 1, 2),
    _VnHostname_Type()
)
vnHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnHostname.setStatus("current")
_VnHostAlias_Type = OctetString
_VnHostAlias_Object = MibTableColumn
vnHostAlias = _VnHostAlias_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 1, 1, 3),
    _VnHostAlias_Type()
)
vnHostAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnHostAlias.setStatus("current")
_VnHostStateID_Type = HostStateID
_VnHostStateID_Object = MibTableColumn
vnHostStateID = _VnHostStateID_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 1, 1, 4),
    _VnHostStateID_Type()
)
vnHostStateID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnHostStateID.setStatus("current")
_VnHostStateType_Type = HostStateType
_VnHostStateType_Object = MibTableColumn
vnHostStateType = _VnHostStateType_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 1, 1, 5),
    _VnHostStateType_Type()
)
vnHostStateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnHostStateType.setStatus("current")
_VnHostAttempt_Type = Integer32
_VnHostAttempt_Object = MibTableColumn
vnHostAttempt = _VnHostAttempt_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 1, 1, 6),
    _VnHostAttempt_Type()
)
vnHostAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnHostAttempt.setStatus("current")
_VnHostDurationSec_Type = Integer32
_VnHostDurationSec_Object = MibTableColumn
vnHostDurationSec = _VnHostDurationSec_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 1, 1, 7),
    _VnHostDurationSec_Type()
)
vnHostDurationSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnHostDurationSec.setStatus("current")
_VnHostGroupName_Type = OctetString
_VnHostGroupName_Object = MibTableColumn
vnHostGroupName = _VnHostGroupName_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 1, 1, 8),
    _VnHostGroupName_Type()
)
vnHostGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnHostGroupName.setStatus("current")
_VnHostLastCheck_Type = Integer32
_VnHostLastCheck_Object = MibTableColumn
vnHostLastCheck = _VnHostLastCheck_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 1, 1, 9),
    _VnHostLastCheck_Type()
)
vnHostLastCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnHostLastCheck.setStatus("current")
_VnHostLastChange_Type = Integer32
_VnHostLastChange_Object = MibTableColumn
vnHostLastChange = _VnHostLastChange_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 1, 1, 10),
    _VnHostLastChange_Type()
)
vnHostLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnHostLastChange.setStatus("current")
_VnHostLastUp_Type = Integer32
_VnHostLastUp_Object = MibTableColumn
vnHostLastUp = _VnHostLastUp_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 1, 1, 11),
    _VnHostLastUp_Type()
)
vnHostLastUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnHostLastUp.setStatus("current")
_VnHostLastDown_Type = Integer32
_VnHostLastDown_Object = MibTableColumn
vnHostLastDown = _VnHostLastDown_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 1, 1, 12),
    _VnHostLastDown_Type()
)
vnHostLastDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnHostLastDown.setStatus("current")
_VnHostLastUnreachable_Type = Integer32
_VnHostLastUnreachable_Object = MibTableColumn
vnHostLastUnreachable = _VnHostLastUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 1, 1, 13),
    _VnHostLastUnreachable_Type()
)
vnHostLastUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnHostLastUnreachable.setStatus("current")
_VnHostOutput_Type = OctetString
_VnHostOutput_Object = MibTableColumn
vnHostOutput = _VnHostOutput_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 1, 1, 14),
    _VnHostOutput_Type()
)
vnHostOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnHostOutput.setStatus("current")
_VnHostPerfData_Type = OctetString
_VnHostPerfData_Object = MibTableColumn
vnHostPerfData = _VnHostPerfData_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 1, 1, 15),
    _VnHostPerfData_Type()
)
vnHostPerfData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnHostPerfData.setStatus("current")
_VnomicHostNotifyTable_Object = MibTable
vnomicHostNotifyTable = _VnomicHostNotifyTable_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 2)
)
if mibBuilder.loadTexts:
    vnomicHostNotifyTable.setStatus("current")
_VnomicHostNotifyEntry_Object = MibTableRow
vnomicHostNotifyEntry = _VnomicHostNotifyEntry_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 2, 1)
)
vnomicHostNotifyEntry.setIndexNames(
    (0, "VNOMIC-NOTIFY-MIB", "vnHostEventIndex"),
)
if mibBuilder.loadTexts:
    vnomicHostNotifyEntry.setStatus("current")
_VnHostNotifyType_Type = NotifyType
_VnHostNotifyType_Object = MibTableColumn
vnHostNotifyType = _VnHostNotifyType_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 2, 1, 1),
    _VnHostNotifyType_Type()
)
vnHostNotifyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnHostNotifyType.setStatus("current")
_VnHostNotifyNum_Type = Gauge32
_VnHostNotifyNum_Object = MibTableColumn
vnHostNotifyNum = _VnHostNotifyNum_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 2, 1, 2),
    _VnHostNotifyNum_Type()
)
vnHostNotifyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnHostNotifyNum.setStatus("current")
_VnHostAckAuthor_Type = OctetString
_VnHostAckAuthor_Object = MibTableColumn
vnHostAckAuthor = _VnHostAckAuthor_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 2, 1, 3),
    _VnHostAckAuthor_Type()
)
vnHostAckAuthor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnHostAckAuthor.setStatus("current")
_VnHostAckComment_Type = OctetString
_VnHostAckComment_Object = MibTableColumn
vnHostAckComment = _VnHostAckComment_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 2, 1, 4),
    _VnHostAckComment_Type()
)
vnHostAckComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnHostAckComment.setStatus("current")
_VnomicSvcEventTable_Object = MibTable
vnomicSvcEventTable = _VnomicSvcEventTable_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 3)
)
if mibBuilder.loadTexts:
    vnomicSvcEventTable.setStatus("current")
_VnomicSvcEventEntry_Object = MibTableRow
vnomicSvcEventEntry = _VnomicSvcEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 3, 1)
)
vnomicSvcEventEntry.setIndexNames(
    (0, "VNOMIC-NOTIFY-MIB", "vnServiceEventIndex"),
)
if mibBuilder.loadTexts:
    vnomicSvcEventEntry.setStatus("current")


class _VnServiceEventIndex_Type(Integer32):
    """Custom type vnServiceEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VnServiceEventIndex_Type.__name__ = "Integer32"
_VnServiceEventIndex_Object = MibTableColumn
vnServiceEventIndex = _VnServiceEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 3, 1, 1),
    _VnServiceEventIndex_Type()
)
vnServiceEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vnServiceEventIndex.setStatus("current")
_VnServiceHostname_Type = OctetString
_VnServiceHostname_Object = MibTableColumn
vnServiceHostname = _VnServiceHostname_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 3, 1, 2),
    _VnServiceHostname_Type()
)
vnServiceHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnServiceHostname.setStatus("current")
_VnServiceHostAlias_Type = OctetString
_VnServiceHostAlias_Object = MibTableColumn
vnServiceHostAlias = _VnServiceHostAlias_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 3, 1, 3),
    _VnServiceHostAlias_Type()
)
vnServiceHostAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnServiceHostAlias.setStatus("current")
_VnServiceHostStateID_Type = HostStateID
_VnServiceHostStateID_Object = MibTableColumn
vnServiceHostStateID = _VnServiceHostStateID_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 3, 1, 4),
    _VnServiceHostStateID_Type()
)
vnServiceHostStateID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnServiceHostStateID.setStatus("current")
_VnServiceHostStateType_Type = HostStateType
_VnServiceHostStateType_Object = MibTableColumn
vnServiceHostStateType = _VnServiceHostStateType_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 3, 1, 5),
    _VnServiceHostStateType_Type()
)
vnServiceHostStateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnServiceHostStateType.setStatus("current")
_VnServiceDesc_Type = OctetString
_VnServiceDesc_Object = MibTableColumn
vnServiceDesc = _VnServiceDesc_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 3, 1, 6),
    _VnServiceDesc_Type()
)
vnServiceDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnServiceDesc.setStatus("current")
_VnServiceStateID_Type = ServiceStateID
_VnServiceStateID_Object = MibTableColumn
vnServiceStateID = _VnServiceStateID_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 3, 1, 7),
    _VnServiceStateID_Type()
)
vnServiceStateID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnServiceStateID.setStatus("current")
_VnServiceAttempt_Type = Integer32
_VnServiceAttempt_Object = MibTableColumn
vnServiceAttempt = _VnServiceAttempt_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 3, 1, 8),
    _VnServiceAttempt_Type()
)
vnServiceAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnServiceAttempt.setStatus("current")
_VnServiceDurationSec_Type = Integer32
_VnServiceDurationSec_Object = MibTableColumn
vnServiceDurationSec = _VnServiceDurationSec_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 3, 1, 9),
    _VnServiceDurationSec_Type()
)
vnServiceDurationSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnServiceDurationSec.setStatus("current")
_VnServiceGroupName_Type = OctetString
_VnServiceGroupName_Object = MibTableColumn
vnServiceGroupName = _VnServiceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 3, 1, 10),
    _VnServiceGroupName_Type()
)
vnServiceGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnServiceGroupName.setStatus("current")
_VnServiceLastCheck_Type = Integer32
_VnServiceLastCheck_Object = MibTableColumn
vnServiceLastCheck = _VnServiceLastCheck_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 3, 1, 11),
    _VnServiceLastCheck_Type()
)
vnServiceLastCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnServiceLastCheck.setStatus("current")
_VnServiceLastChange_Type = Integer32
_VnServiceLastChange_Object = MibTableColumn
vnServiceLastChange = _VnServiceLastChange_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 3, 1, 12),
    _VnServiceLastChange_Type()
)
vnServiceLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnServiceLastChange.setStatus("current")
_VnServiceLastOK_Type = Integer32
_VnServiceLastOK_Object = MibTableColumn
vnServiceLastOK = _VnServiceLastOK_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 3, 1, 13),
    _VnServiceLastOK_Type()
)
vnServiceLastOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnServiceLastOK.setStatus("current")
_VnServiceLastWarn_Type = Integer32
_VnServiceLastWarn_Object = MibTableColumn
vnServiceLastWarn = _VnServiceLastWarn_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 3, 1, 14),
    _VnServiceLastWarn_Type()
)
vnServiceLastWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnServiceLastWarn.setStatus("current")
_VnServiceLastCrit_Type = Integer32
_VnServiceLastCrit_Object = MibTableColumn
vnServiceLastCrit = _VnServiceLastCrit_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 3, 1, 15),
    _VnServiceLastCrit_Type()
)
vnServiceLastCrit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnServiceLastCrit.setStatus("current")
_VnServiceLastUnkn_Type = Integer32
_VnServiceLastUnkn_Object = MibTableColumn
vnServiceLastUnkn = _VnServiceLastUnkn_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 3, 1, 16),
    _VnServiceLastUnkn_Type()
)
vnServiceLastUnkn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnServiceLastUnkn.setStatus("current")
_VnServiceOutput_Type = OctetString
_VnServiceOutput_Object = MibTableColumn
vnServiceOutput = _VnServiceOutput_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 3, 1, 17),
    _VnServiceOutput_Type()
)
vnServiceOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnServiceOutput.setStatus("current")
_VnServicePerfData_Type = OctetString
_VnServicePerfData_Object = MibTableColumn
vnServicePerfData = _VnServicePerfData_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 3, 1, 18),
    _VnServicePerfData_Type()
)
vnServicePerfData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnServicePerfData.setStatus("current")
_VnomicSvcNotifyTable_Object = MibTable
vnomicSvcNotifyTable = _VnomicSvcNotifyTable_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 4)
)
if mibBuilder.loadTexts:
    vnomicSvcNotifyTable.setStatus("current")
_VnomicSvcNotifyEntry_Object = MibTableRow
vnomicSvcNotifyEntry = _VnomicSvcNotifyEntry_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 4, 1)
)
vnomicSvcNotifyEntry.setIndexNames(
    (0, "VNOMIC-NOTIFY-MIB", "vnServiceEventIndex"),
)
if mibBuilder.loadTexts:
    vnomicSvcNotifyEntry.setStatus("current")
_VnServiceNotifyType_Type = NotifyType
_VnServiceNotifyType_Object = MibTableColumn
vnServiceNotifyType = _VnServiceNotifyType_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 4, 1, 1),
    _VnServiceNotifyType_Type()
)
vnServiceNotifyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnServiceNotifyType.setStatus("current")
_VnServiceNotifyNum_Type = Gauge32
_VnServiceNotifyNum_Object = MibTableColumn
vnServiceNotifyNum = _VnServiceNotifyNum_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 4, 1, 2),
    _VnServiceNotifyNum_Type()
)
vnServiceNotifyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnServiceNotifyNum.setStatus("current")
_VnServiceAckAuthor_Type = OctetString
_VnServiceAckAuthor_Object = MibTableColumn
vnServiceAckAuthor = _VnServiceAckAuthor_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 4, 1, 3),
    _VnServiceAckAuthor_Type()
)
vnServiceAckAuthor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnServiceAckAuthor.setStatus("current")
_VnServiceAckComment_Type = OctetString
_VnServiceAckComment_Object = MibTableColumn
vnServiceAckComment = _VnServiceAckComment_Object(
    (1, 3, 6, 1, 4, 1, 49671, 1, 4, 1, 4),
    _VnServiceAckComment_Type()
)
vnServiceAckComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnServiceAckComment.setStatus("current")

# Managed Objects groups


# Notification objects

vnHostEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 49671, 1, 5)
)
vnHostEvent.setObjects(
      *(("VNOMIC-NOTIFY-MIB", "vnHostname"),
        ("VNOMIC-NOTIFY-MIB", "vnHostStateID"),
        ("VNOMIC-NOTIFY-MIB", "vnHostStateType"),
        ("VNOMIC-NOTIFY-MIB", "vnHostAttempt"),
        ("VNOMIC-NOTIFY-MIB", "vnHostDurationSec"),
        ("VNOMIC-NOTIFY-MIB", "vnHostGroupName"),
        ("VNOMIC-NOTIFY-MIB", "vnHostLastCheck"),
        ("VNOMIC-NOTIFY-MIB", "vnHostLastChange"),
        ("VNOMIC-NOTIFY-MIB", "vnHostOutput"))
)
if mibBuilder.loadTexts:
    vnHostEvent.setStatus(
        "current"
    )

vnHostNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 49671, 1, 6)
)
vnHostNotify.setObjects(
      *(("VNOMIC-NOTIFY-MIB", "vnHostNotifyType"),
        ("VNOMIC-NOTIFY-MIB", "vnHostNotifyNum"),
        ("VNOMIC-NOTIFY-MIB", "vnHostAckAuthor"),
        ("VNOMIC-NOTIFY-MIB", "vnHostAckComment"),
        ("VNOMIC-NOTIFY-MIB", "vnHostname"),
        ("VNOMIC-NOTIFY-MIB", "vnHostStateID"),
        ("VNOMIC-NOTIFY-MIB", "vnHostStateType"),
        ("VNOMIC-NOTIFY-MIB", "vnHostAttempt"),
        ("VNOMIC-NOTIFY-MIB", "vnHostDurationSec"),
        ("VNOMIC-NOTIFY-MIB", "vnHostGroupName"),
        ("VNOMIC-NOTIFY-MIB", "vnHostLastCheck"),
        ("VNOMIC-NOTIFY-MIB", "vnHostLastChange"),
        ("VNOMIC-NOTIFY-MIB", "vnHostOutput"))
)
if mibBuilder.loadTexts:
    vnHostNotify.setStatus(
        "current"
    )

vnServiceEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 49671, 1, 7)
)
vnServiceEvent.setObjects(
      *(("VNOMIC-NOTIFY-MIB", "vnHostname"),
        ("VNOMIC-NOTIFY-MIB", "vnHostStateID"),
        ("VNOMIC-NOTIFY-MIB", "vnServiceDesc"),
        ("VNOMIC-NOTIFY-MIB", "vnServiceStateID"),
        ("VNOMIC-NOTIFY-MIB", "vnServiceAttempt"),
        ("VNOMIC-NOTIFY-MIB", "vnServiceDurationSec"),
        ("VNOMIC-NOTIFY-MIB", "vnServiceGroupName"),
        ("VNOMIC-NOTIFY-MIB", "vnServiceLastCheck"),
        ("VNOMIC-NOTIFY-MIB", "vnServiceLastChange"),
        ("VNOMIC-NOTIFY-MIB", "vnServiceOutput"))
)
if mibBuilder.loadTexts:
    vnServiceEvent.setStatus(
        "current"
    )

vnServiceNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 49671, 1, 8)
)
vnServiceNotify.setObjects(
      *(("VNOMIC-NOTIFY-MIB", "vnServiceNotifyType"),
        ("VNOMIC-NOTIFY-MIB", "vnServiceNotifyNum"),
        ("VNOMIC-NOTIFY-MIB", "vnServiceAckAuthor"),
        ("VNOMIC-NOTIFY-MIB", "vnServiceAckComment"),
        ("VNOMIC-NOTIFY-MIB", "vnHostname"),
        ("VNOMIC-NOTIFY-MIB", "vnHostStateID"),
        ("VNOMIC-NOTIFY-MIB", "vnServiceDesc"),
        ("VNOMIC-NOTIFY-MIB", "vnServiceStateID"),
        ("VNOMIC-NOTIFY-MIB", "vnServiceAttempt"),
        ("VNOMIC-NOTIFY-MIB", "vnServiceDurationSec"),
        ("VNOMIC-NOTIFY-MIB", "vnServiceGroupName"),
        ("VNOMIC-NOTIFY-MIB", "vnServiceLastCheck"),
        ("VNOMIC-NOTIFY-MIB", "vnServiceLastChange"),
        ("VNOMIC-NOTIFY-MIB", "vnServiceOutput"))
)
if mibBuilder.loadTexts:
    vnServiceNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VNOMIC-NOTIFY-MIB",
    **{"vnomicNotify": vnomicNotify,
       "vnomicHostEventTable": vnomicHostEventTable,
       "vnomicHostEventEntry": vnomicHostEventEntry,
       "vnHostEventIndex": vnHostEventIndex,
       "vnHostname": vnHostname,
       "vnHostAlias": vnHostAlias,
       "vnHostStateID": vnHostStateID,
       "vnHostStateType": vnHostStateType,
       "vnHostAttempt": vnHostAttempt,
       "vnHostDurationSec": vnHostDurationSec,
       "vnHostGroupName": vnHostGroupName,
       "vnHostLastCheck": vnHostLastCheck,
       "vnHostLastChange": vnHostLastChange,
       "vnHostLastUp": vnHostLastUp,
       "vnHostLastDown": vnHostLastDown,
       "vnHostLastUnreachable": vnHostLastUnreachable,
       "vnHostOutput": vnHostOutput,
       "vnHostPerfData": vnHostPerfData,
       "vnomicHostNotifyTable": vnomicHostNotifyTable,
       "vnomicHostNotifyEntry": vnomicHostNotifyEntry,
       "vnHostNotifyType": vnHostNotifyType,
       "vnHostNotifyNum": vnHostNotifyNum,
       "vnHostAckAuthor": vnHostAckAuthor,
       "vnHostAckComment": vnHostAckComment,
       "vnomicSvcEventTable": vnomicSvcEventTable,
       "vnomicSvcEventEntry": vnomicSvcEventEntry,
       "vnServiceEventIndex": vnServiceEventIndex,
       "vnServiceHostname": vnServiceHostname,
       "vnServiceHostAlias": vnServiceHostAlias,
       "vnServiceHostStateID": vnServiceHostStateID,
       "vnServiceHostStateType": vnServiceHostStateType,
       "vnServiceDesc": vnServiceDesc,
       "vnServiceStateID": vnServiceStateID,
       "vnServiceAttempt": vnServiceAttempt,
       "vnServiceDurationSec": vnServiceDurationSec,
       "vnServiceGroupName": vnServiceGroupName,
       "vnServiceLastCheck": vnServiceLastCheck,
       "vnServiceLastChange": vnServiceLastChange,
       "vnServiceLastOK": vnServiceLastOK,
       "vnServiceLastWarn": vnServiceLastWarn,
       "vnServiceLastCrit": vnServiceLastCrit,
       "vnServiceLastUnkn": vnServiceLastUnkn,
       "vnServiceOutput": vnServiceOutput,
       "vnServicePerfData": vnServicePerfData,
       "vnomicSvcNotifyTable": vnomicSvcNotifyTable,
       "vnomicSvcNotifyEntry": vnomicSvcNotifyEntry,
       "vnServiceNotifyType": vnServiceNotifyType,
       "vnServiceNotifyNum": vnServiceNotifyNum,
       "vnServiceAckAuthor": vnServiceAckAuthor,
       "vnServiceAckComment": vnServiceAckComment,
       "vnHostEvent": vnHostEvent,
       "vnHostNotify": vnHostNotify,
       "vnServiceEvent": vnServiceEvent,
       "vnServiceNotify": vnServiceNotify}
)
