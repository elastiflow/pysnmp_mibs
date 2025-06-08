# SNMP MIB module (VIDEO-QAM-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/VIDEO-QAM-DEVICE-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:36:32 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(heRF,) = mibBuilder.importSymbols(
    "SCTE-HMS-HEADENDIDENT-MIB",
    "heRF")

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

videoQamDeviceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3)
)
if mibBuilder.loadTexts:
    videoQamDeviceMIB.setRevisions(
        ("2005-04-19 14:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pid(TextualConvention, Unsigned32):
    status = "current"


class ProgramNumber(TextualConvention, Unsigned32):
    status = "current"


class VideoUdpPort(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_VideoQamDeviceMIBNotifs_ObjectIdentity = ObjectIdentity
videoQamDeviceMIBNotifs = _VideoQamDeviceMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 0)
)
_VideoQamDeviceMIBObjects_ObjectIdentity = ObjectIdentity
videoQamDeviceMIBObjects = _VideoQamDeviceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1)
)
_VqdBaseObjects_ObjectIdentity = ObjectIdentity
vqdBaseObjects = _VqdBaseObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 1)
)
_VqdInputObjects_ObjectIdentity = ObjectIdentity
vqdInputObjects = _VqdInputObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2)
)


class _VqdSignalLossTimeout_Type(Unsigned32):
    """Custom type vqdSignalLossTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 10000),
    )


_VqdSignalLossTimeout_Type.__name__ = "Unsigned32"
_VqdSignalLossTimeout_Object = MibScalar
vqdSignalLossTimeout = _VqdSignalLossTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 1),
    _VqdSignalLossTimeout_Type()
)
vqdSignalLossTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vqdSignalLossTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vqdSignalLossTimeout.setUnits("milliseconds")
_VqdVideoSessionTable_Object = MibTable
vqdVideoSessionTable = _VqdVideoSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    vqdVideoSessionTable.setStatus("current")
_VqdVideoSessionEntry_Object = MibTableRow
vqdVideoSessionEntry = _VqdVideoSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 2, 1)
)
vqdVideoSessionEntry.setIndexNames(
    (0, "VIDEO-QAM-DEVICE-MIB", "vqdVideoSessDestAddressType"),
    (0, "VIDEO-QAM-DEVICE-MIB", "vqdVideoSessDestAddress"),
    (0, "VIDEO-QAM-DEVICE-MIB", "vqdVideoSessIndex"),
)
if mibBuilder.loadTexts:
    vqdVideoSessionEntry.setStatus("current")
_VqdVideoSessDestAddressType_Type = InetAddressType
_VqdVideoSessDestAddressType_Object = MibTableColumn
vqdVideoSessDestAddressType = _VqdVideoSessDestAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 2, 1, 1),
    _VqdVideoSessDestAddressType_Type()
)
vqdVideoSessDestAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vqdVideoSessDestAddressType.setStatus("current")
_VqdVideoSessDestAddress_Type = InetAddress
_VqdVideoSessDestAddress_Object = MibTableColumn
vqdVideoSessDestAddress = _VqdVideoSessDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 2, 1, 2),
    _VqdVideoSessDestAddress_Type()
)
vqdVideoSessDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vqdVideoSessDestAddress.setStatus("current")
_VqdVideoSessIndex_Type = VideoUdpPort
_VqdVideoSessIndex_Object = MibTableColumn
vqdVideoSessIndex = _VqdVideoSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 2, 1, 3),
    _VqdVideoSessIndex_Type()
)
vqdVideoSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vqdVideoSessIndex.setStatus("current")
_VqdVideoSessBandwidth_Type = Unsigned32
_VqdVideoSessBandwidth_Object = MibTableColumn
vqdVideoSessBandwidth = _VqdVideoSessBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 2, 1, 4),
    _VqdVideoSessBandwidth_Type()
)
vqdVideoSessBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdVideoSessBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vqdVideoSessBandwidth.setUnits("bps")
_VqdVideoSessStartTime_Type = DateAndTime
_VqdVideoSessStartTime_Object = MibTableColumn
vqdVideoSessStartTime = _VqdVideoSessStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 2, 1, 5),
    _VqdVideoSessStartTime_Type()
)
vqdVideoSessStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdVideoSessStartTime.setStatus("current")
_VqdVideoSessMaxJitter_Type = Unsigned32
_VqdVideoSessMaxJitter_Object = MibTableColumn
vqdVideoSessMaxJitter = _VqdVideoSessMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 2, 1, 6),
    _VqdVideoSessMaxJitter_Type()
)
vqdVideoSessMaxJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vqdVideoSessMaxJitter.setStatus("current")
if mibBuilder.loadTexts:
    vqdVideoSessMaxJitter.setUnits("milliseconds")


class _VqdVideoSessStatus_Type(Integer32):
    """Custom type vqdVideoSessStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("psiFail", 3),
          ("idle", 4))
    )


_VqdVideoSessStatus_Type.__name__ = "Integer32"
_VqdVideoSessStatus_Object = MibTableColumn
vqdVideoSessStatus = _VqdVideoSessStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 2, 1, 7),
    _VqdVideoSessStatus_Type()
)
vqdVideoSessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdVideoSessStatus.setStatus("current")
_VqdVideoSessQamIndex_Type = InterfaceIndex
_VqdVideoSessQamIndex_Object = MibTableColumn
vqdVideoSessQamIndex = _VqdVideoSessQamIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 2, 1, 8),
    _VqdVideoSessQamIndex_Type()
)
vqdVideoSessQamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdVideoSessQamIndex.setStatus("current")
_VqdNGODVideoSessionTable_Object = MibTable
vqdNGODVideoSessionTable = _VqdNGODVideoSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    vqdNGODVideoSessionTable.setStatus("current")
_VqdSessionStatsTable_Object = MibTable
vqdSessionStatsTable = _VqdSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    vqdSessionStatsTable.setStatus("current")
_VqdNGODVideoSessionEntry_Object = MibTableRow
vqdNGODVideoSessionEntry = _VqdNGODVideoSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 3, 1)
)
vqdNGODVideoSessionEntry.setIndexNames(
    (0, "VIDEO-QAM-DEVICE-MIB", "vqdVideoSessDestAddressType"),
    (0, "VIDEO-QAM-DEVICE-MIB", "vqdVideoSessDestAddress"),
    (0, "VIDEO-QAM-DEVICE-MIB", "vqdVideoSessIndex"),
)
if mibBuilder.loadTexts:
    vqdNGODVideoSessionEntry.setStatus("current")
_VqdSessionStatsEntry_Object = MibTableRow
vqdSessionStatsEntry = _VqdSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 3, 1)
)
vqdSessionStatsEntry.setIndexNames(
    (0, "VIDEO-QAM-DEVICE-MIB", "vqdVideoSessDestAddressType"),
    (0, "VIDEO-QAM-DEVICE-MIB", "vqdVideoSessDestAddress"),
    (0, "VIDEO-QAM-DEVICE-MIB", "vqdVideoSessIndex"),
)
if mibBuilder.loadTexts:
    vqdSessionStatsEntry.setStatus("current")
