# SNMP MIB module (MPEGTSMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/viathinksoft_37476/MPEGTSMON-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:06:51 2025
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

mpegtsMon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Summary_ObjectIdentity = ObjectIdentity
summary = _Summary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 1)
)
_Cumulative_ObjectIdentity = ObjectIdentity
cumulative = _Cumulative_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 1, 1)
)
_RecvBytes_Type = Counter32
_RecvBytes_Object = MibScalar
recvBytes = _RecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 1, 1, 1),
    _RecvBytes_Type()
)
recvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recvBytes.setStatus("current")
_ContinuityErrors_Type = Counter32
_ContinuityErrors_Object = MibScalar
continuityErrors = _ContinuityErrors_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 1, 1, 2),
    _ContinuityErrors_Type()
)
continuityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    continuityErrors.setStatus("current")
_Level_ObjectIdentity = ObjectIdentity
level = _Level_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 1, 2)
)
_StreamsTotal_Type = Gauge32
_StreamsTotal_Object = MibScalar
streamsTotal = _StreamsTotal_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 1, 2, 1),
    _StreamsTotal_Type()
)
streamsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsTotal.setStatus("current")
_StreamsBad_Type = Gauge32
_StreamsBad_Object = MibScalar
streamsBad = _StreamsBad_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 1, 2, 2),
    _StreamsBad_Type()
)
streamsBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsBad.setStatus("current")
_StreamsScrambled_Type = Gauge32
_StreamsScrambled_Object = MibScalar
streamsScrambled = _StreamsScrambled_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 1, 2, 3),
    _StreamsScrambled_Type()
)
streamsScrambled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsScrambled.setStatus("current")
_StreamsTEI_Type = Gauge32
_StreamsTEI_Object = MibScalar
streamsTEI = _StreamsTEI_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 1, 2, 4),
    _StreamsTEI_Type()
)
streamsTEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsTEI.setStatus("current")
_Other_ObjectIdentity = ObjectIdentity
other = _Other_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 2)
)
_LastChangedStreamAddr_Type = OctetString
_LastChangedStreamAddr_Object = MibScalar
lastChangedStreamAddr = _LastChangedStreamAddr_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 2, 1),
    _LastChangedStreamAddr_Type()
)
lastChangedStreamAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastChangedStreamAddr.setStatus("current")
_Streams_ObjectIdentity = ObjectIdentity
streams = _Streams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 3)
)
_StreamsTable_Object = MibTable
streamsTable = _StreamsTable_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 3, 1)
)
if mibBuilder.loadTexts:
    streamsTable.setStatus("current")
_StreamsEntry_Object = MibTableRow
streamsEntry = _StreamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 3, 1, 1)
)
streamsEntry.setIndexNames(
    (0, "MPEGTSMON-MIB", "sIP"),
)
if mibBuilder.loadTexts:
    streamsEntry.setStatus("current")
_SIP_Type = IpAddress
_SIP_Object = MibTableColumn
sIP = _SIP_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 3, 1, 1, 1),
    _SIP_Type()
)
sIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sIP.setStatus("current")
_SRecvBytes_Type = Counter32
_SRecvBytes_Object = MibTableColumn
sRecvBytes = _SRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 3, 1, 1, 2),
    _SRecvBytes_Type()
)
sRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRecvBytes.setStatus("current")
_SContinuityErrors_Type = Counter32
_SContinuityErrors_Object = MibTableColumn
sContinuityErrors = _SContinuityErrors_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 3, 1, 1, 3),
    _SContinuityErrors_Type()
)
sContinuityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sContinuityErrors.setStatus("current")


