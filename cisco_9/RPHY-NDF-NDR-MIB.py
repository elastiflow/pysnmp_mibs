# SNMP MIB module (RPHY-NDF-NDR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/RPHY-NDF-NDR-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:16:23 2025
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

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rphyNdfNdrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 857)
)
if mibBuilder.loadTexts:
    rphyNdfNdrMIB.setRevisions(
        ("2018-09-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RphyNdfNdrMIBNotifs_ObjectIdentity = ObjectIdentity
rphyNdfNdrMIBNotifs = _RphyNdfNdrMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 0)
)
_RphyNdfNdrMIBObjects_ObjectIdentity = ObjectIdentity
rphyNdfNdrMIBObjects = _RphyNdfNdrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1)
)
_DocsRphyRpdDevNdfCfgTable_Object = MibTable
docsRphyRpdDevNdfCfgTable = _DocsRphyRpdDevNdfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 1)
)
if mibBuilder.loadTexts:
    docsRphyRpdDevNdfCfgTable.setStatus("current")
_DocsRphyRpdDevNdfCfgEntry_Object = MibTableRow
docsRphyRpdDevNdfCfgEntry = _DocsRphyRpdDevNdfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 1, 1)
)
docsRphyRpdDevNdfCfgEntry.setIndexNames(
    (0, "RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdfUniqueId"),
    (0, "RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdfRfPort"),
    (0, "RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdfRfChannel"),
)
if mibBuilder.loadTexts:
    docsRphyRpdDevNdfCfgEntry.setStatus("current")
_DocsRphyRpdDevNdfUniqueId_Type = MacAddress
_DocsRphyRpdDevNdfUniqueId_Object = MibTableColumn
docsRphyRpdDevNdfUniqueId = _DocsRphyRpdDevNdfUniqueId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 1, 1, 1),
    _DocsRphyRpdDevNdfUniqueId_Type()
)
docsRphyRpdDevNdfUniqueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdfUniqueId.setStatus("current")
_DocsRphyRpdDevNdfRfPort_Type = Unsigned32
_DocsRphyRpdDevNdfRfPort_Object = MibTableColumn
docsRphyRpdDevNdfRfPort = _DocsRphyRpdDevNdfRfPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 1, 1, 2),
    _DocsRphyRpdDevNdfRfPort_Type()
)
docsRphyRpdDevNdfRfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdfRfPort.setStatus("current")
_DocsRphyRpdDevNdfRfChannel_Type = Unsigned32
_DocsRphyRpdDevNdfRfChannel_Object = MibTableColumn
docsRphyRpdDevNdfRfChannel = _DocsRphyRpdDevNdfRfChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 1, 1, 3),
    _DocsRphyRpdDevNdfRfChannel_Type()
)
docsRphyRpdDevNdfRfChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdfRfChannel.setStatus("current")
_DocsRphyRpdDevNdfEnable_Type = TruthValue
_DocsRphyRpdDevNdfEnable_Object = MibTableColumn
docsRphyRpdDevNdfEnable = _DocsRphyRpdDevNdfEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 1, 1, 4),
    _DocsRphyRpdDevNdfEnable_Type()
)
docsRphyRpdDevNdfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdfEnable.setStatus("current")
_DocsRphyRpdDevNdfDstIPAddr_Type = InetAddress
_DocsRphyRpdDevNdfDstIPAddr_Object = MibTableColumn
docsRphyRpdDevNdfDstIPAddr = _DocsRphyRpdDevNdfDstIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 1, 1, 5),
    _DocsRphyRpdDevNdfDstIPAddr_Type()
)
docsRphyRpdDevNdfDstIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdfDstIPAddr.setStatus("current")
_DocsRphyRpdDevNdfSrcIPAddr_Type = InetAddress
_DocsRphyRpdDevNdfSrcIPAddr_Object = MibTableColumn
docsRphyRpdDevNdfSrcIPAddr = _DocsRphyRpdDevNdfSrcIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 1, 1, 6),
    _DocsRphyRpdDevNdfSrcIPAddr_Type()
)
docsRphyRpdDevNdfSrcIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdfSrcIPAddr.setStatus("current")