_VqdNGODVideoSessOnDemandSessionId_Type = SnmpAdminString
_VqdNGODVideoSessOnDemandSessionId_Object = MibTableColumn
vqdNGODVideoSessOnDemandSessionId = _VqdNGODVideoSessOnDemandSessionId_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 3, 1, 1),
    _VqdNGODVideoSessOnDemandSessionId_Type()
)
vqdNGODVideoSessOnDemandSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdNGODVideoSessOnDemandSessionId.setStatus("current")
_VqdSessStatsCurrentBitrate_Type = Unsigned32
_VqdSessStatsCurrentBitrate_Object = MibTableColumn
vqdSessStatsCurrentBitrate = _VqdSessStatsCurrentBitrate_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 3, 1, 1),
    _VqdSessStatsCurrentBitrate_Type()
)
vqdSessStatsCurrentBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdSessStatsCurrentBitrate.setStatus("current")
if mibBuilder.loadTexts:
    vqdSessStatsCurrentBitrate.setUnits("bps")
_VqdSessStatsAvgBitrate_Type = Unsigned32
_VqdSessStatsAvgBitrate_Object = MibTableColumn
vqdSessStatsAvgBitrate = _VqdSessStatsAvgBitrate_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 3, 1, 2),
    _VqdSessStatsAvgBitrate_Type()
)
vqdSessStatsAvgBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdSessStatsAvgBitrate.setStatus("current")
if mibBuilder.loadTexts:
    vqdSessStatsAvgBitrate.setUnits("bps")
_VqdSessStatsPeakJitter_Type = Unsigned32
_VqdSessStatsPeakJitter_Object = MibTableColumn
vqdSessStatsPeakJitter = _VqdSessStatsPeakJitter_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 3, 1, 3),
    _VqdSessStatsPeakJitter_Type()
)
vqdSessStatsPeakJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdSessStatsPeakJitter.setStatus("current")
if mibBuilder.loadTexts:
    vqdSessStatsPeakJitter.setUnits("microseconds")
_VqdSessStatsAvgJitter_Type = Unsigned32
_VqdSessStatsAvgJitter_Object = MibTableColumn
vqdSessStatsAvgJitter = _VqdSessStatsAvgJitter_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 3, 1, 4),
    _VqdSessStatsAvgJitter_Type()
)
vqdSessStatsAvgJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdSessStatsAvgJitter.setStatus("current")
if mibBuilder.loadTexts:
    vqdSessStatsAvgJitter.setUnits("microseconds")
_VqdSessionDetStatsTable_Object = MibTable
vqdSessionDetStatsTable = _VqdSessionDetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    vqdSessionDetStatsTable.setStatus("current")
_VqdSessionDetStatsEntry_Object = MibTableRow
vqdSessionDetStatsEntry = _VqdSessionDetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 4, 1)
)
vqdSessionDetStatsEntry.setIndexNames(
    (0, "VIDEO-QAM-DEVICE-MIB", "vqdVideoSessDestAddressType"),
    (0, "VIDEO-QAM-DEVICE-MIB", "vqdVideoSessDestAddress"),
    (0, "VIDEO-QAM-DEVICE-MIB", "vqdVideoSessIndex"),
)
if mibBuilder.loadTexts:
    vqdSessionDetStatsEntry.setStatus("current")
_VqdSessDetStatsSyncLosses_Type = Counter32
_VqdSessDetStatsSyncLosses_Object = MibTableColumn
vqdSessDetStatsSyncLosses = _VqdSessDetStatsSyncLosses_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 4, 1, 1),
    _VqdSessDetStatsSyncLosses_Type()
)
vqdSessDetStatsSyncLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdSessDetStatsSyncLosses.setStatus("current")
_VqdSessDetStatsPcrFrequencyDiff_Type = Integer32
_VqdSessDetStatsPcrFrequencyDiff_Object = MibTableColumn
vqdSessDetStatsPcrFrequencyDiff = _VqdSessDetStatsPcrFrequencyDiff_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 4, 1, 2),
    _VqdSessDetStatsPcrFrequencyDiff_Type()
)
vqdSessDetStatsPcrFrequencyDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdSessDetStatsPcrFrequencyDiff.setStatus("current")
if mibBuilder.loadTexts:
    vqdSessDetStatsPcrFrequencyDiff.setUnits("Hz")
_VqdSessDetStatsPcrPackets_Type = Counter32
_VqdSessDetStatsPcrPackets_Object = MibTableColumn
vqdSessDetStatsPcrPackets = _VqdSessDetStatsPcrPackets_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 4, 1, 3),
    _VqdSessDetStatsPcrPackets_Type()
)
vqdSessDetStatsPcrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdSessDetStatsPcrPackets.setStatus("current")
if mibBuilder.loadTexts:
    vqdSessDetStatsPcrPackets.setUnits("packets")
_VqdSessDetStatsNonPcrPackets_Type = Counter32
_VqdSessDetStatsNonPcrPackets_Object = MibTableColumn
vqdSessDetStatsNonPcrPackets = _VqdSessDetStatsNonPcrPackets_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 4, 1, 4),
    _VqdSessDetStatsNonPcrPackets_Type()
)
vqdSessDetStatsNonPcrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdSessDetStatsNonPcrPackets.setStatus("current")
if mibBuilder.loadTexts:
    vqdSessDetStatsNonPcrPackets.setUnits("packets")
_VqdSessDetStatsDroppedPackets_Type = Counter32
_VqdSessDetStatsDroppedPackets_Object = MibTableColumn
vqdSessDetStatsDroppedPackets = _VqdSessDetStatsDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 4, 1, 5),
    _VqdSessDetStatsDroppedPackets_Type()
)
vqdSessDetStatsDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdSessDetStatsDroppedPackets.setStatus("current")
if mibBuilder.loadTexts:
    vqdSessDetStatsDroppedPackets.setUnits("packets")
_VqdSessDetStatsDiscontinuityPcrs_Type = Counter32
_VqdSessDetStatsDiscontinuityPcrs_Object = MibTableColumn
vqdSessDetStatsDiscontinuityPcrs = _VqdSessDetStatsDiscontinuityPcrs_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 4, 1, 6),
    _VqdSessDetStatsDiscontinuityPcrs_Type()
)
vqdSessDetStatsDiscontinuityPcrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdSessDetStatsDiscontinuityPcrs.setStatus("current")
if mibBuilder.loadTexts:
    vqdSessDetStatsDiscontinuityPcrs.setUnits("packets")
_VqdSessDetStatsContinuityErrors_Type = Counter32
_VqdSessDetStatsContinuityErrors_Object = MibTableColumn
vqdSessDetStatsContinuityErrors = _VqdSessDetStatsContinuityErrors_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 4, 1, 7),
    _VqdSessDetStatsContinuityErrors_Type()
)
vqdSessDetStatsContinuityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdSessDetStatsContinuityErrors.setStatus("current")
_VqdSessDetStatsUnderflows_Type = Counter32
_VqdSessDetStatsUnderflows_Object = MibTableColumn
vqdSessDetStatsUnderflows = _VqdSessDetStatsUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 4, 1, 8),
    _VqdSessDetStatsUnderflows_Type()
)
vqdSessDetStatsUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdSessDetStatsUnderflows.setStatus("current")
if mibBuilder.loadTexts:
    vqdSessDetStatsUnderflows.setUnits("packets")