class _SStatus_Type(Integer32):
    """Custom type sStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("bad", 2))
    )


_SStatus_Type.__name__ = "Integer32"
_SStatus_Object = MibTableColumn
sStatus = _SStatus_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 3, 1, 1, 4),
    _SStatus_Type()
)
sStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sStatus.setStatus("current")


class _SStatusDetail_Type(Bits):
    """Custom type sStatusDetail based on Bits"""
    namedValues = NamedValues(
        *(("noSync", 0),
          ("noIncoming", 1),
          ("noAV", 2),
          ("scrambled", 3),
          ("tei", 4))
    )

_SStatusDetail_Type.__name__ = "Bits"
_SStatusDetail_Object = MibTableColumn
sStatusDetail = _SStatusDetail_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 3, 1, 1, 5),
    _SStatusDetail_Type()
)
sStatusDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sStatusDetail.setStatus("current")
_Probes_ObjectIdentity = ObjectIdentity
probes = _Probes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 4)
)
_ProbesTable_Object = MibTable
probesTable = _ProbesTable_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 4, 1)
)
if mibBuilder.loadTexts:
    probesTable.setStatus("current")
_ProbesEntry_Object = MibTableRow
probesEntry = _ProbesEntry_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 4, 1, 1)
)
probesEntry.setIndexNames(
    (0, "MPEGTSMON-MIB", "pIP"),
)
if mibBuilder.loadTexts:
    probesEntry.setStatus("current")
_PIP_Type = IpAddress
_PIP_Object = MibTableColumn
pIP = _PIP_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 4, 1, 1, 1),
    _PIP_Type()
)
pIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pIP.setStatus("current")
_PDupsHtP_Type = Counter32
_PDupsHtP_Object = MibTableColumn
pDupsHtP = _PDupsHtP_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 4, 1, 1, 2),
    _PDupsHtP_Type()
)
pDupsHtP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDupsHtP.setStatus("current")
_PDupsPtH_Type = Counter32
_PDupsPtH_Object = MibTableColumn
pDupsPtH = _PDupsPtH_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 4, 1, 1, 3),
    _PDupsPtH_Type()
)
pDupsPtH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDupsPtH.setStatus("current")
_PHostPacketLost_Type = Counter32
_PHostPacketLost_Object = MibTableColumn
pHostPacketLost = _PHostPacketLost_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 4, 1, 1, 4),
    _PHostPacketLost_Type()
)
pHostPacketLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pHostPacketLost.setStatus("current")
_PProbePacketLost_Type = Counter32
_PProbePacketLost_Object = MibTableColumn
pProbePacketLost = _PProbePacketLost_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 4, 1, 1, 5),
    _PProbePacketLost_Type()
)
pProbePacketLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pProbePacketLost.setStatus("current")


class _PStatus_Type(Integer32):
    """Custom type pStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_PStatus_Type.__name__ = "Integer32"
_PStatus_Object = MibTableColumn
pStatus = _PStatus_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 4, 1, 1, 6),
    _PStatus_Type()
)
pStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pStatus.setStatus("current")
_ProbesStreamsTable_Object = MibTable
probesStreamsTable = _ProbesStreamsTable_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 4, 2)
)
if mibBuilder.loadTexts:
    probesStreamsTable.setStatus("current")
_ProbesStreamsEntry_Object = MibTableRow
probesStreamsEntry = _ProbesStreamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 4, 2, 1)
)
probesStreamsEntry.setIndexNames(
    (0, "MPEGTSMON-MIB", "pIP"),
    (0, "MPEGTSMON-MIB", "sIP"),
)
if mibBuilder.loadTexts:
    probesStreamsEntry.setStatus("current")
_PsContinuityErrors_Type = Counter32
_PsContinuityErrors_Object = MibTableColumn
psContinuityErrors = _PsContinuityErrors_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 4, 2, 1, 1),
    _PsContinuityErrors_Type()
)
psContinuityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psContinuityErrors.setStatus("current")