class _DocsRphyRpdDevNdfSessionId_Type(Unsigned32):
    """Custom type docsRphyRpdDevNdfSessionId based on Unsigned32"""
    defaultValue = 0


_DocsRphyRpdDevNdfSessionId_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevNdfSessionId_Object = MibTableColumn
docsRphyRpdDevNdfSessionId = _DocsRphyRpdDevNdfSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 1, 1, 7),
    _DocsRphyRpdDevNdfSessionId_Type()
)
docsRphyRpdDevNdfSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdfSessionId.setStatus("current")


class _DocsRphyRpdDevNdfFrequency_Type(Unsigned32):
    """Custom type docsRphyRpdDevNdfFrequency based on Unsigned32"""
    defaultValue = 0


_DocsRphyRpdDevNdfFrequency_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevNdfFrequency_Object = MibTableColumn
docsRphyRpdDevNdfFrequency = _DocsRphyRpdDevNdfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 1, 1, 8),
    _DocsRphyRpdDevNdfFrequency_Type()
)
docsRphyRpdDevNdfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdfFrequency.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdfFrequency.setUnits("Hertz")
_DocsRphyRpdDevNdfBandwidth_Type = Unsigned32
_DocsRphyRpdDevNdfBandwidth_Object = MibTableColumn
docsRphyRpdDevNdfBandwidth = _DocsRphyRpdDevNdfBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 1, 1, 9),
    _DocsRphyRpdDevNdfBandwidth_Type()
)
docsRphyRpdDevNdfBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdfBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdfBandwidth.setUnits("Hertz")


class _DocsRphyRpdDevNdfPowerAdjust_Type(Integer32):
    """Custom type docsRphyRpdDevNdfPowerAdjust based on Integer32"""
    defaultValue = 0


_DocsRphyRpdDevNdfPowerAdjust_Type.__name__ = "Integer32"
_DocsRphyRpdDevNdfPowerAdjust_Object = MibTableColumn
docsRphyRpdDevNdfPowerAdjust = _DocsRphyRpdDevNdfPowerAdjust_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 1, 1, 10),
    _DocsRphyRpdDevNdfPowerAdjust_Type()
)
docsRphyRpdDevNdfPowerAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdfPowerAdjust.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdfPowerAdjust.setUnits("TenthdB")
_DocsRphyRpdDevNdfRfMute_Type = TruthValue
_DocsRphyRpdDevNdfRfMute_Object = MibTableColumn
docsRphyRpdDevNdfRfMute = _DocsRphyRpdDevNdfRfMute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 1, 1, 11),
    _DocsRphyRpdDevNdfRfMute_Type()
)
docsRphyRpdDevNdfRfMute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdfRfMute.setStatus("current")
_DocsRphyRpdDevNdfIsUnicast_Type = TruthValue
_DocsRphyRpdDevNdfIsUnicast_Object = MibTableColumn
docsRphyRpdDevNdfIsUnicast = _DocsRphyRpdDevNdfIsUnicast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 1, 1, 12),
    _DocsRphyRpdDevNdfIsUnicast_Type()
)
docsRphyRpdDevNdfIsUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdfIsUnicast.setStatus("current")
_DocsRphyRpdDevNdfRpdStatus_Type = OctetString
_DocsRphyRpdDevNdfRpdStatus_Object = MibTableColumn
docsRphyRpdDevNdfRpdStatus = _DocsRphyRpdDevNdfRpdStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 1, 1, 13),
    _DocsRphyRpdDevNdfRpdStatus_Type()
)
docsRphyRpdDevNdfRpdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdfRpdStatus.setStatus("current")
_DocsRphyRpdDevNdfRpdInPktCount_Type = Counter64
_DocsRphyRpdDevNdfRpdInPktCount_Object = MibTableColumn
docsRphyRpdDevNdfRpdInPktCount = _DocsRphyRpdDevNdfRpdInPktCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 1, 1, 14),
    _DocsRphyRpdDevNdfRpdInPktCount_Type()
)
docsRphyRpdDevNdfRpdInPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdfRpdInPktCount.setStatus("current")
_DocsRphyRpdDevNdfRpdOutPktCount_Type = Counter64
_DocsRphyRpdDevNdfRpdOutPktCount_Object = MibTableColumn
docsRphyRpdDevNdfRpdOutPktCount = _DocsRphyRpdDevNdfRpdOutPktCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 1, 1, 15),
    _DocsRphyRpdDevNdfRpdOutPktCount_Type()
)
docsRphyRpdDevNdfRpdOutPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdfRpdOutPktCount.setStatus("current")
_DocsRphyRpdDevNdrCfgTable_Object = MibTable
docsRphyRpdDevNdrCfgTable = _DocsRphyRpdDevNdrCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 2)
)
if mibBuilder.loadTexts:
    docsRphyRpdDevNdrCfgTable.setStatus("current")