_VqdSessDetStatsOverflows_Type = Counter32
_VqdSessDetStatsOverflows_Object = MibTableColumn
vqdSessDetStatsOverflows = _VqdSessDetStatsOverflows_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 4, 1, 9),
    _VqdSessDetStatsOverflows_Type()
)
vqdSessDetStatsOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdSessDetStatsOverflows.setStatus("current")
if mibBuilder.loadTexts:
    vqdSessDetStatsOverflows.setUnits("packets")
_VqdSessDetStatsMaxPcrInterval_Type = Unsigned32
_VqdSessDetStatsMaxPcrInterval_Object = MibTableColumn
vqdSessDetStatsMaxPcrInterval = _VqdSessDetStatsMaxPcrInterval_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 4, 1, 10),
    _VqdSessDetStatsMaxPcrInterval_Type()
)
vqdSessDetStatsMaxPcrInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdSessDetStatsMaxPcrInterval.setStatus("current")
if mibBuilder.loadTexts:
    vqdSessDetStatsMaxPcrInterval.setUnits("microseconds")
_VqdSessDetStatsAvgPcrInterval_Type = Unsigned32
_VqdSessDetStatsAvgPcrInterval_Object = MibTableColumn
vqdSessDetStatsAvgPcrInterval = _VqdSessDetStatsAvgPcrInterval_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 4, 1, 11),
    _VqdSessDetStatsAvgPcrInterval_Type()
)
vqdSessDetStatsAvgPcrInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdSessDetStatsAvgPcrInterval.setStatus("current")
if mibBuilder.loadTexts:
    vqdSessDetStatsAvgPcrInterval.setUnits("microseconds")
_VqdInputPsiTable_Object = MibTable
vqdInputPsiTable = _VqdInputPsiTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 5)
)
if mibBuilder.loadTexts:
    vqdInputPsiTable.setStatus("current")
_VqdInputPsiEntry_Object = MibTableRow
vqdInputPsiEntry = _VqdInputPsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 5, 1)
)
vqdInputPsiEntry.setIndexNames(
    (0, "VIDEO-QAM-DEVICE-MIB", "vqdVideoSessDestAddressType"),
    (0, "VIDEO-QAM-DEVICE-MIB", "vqdVideoSessDestAddress"),
    (0, "VIDEO-QAM-DEVICE-MIB", "vqdVideoSessIndex"),
)
if mibBuilder.loadTexts:
    vqdInputPsiEntry.setStatus("current")
_VqdInputPsiTsid_Type = Unsigned32
_VqdInputPsiTsid_Object = MibTableColumn
vqdInputPsiTsid = _VqdInputPsiTsid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 5, 1, 1),
    _VqdInputPsiTsid_Type()
)
vqdInputPsiTsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdInputPsiTsid.setStatus("current")
_VqdInputPsiPatVersion_Type = Unsigned32
_VqdInputPsiPatVersion_Object = MibTableColumn
vqdInputPsiPatVersion = _VqdInputPsiPatVersion_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 5, 1, 2),
    _VqdInputPsiPatVersion_Type()
)
vqdInputPsiPatVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdInputPsiPatVersion.setStatus("current")
_VqdInputPsiCatVersion_Type = Unsigned32
_VqdInputPsiCatVersion_Object = MibTableColumn
vqdInputPsiCatVersion = _VqdInputPsiCatVersion_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 5, 1, 3),
    _VqdInputPsiCatVersion_Type()
)
vqdInputPsiCatVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdInputPsiCatVersion.setStatus("current")
_VqdInputPsiNitPid_Type = Pid
_VqdInputPsiNitPid_Object = MibTableColumn
vqdInputPsiNitPid = _VqdInputPsiNitPid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 5, 1, 4),
    _VqdInputPsiNitPid_Type()
)
vqdInputPsiNitPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdInputPsiNitPid.setStatus("current")
_VqdInputPsiNumPrograms_Type = Unsigned32
_VqdInputPsiNumPrograms_Object = MibTableColumn
vqdInputPsiNumPrograms = _VqdInputPsiNumPrograms_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 5, 1, 5),
    _VqdInputPsiNumPrograms_Type()
)
vqdInputPsiNumPrograms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdInputPsiNumPrograms.setStatus("current")
_VqdInputPsiNumEmms_Type = Unsigned32
_VqdInputPsiNumEmms_Object = MibTableColumn
vqdInputPsiNumEmms = _VqdInputPsiNumEmms_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 5, 1, 6),
    _VqdInputPsiNumEmms_Type()
)
vqdInputPsiNumEmms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdInputPsiNumEmms.setStatus("current")
_VqdInputPsiProgTable_Object = MibTable
vqdInputPsiProgTable = _VqdInputPsiProgTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 6)
)
if mibBuilder.loadTexts:
    vqdInputPsiProgTable.setStatus("current")
_VqdInputPsiProgEntry_Object = MibTableRow
vqdInputPsiProgEntry = _VqdInputPsiProgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 6, 1)
)
vqdInputPsiProgEntry.setIndexNames(
    (0, "VIDEO-QAM-DEVICE-MIB", "vqdVideoSessDestAddressType"),
    (0, "VIDEO-QAM-DEVICE-MIB", "vqdVideoSessDestAddress"),
    (0, "VIDEO-QAM-DEVICE-MIB", "vqdVideoSessIndex"),
    (0, "VIDEO-QAM-DEVICE-MIB", "vqdInputPsiProgIndex"),
)
if mibBuilder.loadTexts:
    vqdInputPsiProgEntry.setStatus("current")
_VqdInputPsiProgIndex_Type = ProgramNumber
_VqdInputPsiProgIndex_Object = MibTableColumn
vqdInputPsiProgIndex = _VqdInputPsiProgIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 6, 1, 1),
    _VqdInputPsiProgIndex_Type()
)
vqdInputPsiProgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vqdInputPsiProgIndex.setStatus("current")
_VqdInputPsiProgPmtVersion_Type = Unsigned32
_VqdInputPsiProgPmtVersion_Object = MibTableColumn
vqdInputPsiProgPmtVersion = _VqdInputPsiProgPmtVersion_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 6, 1, 2),
    _VqdInputPsiProgPmtVersion_Type()
)
vqdInputPsiProgPmtVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdInputPsiProgPmtVersion.setStatus("current")
_VqdInputPsiProgPmtPid_Type = Pid
_VqdInputPsiProgPmtPid_Object = MibTableColumn
vqdInputPsiProgPmtPid = _VqdInputPsiProgPmtPid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 6, 1, 3),
    _VqdInputPsiProgPmtPid_Type()
)
vqdInputPsiProgPmtPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdInputPsiProgPmtPid.setStatus("current")
_VqdInputPsiProgPcrPid_Type = Pid
_VqdInputPsiProgPcrPid_Object = MibTableColumn
vqdInputPsiProgPcrPid = _VqdInputPsiProgPcrPid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 6, 1, 4),
    _VqdInputPsiProgPcrPid_Type()
)
vqdInputPsiProgPcrPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdInputPsiProgPcrPid.setStatus("current")
_VqdInputPsiProgEcmPid_Type = Pid
_VqdInputPsiProgEcmPid_Object = MibTableColumn
vqdInputPsiProgEcmPid = _VqdInputPsiProgEcmPid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 6, 1, 5),
    _VqdInputPsiProgEcmPid_Type()
)
vqdInputPsiProgEcmPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdInputPsiProgEcmPid.setStatus("current")
_VqdInputPsiProgNumElems_Type = Unsigned32
_VqdInputPsiProgNumElems_Object = MibTableColumn
vqdInputPsiProgNumElems = _VqdInputPsiProgNumElems_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 6, 1, 6),
    _VqdInputPsiProgNumElems_Type()
)
vqdInputPsiProgNumElems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdInputPsiProgNumElems.setStatus("current")
_VqdInputPsiProgNumEcms_Type = Unsigned32
_VqdInputPsiProgNumEcms_Object = MibTableColumn
vqdInputPsiProgNumEcms = _VqdInputPsiProgNumEcms_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 6, 1, 7),
    _VqdInputPsiProgNumEcms_Type()
)
vqdInputPsiProgNumEcms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdInputPsiProgNumEcms.setStatus("current")
_VqdInputPsiProgCaDescr_Type = SnmpAdminString
_VqdInputPsiProgCaDescr_Object = MibTableColumn
vqdInputPsiProgCaDescr = _VqdInputPsiProgCaDescr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 6, 1, 8),
    _VqdInputPsiProgCaDescr_Type()
)
vqdInputPsiProgCaDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdInputPsiProgCaDescr.setStatus("current")
_VqdInputPsiProgElemStreamTable_Object = MibTable
vqdInputPsiProgElemStreamTable = _VqdInputPsiProgElemStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 7)
)
if mibBuilder.loadTexts:
    vqdInputPsiProgElemStreamTable.setStatus("current")