class _PsStatus_Type(Integer32):
    """Custom type psStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_PsStatus_Type.__name__ = "Integer32"
_PsStatus_Object = MibTableColumn
psStatus = _PsStatus_Object(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 4, 2, 1, 2),
    _PsStatus_Type()
)
psStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psStatus.setStatus("current")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 99)
)
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 100)
)

# Managed Objects groups

summaryCumulativeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 100, 2)
)
summaryCumulativeGroup.setObjects(
      *(("MPEGTSMON-MIB", "recvBytes"),
        ("MPEGTSMON-MIB", "continuityErrors"))
)
if mibBuilder.loadTexts:
    summaryCumulativeGroup.setStatus("current")

summaryLevelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 100, 3)
)
summaryLevelGroup.setObjects(
      *(("MPEGTSMON-MIB", "streamsTotal"),
        ("MPEGTSMON-MIB", "streamsBad"),
        ("MPEGTSMON-MIB", "streamsScrambled"),
        ("MPEGTSMON-MIB", "streamsTEI"))
)
if mibBuilder.loadTexts:
    summaryLevelGroup.setStatus("current")

otherGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 100, 4)
)
otherGroup.setObjects(
    ("MPEGTSMON-MIB", "lastChangedStreamAddr")
)
if mibBuilder.loadTexts:
    otherGroup.setStatus("current")

streamsTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 100, 5)
)
streamsTableGroup.setObjects(
      *(("MPEGTSMON-MIB", "sIP"),
        ("MPEGTSMON-MIB", "sRecvBytes"),
        ("MPEGTSMON-MIB", "sContinuityErrors"),
        ("MPEGTSMON-MIB", "sStatus"),
        ("MPEGTSMON-MIB", "sStatusDetail"))
)
if mibBuilder.loadTexts:
    streamsTableGroup.setStatus("current")

probesTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 100, 6)
)
probesTableGroup.setObjects(
      *(("MPEGTSMON-MIB", "pIP"),
        ("MPEGTSMON-MIB", "pDupsHtP"),
        ("MPEGTSMON-MIB", "pDupsPtH"),
        ("MPEGTSMON-MIB", "pHostPacketLost"),
        ("MPEGTSMON-MIB", "pProbePacketLost"),
        ("MPEGTSMON-MIB", "pStatus"))
)
if mibBuilder.loadTexts:
    probesTableGroup.setStatus("current")

probesStreamsTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 100, 8)
)
probesStreamsTableGroup.setObjects(
      *(("MPEGTSMON-MIB", "psContinuityErrors"),
        ("MPEGTSMON-MIB", "psStatus"))
)
if mibBuilder.loadTexts:
    probesStreamsTableGroup.setStatus("current")


# Notification objects

streamDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 99, 1)
)
streamDown.setObjects(
    ("MPEGTSMON-MIB", "lastChangedStreamAddr")
)
if mibBuilder.loadTexts:
    streamDown.setStatus(
        "current"
    )

streamUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 99, 2)
)
streamUp.setObjects(
    ("MPEGTSMON-MIB", "lastChangedStreamAddr")
)
if mibBuilder.loadTexts:
    streamUp.setStatus(
        "current"
    )

probeDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 99, 3)
)
probeDown.setObjects(
    ("MPEGTSMON-MIB", "pIP")
)
if mibBuilder.loadTexts:
    probeDown.setStatus(
        "current"
    )

probeUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 99, 4)
)
probeUp.setObjects(
    ("MPEGTSMON-MIB", "pIP")
)
if mibBuilder.loadTexts:
    probeUp.setStatus(
        "current"
    )

streamAtProbeDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 99, 5)
)
streamAtProbeDown.setObjects(
      *(("MPEGTSMON-MIB", "pIP"),
        ("MPEGTSMON-MIB", "sIP"))
)
if mibBuilder.loadTexts:
    streamAtProbeDown.setStatus(
        "current"
    )

streamAtProbeUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 99, 6)
)
streamAtProbeUp.setObjects(
      *(("MPEGTSMON-MIB", "pIP"),
        ("MPEGTSMON-MIB", "sIP"))
)
if mibBuilder.loadTexts:
    streamAtProbeUp.setStatus(
        "current"
    )


# Notifications groups

streamNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 100, 1)
)
streamNotificationsGroup.setObjects(
      *(("MPEGTSMON-MIB", "streamDown"),
        ("MPEGTSMON-MIB", "streamUp"))
)
if mibBuilder.loadTexts:
    streamNotificationsGroup.setStatus(
        "current"
    )

probeNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 100, 7)
)
probeNotificationsGroup.setObjects(
      *(("MPEGTSMON-MIB", "probeDown"),
        ("MPEGTSMON-MIB", "probeUp"))
)
if mibBuilder.loadTexts:
    probeNotificationsGroup.setStatus(
        "current"
    )

probeStreamNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 37476, 9000, 24, 1, 100, 9)
)
probeStreamNotificationsGroup.setObjects(
      *(("MPEGTSMON-MIB", "streamAtProbeDown"),
        ("MPEGTSMON-MIB", "streamAtProbeUp"))
)
if mibBuilder.loadTexts:
    probeStreamNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPEGTSMON-MIB",
    **{"mpegtsMon": mpegtsMon,
       "summary": summary,
       "cumulative": cumulative,
       "recvBytes": recvBytes,
       "continuityErrors": continuityErrors,
       "level": level,
       "streamsTotal": streamsTotal,
       "streamsBad": streamsBad,
       "streamsScrambled": streamsScrambled,
       "streamsTEI": streamsTEI,
       "other": other,
       "lastChangedStreamAddr": lastChangedStreamAddr,
       "streams": streams,
       "streamsTable": streamsTable,
       "streamsEntry": streamsEntry,
       "sIP": sIP,
       "sRecvBytes": sRecvBytes,
       "sContinuityErrors": sContinuityErrors,
       "sStatus": sStatus,
       "sStatusDetail": sStatusDetail,
       "probes": probes,
       "probesTable": probesTable,
       "probesEntry": probesEntry,
       "pIP": pIP,
       "pDupsHtP": pDupsHtP,
       "pDupsPtH": pDupsPtH,
       "pHostPacketLost": pHostPacketLost,
       "pProbePacketLost": pProbePacketLost,
       "pStatus": pStatus,
       "probesStreamsTable": probesStreamsTable,
       "probesStreamsEntry": probesStreamsEntry,
       "psContinuityErrors": psContinuityErrors,
       "psStatus": psStatus,
       "traps": traps,
       "streamDown": streamDown,
       "streamUp": streamUp,
       "probeDown": probeDown,
       "probeUp": probeUp,
       "streamAtProbeDown": streamAtProbeDown,
       "streamAtProbeUp": streamAtProbeUp,
       "groups": groups,
       "streamNotificationsGroup": streamNotificationsGroup,
       "summaryCumulativeGroup": summaryCumulativeGroup,
       "summaryLevelGroup": summaryLevelGroup,
       "otherGroup": otherGroup,
       "streamsTableGroup": streamsTableGroup,
       "probesTableGroup": probesTableGroup,
       "probeNotificationsGroup": probeNotificationsGroup,
       "probesStreamsTableGroup": probesStreamsTableGroup,
       "probeStreamNotificationsGroup": probeStreamNotificationsGroup}
)