_DocsRphyRpdDevNdrCfgEntry_Object = MibTableRow
docsRphyRpdDevNdrCfgEntry = _DocsRphyRpdDevNdrCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 2, 1)
)
docsRphyRpdDevNdrCfgEntry.setIndexNames(
    (0, "RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdrUniqueId"),
    (0, "RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdrRfPort"),
    (0, "RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdrRfChannel"),
)
if mibBuilder.loadTexts:
    docsRphyRpdDevNdrCfgEntry.setStatus("current")
_DocsRphyRpdDevNdrUniqueId_Type = MacAddress
_DocsRphyRpdDevNdrUniqueId_Object = MibTableColumn
docsRphyRpdDevNdrUniqueId = _DocsRphyRpdDevNdrUniqueId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 2, 1, 1),
    _DocsRphyRpdDevNdrUniqueId_Type()
)
docsRphyRpdDevNdrUniqueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdrUniqueId.setStatus("current")
_DocsRphyRpdDevNdrRfPort_Type = Unsigned32
_DocsRphyRpdDevNdrRfPort_Object = MibTableColumn
docsRphyRpdDevNdrRfPort = _DocsRphyRpdDevNdrRfPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 2, 1, 2),
    _DocsRphyRpdDevNdrRfPort_Type()
)
docsRphyRpdDevNdrRfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdrRfPort.setStatus("current")
_DocsRphyRpdDevNdrRfChannel_Type = Unsigned32
_DocsRphyRpdDevNdrRfChannel_Object = MibTableColumn
docsRphyRpdDevNdrRfChannel = _DocsRphyRpdDevNdrRfChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 2, 1, 3),
    _DocsRphyRpdDevNdrRfChannel_Type()
)
docsRphyRpdDevNdrRfChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdrRfChannel.setStatus("current")
_DocsRphyRpdDevNdrEnable_Type = TruthValue
_DocsRphyRpdDevNdrEnable_Object = MibTableColumn
docsRphyRpdDevNdrEnable = _DocsRphyRpdDevNdrEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 2, 1, 4),
    _DocsRphyRpdDevNdrEnable_Type()
)
docsRphyRpdDevNdrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdrEnable.setStatus("current")
_DocsRphyRpdDevNdrDstIPAddr_Type = InetAddress
_DocsRphyRpdDevNdrDstIPAddr_Object = MibTableColumn
docsRphyRpdDevNdrDstIPAddr = _DocsRphyRpdDevNdrDstIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 2, 1, 5),
    _DocsRphyRpdDevNdrDstIPAddr_Type()
)
docsRphyRpdDevNdrDstIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdrDstIPAddr.setStatus("current")
_DocsRphyRpdDevNdrSrcIPAddr_Type = InetAddress
_DocsRphyRpdDevNdrSrcIPAddr_Object = MibTableColumn
docsRphyRpdDevNdrSrcIPAddr = _DocsRphyRpdDevNdrSrcIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 2, 1, 6),
    _DocsRphyRpdDevNdrSrcIPAddr_Type()
)
docsRphyRpdDevNdrSrcIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdrSrcIPAddr.setStatus("current")
_DocsRphyRpdDevNdrSessionId_Type = Unsigned32
_DocsRphyRpdDevNdrSessionId_Object = MibTableColumn
docsRphyRpdDevNdrSessionId = _DocsRphyRpdDevNdrSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 2, 1, 7),
    _DocsRphyRpdDevNdrSessionId_Type()
)
docsRphyRpdDevNdrSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdrSessionId.setStatus("current")