_VqdInputPsiProgElemStreamEntry_Object = MibTableRow
vqdInputPsiProgElemStreamEntry = _VqdInputPsiProgElemStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 7, 1)
)
vqdInputPsiProgElemStreamEntry.setIndexNames(
    (0, "VIDEO-QAM-DEVICE-MIB", "vqdVideoSessDestAddressType"),
    (0, "VIDEO-QAM-DEVICE-MIB", "vqdVideoSessDestAddress"),
    (0, "VIDEO-QAM-DEVICE-MIB", "vqdVideoSessIndex"),
    (0, "VIDEO-QAM-DEVICE-MIB", "vqdInputPsiProgElemStreamIndex"),
)
if mibBuilder.loadTexts:
    vqdInputPsiProgElemStreamEntry.setStatus("current")
_VqdInputPsiProgElemStreamIndex_Type = Pid
_VqdInputPsiProgElemStreamIndex_Object = MibTableColumn
vqdInputPsiProgElemStreamIndex = _VqdInputPsiProgElemStreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 7, 1, 1),
    _VqdInputPsiProgElemStreamIndex_Type()
)
vqdInputPsiProgElemStreamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vqdInputPsiProgElemStreamIndex.setStatus("current")
_VqdInputPsiProgElemStreamProgNum_Type = ProgramNumber
_VqdInputPsiProgElemStreamProgNum_Object = MibTableColumn
vqdInputPsiProgElemStreamProgNum = _VqdInputPsiProgElemStreamProgNum_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 7, 1, 2),
    _VqdInputPsiProgElemStreamProgNum_Type()
)
vqdInputPsiProgElemStreamProgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdInputPsiProgElemStreamProgNum.setStatus("current")
_VqdInputPsiProgElemStreamType_Type = Unsigned32
_VqdInputPsiProgElemStreamType_Object = MibTableColumn
vqdInputPsiProgElemStreamType = _VqdInputPsiProgElemStreamType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 7, 1, 3),
    _VqdInputPsiProgElemStreamType_Type()
)
vqdInputPsiProgElemStreamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdInputPsiProgElemStreamType.setStatus("current")
_VqdInputPsiProgElemStreamDescr_Type = SnmpAdminString
_VqdInputPsiProgElemStreamDescr_Object = MibTableColumn
vqdInputPsiProgElemStreamDescr = _VqdInputPsiProgElemStreamDescr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 2, 7, 1, 4),
    _VqdInputPsiProgElemStreamDescr_Type()
)
vqdInputPsiProgElemStreamDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdInputPsiProgElemStreamDescr.setStatus("current")
_VqdOutputObjects_ObjectIdentity = ObjectIdentity
vqdOutputObjects = _VqdOutputObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3)
)
_VqdOutQamTable_Object = MibTable
vqdOutQamTable = _VqdOutQamTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    vqdOutQamTable.setStatus("current")
_VqdOutQamEntry_Object = MibTableRow
vqdOutQamEntry = _VqdOutQamEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 1, 1)
)
vqdOutQamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vqdOutQamEntry.setStatus("current")
_VqdOutQamFrequency_Type = Unsigned32
_VqdOutQamFrequency_Object = MibTableColumn
vqdOutQamFrequency = _VqdOutQamFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 1, 1, 1),
    _VqdOutQamFrequency_Type()
)
vqdOutQamFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vqdOutQamFrequency.setStatus("current")
if mibBuilder.loadTexts:
    vqdOutQamFrequency.setUnits("Hz")
_VqdOutQamPower_Type = Integer32
_VqdOutQamPower_Object = MibTableColumn
vqdOutQamPower = _VqdOutQamPower_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 1, 1, 2),
    _VqdOutQamPower_Type()
)
vqdOutQamPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vqdOutQamPower.setStatus("current")
if mibBuilder.loadTexts:
    vqdOutQamPower.setUnits("dBmv")


class _VqdOutModulationType_Type(Integer32):
    """Custom type vqdOutModulationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qam64", 1),
          ("qam256", 2))
    )


_VqdOutModulationType_Type.__name__ = "Integer32"
_VqdOutModulationType_Object = MibTableColumn
vqdOutModulationType = _VqdOutModulationType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 1, 1, 3),
    _VqdOutModulationType_Type()
)
vqdOutModulationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vqdOutModulationType.setStatus("current")
_VqdOutQamUncommittedBw_Type = Unsigned32
_VqdOutQamUncommittedBw_Object = MibTableColumn
vqdOutQamUncommittedBw = _VqdOutQamUncommittedBw_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 1, 1, 4),
    _VqdOutQamUncommittedBw_Type()
)
vqdOutQamUncommittedBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vqdOutQamUncommittedBw.setStatus("current")
if mibBuilder.loadTexts:
    vqdOutQamUncommittedBw.setUnits("bps")
_VqdOutQamUtilization_Type = Unsigned32
_VqdOutQamUtilization_Object = MibTableColumn
vqdOutQamUtilization = _VqdOutQamUtilization_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 1, 1, 5),
    _VqdOutQamUtilization_Type()
)
vqdOutQamUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdOutQamUtilization.setStatus("current")
if mibBuilder.loadTexts:
    vqdOutQamUtilization.setUnits("%")
_VqdOutQamUtilLowThreshold_Type = Unsigned32
_VqdOutQamUtilLowThreshold_Object = MibTableColumn
vqdOutQamUtilLowThreshold = _VqdOutQamUtilLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 1, 1, 6),
    _VqdOutQamUtilLowThreshold_Type()
)
vqdOutQamUtilLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vqdOutQamUtilLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vqdOutQamUtilLowThreshold.setUnits("%")
_VqdOutQamUtilHighThreshold_Type = Unsigned32
_VqdOutQamUtilHighThreshold_Object = MibTableColumn
vqdOutQamUtilHighThreshold = _VqdOutQamUtilHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 1, 1, 7),
    _VqdOutQamUtilHighThreshold_Type()
)
vqdOutQamUtilHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vqdOutQamUtilHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vqdOutQamUtilHighThreshold.setUnits("%")


class _VqdOutQamTsid_Type(Unsigned32):
    """Custom type vqdOutQamTsid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VqdOutQamTsid_Type.__name__ = "Unsigned32"
_VqdOutQamTsid_Object = MibTableColumn
vqdOutQamTsid = _VqdOutQamTsid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 1, 1, 8),
    _VqdOutQamTsid_Type()
)
vqdOutQamTsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vqdOutQamTsid.setStatus("current")


class _VqdOutQamNitPid_Type(Pid):
    """Custom type vqdOutQamNitPid based on Pid"""
    subtypeSpec = Pid.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 8191),
    )


_VqdOutQamNitPid_Type.__name__ = "Pid"
_VqdOutQamNitPid_Object = MibTableColumn
vqdOutQamNitPid = _VqdOutQamNitPid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 1, 1, 9),
    _VqdOutQamNitPid_Type()
)
vqdOutQamNitPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vqdOutQamNitPid.setStatus("current")
_VqdOutQamPatInterval_Type = Unsigned32
_VqdOutQamPatInterval_Object = MibTableColumn
vqdOutQamPatInterval = _VqdOutQamPatInterval_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 1, 1, 10),
    _VqdOutQamPatInterval_Type()
)
vqdOutQamPatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vqdOutQamPatInterval.setStatus("current")
if mibBuilder.loadTexts:
    vqdOutQamPatInterval.setUnits("milliseconds")
_VqdOutQamPmtInterval_Type = Unsigned32
_VqdOutQamPmtInterval_Object = MibTableColumn
vqdOutQamPmtInterval = _VqdOutQamPmtInterval_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 1, 1, 11),
    _VqdOutQamPmtInterval_Type()
)
vqdOutQamPmtInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vqdOutQamPmtInterval.setStatus("current")
if mibBuilder.loadTexts:
    vqdOutQamPmtInterval.setUnits("milliseconds")


class _VqdOutQamInterleaverLevel_Type(Integer32):
    """Custom type vqdOutQamInterleaverLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2))
    )


_VqdOutQamInterleaverLevel_Type.__name__ = "Integer32"
_VqdOutQamInterleaverLevel_Object = MibTableColumn
vqdOutQamInterleaverLevel = _VqdOutQamInterleaverLevel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 1, 1, 12),
    _VqdOutQamInterleaverLevel_Type()
)
vqdOutQamInterleaverLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vqdOutQamInterleaverLevel.setStatus("current")


class _VqdOutQamInterleaverMode_Type(Integer32):
    """Custom type vqdOutQamInterleaverMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              12,
              14)
        )
    )
    namedValues = NamedValues(
        *(("fecI128J1", 1),
          ("fecI128J2", 2),
          ("fecI64J2", 3),
          ("fecI128J3", 4),
          ("fecI32J4", 5),
          ("fecI128J4", 6),
          ("fecI16J8", 7),
          ("fecI128J5", 8),
          ("fecI8J16", 9),
          ("fecI128J6", 10),
          ("fecI128J7", 12),
          ("fecI128J8", 14))
    )


_VqdOutQamInterleaverMode_Type.__name__ = "Integer32"
_VqdOutQamInterleaverMode_Object = MibTableColumn
vqdOutQamInterleaverMode = _VqdOutQamInterleaverMode_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 1, 1, 13),
    _VqdOutQamInterleaverMode_Type()
)
vqdOutQamInterleaverMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vqdOutQamInterleaverMode.setStatus("current")


class _VqdOutQamAnnexMode_Type(Integer32):
    """Custom type vqdOutQamAnnexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("annexA", 1),
          ("annexB", 2),
          ("annexC", 3))
    )


_VqdOutQamAnnexMode_Type.__name__ = "Integer32"
_VqdOutQamAnnexMode_Object = MibTableColumn
vqdOutQamAnnexMode = _VqdOutQamAnnexMode_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 1, 1, 14),
    _VqdOutQamAnnexMode_Type()
)
vqdOutQamAnnexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vqdOutQamAnnexMode.setStatus("current")


class _VqdOutQamChannelBandwidth_Type(Integer32):
    """Custom type vqdOutQamChannelBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mhz6", 1),
          ("mhz8", 2))
    )


_VqdOutQamChannelBandwidth_Type.__name__ = "Integer32"
_VqdOutQamChannelBandwidth_Object = MibTableColumn
vqdOutQamChannelBandwidth = _VqdOutQamChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 1, 1, 15),
    _VqdOutQamChannelBandwidth_Type()
)
vqdOutQamChannelBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vqdOutQamChannelBandwidth.setStatus("current")
_VqdOutQamNGODTable_Object = MibTable
vqdOutQamNGODTable = _VqdOutQamNGODTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    vqdOutQamNGODTable.setStatus("current")
_VqdOutQamPsiTable_Object = MibTable
vqdOutQamPsiTable = _VqdOutQamPsiTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    vqdOutQamPsiTable.setStatus("current")
_VqdOutQamNGODEntry_Object = MibTableRow
vqdOutQamNGODEntry = _VqdOutQamNGODEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 2, 1)
)
vqdOutQamNGODEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vqdOutQamNGODEntry.setStatus("current")
_VqdOutQamPsiEntry_Object = MibTableRow
vqdOutQamPsiEntry = _VqdOutQamPsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 2, 1)
)
vqdOutQamPsiEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VIDEO-QAM-DEVICE-MIB", "vqdOutQamProgramNum"),
)
if mibBuilder.loadTexts:
    vqdOutQamPsiEntry.setStatus("current")