class _DocsRphyRpdDevNdrFrequency_Type(Unsigned32):
    """Custom type docsRphyRpdDevNdrFrequency based on Unsigned32"""
    defaultValue = 0


_DocsRphyRpdDevNdrFrequency_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevNdrFrequency_Object = MibTableColumn
docsRphyRpdDevNdrFrequency = _DocsRphyRpdDevNdrFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 2, 1, 8),
    _DocsRphyRpdDevNdrFrequency_Type()
)
docsRphyRpdDevNdrFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdrFrequency.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdrFrequency.setUnits("Hertz")
_DocsRphyRpdDevNdrBandwidth_Type = Unsigned32
_DocsRphyRpdDevNdrBandwidth_Object = MibTableColumn
docsRphyRpdDevNdrBandwidth = _DocsRphyRpdDevNdrBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 2, 1, 9),
    _DocsRphyRpdDevNdrBandwidth_Type()
)
docsRphyRpdDevNdrBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdrBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdrBandwidth.setUnits("Hertz")
_DocsRphyRpdDevNdrMtuSize_Type = Unsigned32
_DocsRphyRpdDevNdrMtuSize_Object = MibTableColumn
docsRphyRpdDevNdrMtuSize = _DocsRphyRpdDevNdrMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 2, 1, 10),
    _DocsRphyRpdDevNdrMtuSize_Type()
)
docsRphyRpdDevNdrMtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdrMtuSize.setStatus("current")


class _DocsRphyRpdDevNdrPhb_Type(Unsigned32):
    """Custom type docsRphyRpdDevNdrPhb based on Unsigned32"""
    defaultValue = 0


_DocsRphyRpdDevNdrPhb_Type.__name__ = "Unsigned32"
_DocsRphyRpdDevNdrPhb_Object = MibTableColumn
docsRphyRpdDevNdrPhb = _DocsRphyRpdDevNdrPhb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 2, 1, 11),
    _DocsRphyRpdDevNdrPhb_Type()
)
docsRphyRpdDevNdrPhb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdrPhb.setStatus("current")
_DocsRphyRpdDevNdrPowerAdjust_Type = Integer32
_DocsRphyRpdDevNdrPowerAdjust_Object = MibTableColumn
docsRphyRpdDevNdrPowerAdjust = _DocsRphyRpdDevNdrPowerAdjust_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 2, 1, 12),
    _DocsRphyRpdDevNdrPowerAdjust_Type()
)
docsRphyRpdDevNdrPowerAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdrPowerAdjust.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdrPowerAdjust.setUnits("TenthdBmV")
_DocsRphyRpdDevNdrRpdStatus_Type = OctetString
_DocsRphyRpdDevNdrRpdStatus_Object = MibTableColumn
docsRphyRpdDevNdrRpdStatus = _DocsRphyRpdDevNdrRpdStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 2, 1, 13),
    _DocsRphyRpdDevNdrRpdStatus_Type()
)
docsRphyRpdDevNdrRpdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdrRpdStatus.setStatus("current")
_DocsRphyRpdDevNdrRpdInPktCount_Type = Counter64
_DocsRphyRpdDevNdrRpdInPktCount_Object = MibTableColumn
docsRphyRpdDevNdrRpdInPktCount = _DocsRphyRpdDevNdrRpdInPktCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 2, 1, 14),
    _DocsRphyRpdDevNdrRpdInPktCount_Type()
)
docsRphyRpdDevNdrRpdInPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdrRpdInPktCount.setStatus("current")
_DocsRphyRpdDevNdrRpdOutPktCount_Type = Counter64
_DocsRphyRpdDevNdrRpdOutPktCount_Object = MibTableColumn
docsRphyRpdDevNdrRpdOutPktCount = _DocsRphyRpdDevNdrRpdOutPktCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 1, 2, 1, 15),
    _DocsRphyRpdDevNdrRpdOutPktCount_Type()
)
docsRphyRpdDevNdrRpdOutPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyRpdDevNdrRpdOutPktCount.setStatus("current")
_RphyNdfNdrMIBConform_ObjectIdentity = ObjectIdentity
rphyNdfNdrMIBConform = _RphyNdfNdrMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 2)
)
_RphyNdfNdrMIBCompliances_ObjectIdentity = ObjectIdentity
rphyNdfNdrMIBCompliances = _RphyNdfNdrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 2, 1)
)
_RphyNdfNdrMIBGroups_ObjectIdentity = ObjectIdentity
rphyNdfNdrMIBGroups = _RphyNdfNdrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 2, 2)
)