_VqdOutQamNGODQAMName_Type = SnmpAdminString
_VqdOutQamNGODQAMName_Object = MibTableColumn
vqdOutQamNGODQAMName = _VqdOutQamNGODQAMName_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 2, 1, 1),
    _VqdOutQamNGODQAMName_Type()
)
vqdOutQamNGODQAMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdOutQamNGODQAMName.setStatus("current")
_VqdOutQamProgramNum_Type = ProgramNumber
_VqdOutQamProgramNum_Object = MibTableColumn
vqdOutQamProgramNum = _VqdOutQamProgramNum_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 2, 1, 1),
    _VqdOutQamProgramNum_Type()
)
vqdOutQamProgramNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vqdOutQamProgramNum.setStatus("current")
_VqdOutQamNGODQAMGroupName_Type = SnmpAdminString
_VqdOutQamNGODQAMGroupName_Object = MibTableColumn
vqdOutQamNGODQAMGroupName = _VqdOutQamNGODQAMGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 2, 1, 2),
    _VqdOutQamNGODQAMGroupName_Type()
)
vqdOutQamNGODQAMGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdOutQamNGODQAMGroupName.setStatus("current")
_VqdOutQamSessDestAddressType_Type = InetAddressType
_VqdOutQamSessDestAddressType_Object = MibTableColumn
vqdOutQamSessDestAddressType = _VqdOutQamSessDestAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 2, 1, 2),
    _VqdOutQamSessDestAddressType_Type()
)
vqdOutQamSessDestAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdOutQamSessDestAddressType.setStatus("current")
_VqdOutQamNGODInbandCarriageType_Type = Integer32
_VqdOutQamNGODInbandCarriageType_Object = MibTableColumn
vqdOutQamNGODInbandCarriageType = _VqdOutQamNGODInbandCarriageType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 2, 1, 3),
    _VqdOutQamNGODInbandCarriageType_Type()
)
vqdOutQamNGODInbandCarriageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vqdOutQamNGODInbandCarriageType.setStatus("current")
_VqdOutQamSessDestAddress_Type = InetAddress
_VqdOutQamSessDestAddress_Object = MibTableColumn
vqdOutQamSessDestAddress = _VqdOutQamSessDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 2, 1, 3),
    _VqdOutQamSessDestAddress_Type()
)
vqdOutQamSessDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdOutQamSessDestAddress.setStatus("current")
_VqdOutQamNGODInbandMarkerType_Type = Integer32
_VqdOutQamNGODInbandMarkerType_Object = MibTableColumn
vqdOutQamNGODInbandMarkerType = _VqdOutQamNGODInbandMarkerType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 2, 1, 4),
    _VqdOutQamNGODInbandMarkerType_Type()
)
vqdOutQamNGODInbandMarkerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vqdOutQamNGODInbandMarkerType.setStatus("current")
_VqdOutQamSessionNum_Type = VideoUdpPort
_VqdOutQamSessionNum_Object = MibTableColumn
vqdOutQamSessionNum = _VqdOutQamSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 2, 1, 4),
    _VqdOutQamSessionNum_Type()
)
vqdOutQamSessionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdOutQamSessionNum.setStatus("current")
_VqdOutQamNGODInbandMarkerSubType_Type = Integer32
_VqdOutQamNGODInbandMarkerSubType_Object = MibTableColumn
vqdOutQamNGODInbandMarkerSubType = _VqdOutQamNGODInbandMarkerSubType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 2, 1, 5),
    _VqdOutQamNGODInbandMarkerSubType_Type()
)
vqdOutQamNGODInbandMarkerSubType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vqdOutQamNGODInbandMarkerSubType.setStatus("current")
_VqdOutQamPmtPid_Type = Pid
_VqdOutQamPmtPid_Object = MibTableColumn
vqdOutQamPmtPid = _VqdOutQamPmtPid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 2, 1, 5),
    _VqdOutQamPmtPid_Type()
)
vqdOutQamPmtPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdOutQamPmtPid.setStatus("current")
_VqdOutQamNGODInbandMarkerValue_Type = SnmpAdminString
_VqdOutQamNGODInbandMarkerValue_Object = MibTableColumn
vqdOutQamNGODInbandMarkerValue = _VqdOutQamNGODInbandMarkerValue_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 2, 1, 6),
    _VqdOutQamNGODInbandMarkerValue_Type()
)
vqdOutQamNGODInbandMarkerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vqdOutQamNGODInbandMarkerValue.setStatus("current")
_VqdOutQamPcrPid_Type = Pid
_VqdOutQamPcrPid_Object = MibTableColumn
vqdOutQamPcrPid = _VqdOutQamPcrPid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 2, 1, 6),
    _VqdOutQamPcrPid_Type()
)
vqdOutQamPcrPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdOutQamPcrPid.setStatus("current")
_VqdOutQamNGODInbandProgramNum_Type = ProgramNumber
_VqdOutQamNGODInbandProgramNum_Object = MibTableColumn
vqdOutQamNGODInbandProgramNum = _VqdOutQamNGODInbandProgramNum_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 2, 1, 7),
    _VqdOutQamNGODInbandProgramNum_Type()
)
vqdOutQamNGODInbandProgramNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vqdOutQamNGODInbandProgramNum.setStatus("current")
_VqdOutQamVideoPid_Type = Pid
_VqdOutQamVideoPid_Object = MibTableColumn
vqdOutQamVideoPid = _VqdOutQamVideoPid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 2, 1, 7),
    _VqdOutQamVideoPid_Type()
)
vqdOutQamVideoPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdOutQamVideoPid.setStatus("current")
_VqdOutQamNGODInbandInsertInterval_Type = Unsigned32
_VqdOutQamNGODInbandInsertInterval_Object = MibTableColumn
vqdOutQamNGODInbandInsertInterval = _VqdOutQamNGODInbandInsertInterval_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 2, 1, 8),
    _VqdOutQamNGODInbandInsertInterval_Type()
)
vqdOutQamNGODInbandInsertInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vqdOutQamNGODInbandInsertInterval.setStatus("current")
_VqdOutQamEcmPid1_Type = Pid
_VqdOutQamEcmPid1_Object = MibTableColumn
vqdOutQamEcmPid1 = _VqdOutQamEcmPid1_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 2, 1, 8),
    _VqdOutQamEcmPid1_Type()
)
vqdOutQamEcmPid1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdOutQamEcmPid1.setStatus("current")
_VqdOutQamEcmPid2_Type = Pid
_VqdOutQamEcmPid2_Object = MibTableColumn
vqdOutQamEcmPid2 = _VqdOutQamEcmPid2_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 3, 2, 1, 9),
    _VqdOutQamEcmPid2_Type()
)
vqdOutQamEcmPid2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vqdOutQamEcmPid2.setStatus("current")
_VqdNotifInfo_ObjectIdentity = ObjectIdentity
vqdNotifInfo = _VqdNotifInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 4)
)
_VqdNotifEnable_Type = TruthValue
_VqdNotifEnable_Object = MibScalar
vqdNotifEnable = _VqdNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 1, 4, 1),
    _VqdNotifEnable_Type()
)
vqdNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vqdNotifEnable.setStatus("current")
_VideoQamDeviceMIBConformance_ObjectIdentity = ObjectIdentity
videoQamDeviceMIBConformance = _VideoQamDeviceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 2)
)
_VideoQamDeviceMIBCompliances_ObjectIdentity = ObjectIdentity
videoQamDeviceMIBCompliances = _VideoQamDeviceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 2, 1)
)
_VideoQamDeviceMIBGroups_ObjectIdentity = ObjectIdentity
videoQamDeviceMIBGroups = _VideoQamDeviceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 2, 2)
)

# Managed Objects groups

vqdQamConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 2, 2, 1)
)
vqdQamConfigGroup.setObjects(
      *(("VIDEO-QAM-DEVICE-MIB", "vqdOutQamFrequency"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutQamPower"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutModulationType"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutQamUncommittedBw"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutQamUtilization"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutQamUtilLowThreshold"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutQamUtilHighThreshold"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutQamTsid"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutQamNitPid"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutQamPatInterval"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutQamPmtInterval"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutQamInterleaverLevel"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutQamInterleaverMode"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutQamAnnexMode"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutQamChannelBandwidth"),
        ("VIDEO-QAM-DEVICE-MIB", "VqdOutQamNGODQAMName"),
        ("VIDEO-QAM-DEVICE-MIB", "VqdOutQamNGODQAMGroupName"),
        ("VIDEO-QAM-DEVICE-MIB", "VqdOutQamNGODInbandCarriageType"),
        ("VIDEO-QAM-DEVICE-MIB", "VqdOutQamNGODInbandMarkerType"),
        ("VIDEO-QAM-DEVICE-MIB", "VqdOutQamNGODInbandMarkerSubType"),
        ("VIDEO-QAM-DEVICE-MIB", "VqdOutQamNGODInbandMarkerValue"),
        ("VIDEO-QAM-DEVICE-MIB", "VqdOutQamNGODInbandProgramNum"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutQamNGODInbandInsertInterval"))
)
if mibBuilder.loadTexts:
    vqdQamConfigGroup.setStatus("current")

vqdSessionInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 2, 2, 2)
)
vqdSessionInfoGroup.setObjects(
      *(("VIDEO-QAM-DEVICE-MIB", "vqdSignalLossTimeout"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdVideoSessBandwidth"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdVideoSessStartTime"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdVideoSessMaxJitter"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdVideoSessStatus"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdVideoSessQamIndex"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdNGODVideoSessDestAddressType"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdNGODVideoSessDestAddress"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdNGODVideoSessIndex"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdNGODVideoSessOnDemandSessionId"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdSessStatsCurrentBitrate"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdSessStatsAvgBitrate"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdSessStatsPeakJitter"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdSessStatsAvgJitter"))
)
if mibBuilder.loadTexts:
    vqdSessionInfoGroup.setStatus("current")

vqdSessionDetailedStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 2, 2, 3)
)
vqdSessionDetailedStatsGroup.setObjects(
      *(("VIDEO-QAM-DEVICE-MIB", "vqdSessDetStatsSyncLosses"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdSessDetStatsPcrFrequencyDiff"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdSessDetStatsPcrPackets"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdSessDetStatsNonPcrPackets"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdSessDetStatsDroppedPackets"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdSessDetStatsDiscontinuityPcrs"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdSessDetStatsContinuityErrors"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdSessDetStatsUnderflows"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdSessDetStatsOverflows"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdSessDetStatsMaxPcrInterval"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdSessDetStatsAvgPcrInterval"))
)
if mibBuilder.loadTexts:
    vqdSessionDetailedStatsGroup.setStatus("current")

vqdInputPSIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 2, 2, 4)
)
vqdInputPSIGroup.setObjects(
      *(("VIDEO-QAM-DEVICE-MIB", "vqdInputPsiTsid"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdInputPsiPatVersion"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdInputPsiCatVersion"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdInputPsiNitPid"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdInputPsiNumPrograms"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdInputPsiNumEmms"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdInputPsiProgPmtVersion"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdInputPsiProgPmtPid"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdInputPsiProgPcrPid"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdInputPsiProgEcmPid"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdInputPsiProgNumElems"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdInputPsiProgNumEcms"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdInputPsiProgCaDescr"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdInputPsiProgElemStreamProgNum"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdInputPsiProgElemStreamType"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdInputPsiProgElemStreamDescr"))
)
if mibBuilder.loadTexts:
    vqdInputPSIGroup.setStatus("current")

vqdOutputPSIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 2, 2, 5)
)
vqdOutputPSIGroup.setObjects(
      *(("VIDEO-QAM-DEVICE-MIB", "vqdOutQamSessDestAddressType"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutQamSessDestAddress"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutQamSessionNum"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutQamPmtPid"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutQamPcrPid"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutQamVideoPid"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutQamEcmPid1"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutQamEcmPid2"))
)
if mibBuilder.loadTexts:
    vqdOutputPSIGroup.setStatus("current")

vqdNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 2, 2, 6)
)
vqdNotifControlGroup.setObjects(
    ("VIDEO-QAM-DEVICE-MIB", "vqdNotifEnable")
)
if mibBuilder.loadTexts:
    vqdNotifControlGroup.setStatus("current")


# Notification objects

vqdQamUtilThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 0, 1)
)
vqdQamUtilThresholdNotification.setObjects(
      *(("VIDEO-QAM-DEVICE-MIB", "vqdOutQamUtilization"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutQamUtilHighThreshold"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutQamUtilLowThreshold"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutQamTsid"))
)
if mibBuilder.loadTexts:
    vqdQamUtilThresholdNotification.setStatus(
        "current"
    )

vqdSessionPsiFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 0, 2)
)
vqdSessionPsiFailNotification.setObjects(
      *(("VIDEO-QAM-DEVICE-MIB", "vqdVideoSessOnDemandSessionId"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdVideoSessQamIndex"))
)
if mibBuilder.loadTexts:
    vqdSessionPsiFailNotification.setStatus(
        "current"
    )


# Notifications groups

vqdNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 2, 2, 7)
)
vqdNotificationGroup.setObjects(
      *(("VIDEO-QAM-DEVICE-MIB", "vqdQamUtilThresholdNotification"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdSessionPsiFailNotification"))
)
if mibBuilder.loadTexts:
    vqdNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

videoQamDeviceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 3, 2, 1, 1)
)
videoQamDeviceCompliance.setObjects(
      *(("VIDEO-QAM-DEVICE-MIB", "vqdQamConfigGroup"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdSessionInfoGroup"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdNotifControlGroup"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdNotificationGroup"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdSessionDetailedStatsGroup"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdInputPSIGroup"),
        ("VIDEO-QAM-DEVICE-MIB", "vqdOutputPSIGroup"))
)
if mibBuilder.loadTexts:
    videoQamDeviceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIDEO-QAM-DEVICE-MIB",
    **{"Pid": Pid,
       "ProgramNumber": ProgramNumber,
       "VideoUdpPort": VideoUdpPort,
       "videoQamDeviceMIB": videoQamDeviceMIB,
       "videoQamDeviceMIBNotifs": videoQamDeviceMIBNotifs,
       "vqdQamUtilThresholdNotification": vqdQamUtilThresholdNotification,
       "vqdSessionPsiFailNotification": vqdSessionPsiFailNotification,
       "videoQamDeviceMIBObjects": videoQamDeviceMIBObjects,
       "vqdBaseObjects": vqdBaseObjects,
       "vqdInputObjects": vqdInputObjects,
       "vqdSignalLossTimeout": vqdSignalLossTimeout,
       "vqdVideoSessionTable": vqdVideoSessionTable,
       "vqdVideoSessionEntry": vqdVideoSessionEntry,
       "vqdVideoSessDestAddressType": vqdVideoSessDestAddressType,
       "vqdVideoSessDestAddress": vqdVideoSessDestAddress,
       "vqdVideoSessIndex": vqdVideoSessIndex,
       "vqdVideoSessBandwidth": vqdVideoSessBandwidth,
       "vqdVideoSessStartTime": vqdVideoSessStartTime,
       "vqdVideoSessMaxJitter": vqdVideoSessMaxJitter,
       "vqdVideoSessStatus": vqdVideoSessStatus,
       "vqdVideoSessQamIndex": vqdVideoSessQamIndex,
       "vqdNGODVideoSessionTable": vqdNGODVideoSessionTable,
       "vqdSessionStatsTable": vqdSessionStatsTable,
       "vqdNGODVideoSessionEntry": vqdNGODVideoSessionEntry,
       "vqdSessionStatsEntry": vqdSessionStatsEntry,
       "vqdNGODVideoSessOnDemandSessionId": vqdNGODVideoSessOnDemandSessionId,
       "vqdSessStatsCurrentBitrate": vqdSessStatsCurrentBitrate,
       "vqdSessStatsAvgBitrate": vqdSessStatsAvgBitrate,
       "vqdSessStatsPeakJitter": vqdSessStatsPeakJitter,
       "vqdSessStatsAvgJitter": vqdSessStatsAvgJitter,
       "vqdSessionDetStatsTable": vqdSessionDetStatsTable,
       "vqdSessionDetStatsEntry": vqdSessionDetStatsEntry,
       "vqdSessDetStatsSyncLosses": vqdSessDetStatsSyncLosses,
       "vqdSessDetStatsPcrFrequencyDiff": vqdSessDetStatsPcrFrequencyDiff,
       "vqdSessDetStatsPcrPackets": vqdSessDetStatsPcrPackets,
       "vqdSessDetStatsNonPcrPackets": vqdSessDetStatsNonPcrPackets,
       "vqdSessDetStatsDroppedPackets": vqdSessDetStatsDroppedPackets,
       "vqdSessDetStatsDiscontinuityPcrs": vqdSessDetStatsDiscontinuityPcrs,
       "vqdSessDetStatsContinuityErrors": vqdSessDetStatsContinuityErrors,
       "vqdSessDetStatsUnderflows": vqdSessDetStatsUnderflows,
       "vqdSessDetStatsOverflows": vqdSessDetStatsOverflows,
       "vqdSessDetStatsMaxPcrInterval": vqdSessDetStatsMaxPcrInterval,
       "vqdSessDetStatsAvgPcrInterval": vqdSessDetStatsAvgPcrInterval,
       "vqdInputPsiTable": vqdInputPsiTable,
       "vqdInputPsiEntry": vqdInputPsiEntry,
       "vqdInputPsiTsid": vqdInputPsiTsid,
       "vqdInputPsiPatVersion": vqdInputPsiPatVersion,
       "vqdInputPsiCatVersion": vqdInputPsiCatVersion,
       "vqdInputPsiNitPid": vqdInputPsiNitPid,
       "vqdInputPsiNumPrograms": vqdInputPsiNumPrograms,
       "vqdInputPsiNumEmms": vqdInputPsiNumEmms,
       "vqdInputPsiProgTable": vqdInputPsiProgTable,
       "vqdInputPsiProgEntry": vqdInputPsiProgEntry,
       "vqdInputPsiProgIndex": vqdInputPsiProgIndex,
       "vqdInputPsiProgPmtVersion": vqdInputPsiProgPmtVersion,
       "vqdInputPsiProgPmtPid": vqdInputPsiProgPmtPid,
       "vqdInputPsiProgPcrPid": vqdInputPsiProgPcrPid,
       "vqdInputPsiProgEcmPid": vqdInputPsiProgEcmPid,
       "vqdInputPsiProgNumElems": vqdInputPsiProgNumElems,
       "vqdInputPsiProgNumEcms": vqdInputPsiProgNumEcms,
       "vqdInputPsiProgCaDescr": vqdInputPsiProgCaDescr,
       "vqdInputPsiProgElemStreamTable": vqdInputPsiProgElemStreamTable,
       "vqdInputPsiProgElemStreamEntry": vqdInputPsiProgElemStreamEntry,
       "vqdInputPsiProgElemStreamIndex": vqdInputPsiProgElemStreamIndex,
       "vqdInputPsiProgElemStreamProgNum": vqdInputPsiProgElemStreamProgNum,
       "vqdInputPsiProgElemStreamType": vqdInputPsiProgElemStreamType,
       "vqdInputPsiProgElemStreamDescr": vqdInputPsiProgElemStreamDescr,
       "vqdOutputObjects": vqdOutputObjects,
       "vqdOutQamTable": vqdOutQamTable,
       "vqdOutQamEntry": vqdOutQamEntry,
       "vqdOutQamFrequency": vqdOutQamFrequency,
       "vqdOutQamPower": vqdOutQamPower,
       "vqdOutModulationType": vqdOutModulationType,
       "vqdOutQamUncommittedBw": vqdOutQamUncommittedBw,
       "vqdOutQamUtilization": vqdOutQamUtilization,
       "vqdOutQamUtilLowThreshold": vqdOutQamUtilLowThreshold,
       "vqdOutQamUtilHighThreshold": vqdOutQamUtilHighThreshold,
       "vqdOutQamTsid": vqdOutQamTsid,
       "vqdOutQamNitPid": vqdOutQamNitPid,
       "vqdOutQamPatInterval": vqdOutQamPatInterval,
       "vqdOutQamPmtInterval": vqdOutQamPmtInterval,
       "vqdOutQamInterleaverLevel": vqdOutQamInterleaverLevel,
       "vqdOutQamInterleaverMode": vqdOutQamInterleaverMode,
       "vqdOutQamAnnexMode": vqdOutQamAnnexMode,
       "vqdOutQamChannelBandwidth": vqdOutQamChannelBandwidth,
       "vqdOutQamNGODTable": vqdOutQamNGODTable,
       "vqdOutQamPsiTable": vqdOutQamPsiTable,
       "vqdOutQamNGODEntry": vqdOutQamNGODEntry,
       "vqdOutQamPsiEntry": vqdOutQamPsiEntry,
       "vqdOutQamNGODQAMName": vqdOutQamNGODQAMName,
       "vqdOutQamProgramNum": vqdOutQamProgramNum,
       "vqdOutQamNGODQAMGroupName": vqdOutQamNGODQAMGroupName,
       "vqdOutQamSessDestAddressType": vqdOutQamSessDestAddressType,
       "vqdOutQamNGODInbandCarriageType": vqdOutQamNGODInbandCarriageType,
       "vqdOutQamSessDestAddress": vqdOutQamSessDestAddress,
       "vqdOutQamNGODInbandMarkerType": vqdOutQamNGODInbandMarkerType,
       "vqdOutQamSessionNum": vqdOutQamSessionNum,
       "vqdOutQamNGODInbandMarkerSubType": vqdOutQamNGODInbandMarkerSubType,
       "vqdOutQamPmtPid": vqdOutQamPmtPid,
       "vqdOutQamNGODInbandMarkerValue": vqdOutQamNGODInbandMarkerValue,
       "vqdOutQamPcrPid": vqdOutQamPcrPid,
       "vqdOutQamNGODInbandProgramNum": vqdOutQamNGODInbandProgramNum,
       "vqdOutQamVideoPid": vqdOutQamVideoPid,
       "vqdOutQamNGODInbandInsertInterval": vqdOutQamNGODInbandInsertInterval,
       "vqdOutQamEcmPid1": vqdOutQamEcmPid1,
       "vqdOutQamEcmPid2": vqdOutQamEcmPid2,
       "vqdNotifInfo": vqdNotifInfo,
       "vqdNotifEnable": vqdNotifEnable,
       "videoQamDeviceMIBConformance": videoQamDeviceMIBConformance,
       "videoQamDeviceMIBCompliances": videoQamDeviceMIBCompliances,
       "videoQamDeviceCompliance": videoQamDeviceCompliance,
       "videoQamDeviceMIBGroups": videoQamDeviceMIBGroups,
       "vqdQamConfigGroup": vqdQamConfigGroup,
       "vqdSessionInfoGroup": vqdSessionInfoGroup,
       "vqdSessionDetailedStatsGroup": vqdSessionDetailedStatsGroup,
       "vqdInputPSIGroup": vqdInputPSIGroup,
       "vqdOutputPSIGroup": vqdOutputPSIGroup,
       "vqdNotifControlGroup": vqdNotifControlGroup,
       "vqdNotificationGroup": vqdNotificationGroup}
)