# Managed Objects groups

rphyNdfNdrMIBMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 2, 2, 1)
)
rphyNdfNdrMIBMainObjectGroup.setObjects(
      *(("RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdfEnable"),
        ("RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdfDstIPAddr"),
        ("RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdfSrcIPAddr"),
        ("RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdfSessionId"),
        ("RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdfFrequency"),
        ("RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdfBandwidth"),
        ("RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdfPowerAdjust"),
        ("RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdfRfMute"),
        ("RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdfIsUnicast"),
        ("RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdfRpdStatus"),
        ("RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdfRpdInPktCount"),
        ("RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdfRpdOutPktCount"),
        ("RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdrEnable"),
        ("RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdrDstIPAddr"),
        ("RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdrSrcIPAddr"),
        ("RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdrSessionId"),
        ("RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdrFrequency"),
        ("RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdrBandwidth"),
        ("RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdrMtuSize"),
        ("RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdrPhb"),
        ("RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdrPowerAdjust"),
        ("RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdrRpdStatus"),
        ("RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdrRpdInPktCount"),
        ("RPHY-NDF-NDR-MIB", "docsRphyRpdDevNdrRpdOutPktCount"))
)
if mibBuilder.loadTexts:
    rphyNdfNdrMIBMainObjectGroup.setStatus("current")


# Notification objects

rphyNdfNdrMIBEventName = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 0, 1)
)
if mibBuilder.loadTexts:
    rphyNdfNdrMIBEventName.setStatus(
        "current"
    )


# Notifications groups

rphyNdfNdrMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 2, 2, 2)
)
rphyNdfNdrMIBNotificationGroup.setObjects(
    ("RPHY-NDF-NDR-MIB", "rphyNdfNdrMIBEventName")
)
if mibBuilder.loadTexts:
    rphyNdfNdrMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rphyNdfNdrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 857, 2, 1, 1)
)
rphyNdfNdrMIBCompliance.setObjects(
      *(("RPHY-NDF-NDR-MIB", "rphyNdfNdrMIBMainObjectGroup"),
        ("RPHY-NDF-NDR-MIB", "rphyNdfNdrMIBNotificationGroup"))
)
if mibBuilder.loadTexts:
    rphyNdfNdrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RPHY-NDF-NDR-MIB",
    **{"rphyNdfNdrMIB": rphyNdfNdrMIB,
       "rphyNdfNdrMIBNotifs": rphyNdfNdrMIBNotifs,
       "rphyNdfNdrMIBEventName": rphyNdfNdrMIBEventName,
       "rphyNdfNdrMIBObjects": rphyNdfNdrMIBObjects,
       "docsRphyRpdDevNdfCfgTable": docsRphyRpdDevNdfCfgTable,
       "docsRphyRpdDevNdfCfgEntry": docsRphyRpdDevNdfCfgEntry,
       "docsRphyRpdDevNdfUniqueId": docsRphyRpdDevNdfUniqueId,
       "docsRphyRpdDevNdfRfPort": docsRphyRpdDevNdfRfPort,
       "docsRphyRpdDevNdfRfChannel": docsRphyRpdDevNdfRfChannel,
       "docsRphyRpdDevNdfEnable": docsRphyRpdDevNdfEnable,
       "docsRphyRpdDevNdfDstIPAddr": docsRphyRpdDevNdfDstIPAddr,
       "docsRphyRpdDevNdfSrcIPAddr": docsRphyRpdDevNdfSrcIPAddr,
       "docsRphyRpdDevNdfSessionId": docsRphyRpdDevNdfSessionId,
       "docsRphyRpdDevNdfFrequency": docsRphyRpdDevNdfFrequency,
       "docsRphyRpdDevNdfBandwidth": docsRphyRpdDevNdfBandwidth,
       "docsRphyRpdDevNdfPowerAdjust": docsRphyRpdDevNdfPowerAdjust,
       "docsRphyRpdDevNdfRfMute": docsRphyRpdDevNdfRfMute,
       "docsRphyRpdDevNdfIsUnicast": docsRphyRpdDevNdfIsUnicast,
       "docsRphyRpdDevNdfRpdStatus": docsRphyRpdDevNdfRpdStatus,
       "docsRphyRpdDevNdfRpdInPktCount": docsRphyRpdDevNdfRpdInPktCount,
       "docsRphyRpdDevNdfRpdOutPktCount": docsRphyRpdDevNdfRpdOutPktCount,
       "docsRphyRpdDevNdrCfgTable": docsRphyRpdDevNdrCfgTable,
       "docsRphyRpdDevNdrCfgEntry": docsRphyRpdDevNdrCfgEntry,
       "docsRphyRpdDevNdrUniqueId": docsRphyRpdDevNdrUniqueId,
       "docsRphyRpdDevNdrRfPort": docsRphyRpdDevNdrRfPort,
       "docsRphyRpdDevNdrRfChannel": docsRphyRpdDevNdrRfChannel,
       "docsRphyRpdDevNdrEnable": docsRphyRpdDevNdrEnable,
       "docsRphyRpdDevNdrDstIPAddr": docsRphyRpdDevNdrDstIPAddr,
       "docsRphyRpdDevNdrSrcIPAddr": docsRphyRpdDevNdrSrcIPAddr,
       "docsRphyRpdDevNdrSessionId": docsRphyRpdDevNdrSessionId,
       "docsRphyRpdDevNdrFrequency": docsRphyRpdDevNdrFrequency,
       "docsRphyRpdDevNdrBandwidth": docsRphyRpdDevNdrBandwidth,
       "docsRphyRpdDevNdrMtuSize": docsRphyRpdDevNdrMtuSize,
       "docsRphyRpdDevNdrPhb": docsRphyRpdDevNdrPhb,
       "docsRphyRpdDevNdrPowerAdjust": docsRphyRpdDevNdrPowerAdjust,
       "docsRphyRpdDevNdrRpdStatus": docsRphyRpdDevNdrRpdStatus,
       "docsRphyRpdDevNdrRpdInPktCount": docsRphyRpdDevNdrRpdInPktCount,
       "docsRphyRpdDevNdrRpdOutPktCount": docsRphyRpdDevNdrRpdOutPktCount,
       "rphyNdfNdrMIBConform": rphyNdfNdrMIBConform,
       "rphyNdfNdrMIBCompliances": rphyNdfNdrMIBCompliances,
       "rphyNdfNdrMIBCompliance": rphyNdfNdrMIBCompliance,
       "rphyNdfNdrMIBGroups": rphyNdfNdrMIBGroups,
       "rphyNdfNdrMIBMainObjectGroup": rphyNdfNdrMIBMainObjectGroup,
       "rphyNdfNdrMIBNotificationGroup": rphyNdfNdrMIBNotificationGroup}
)
