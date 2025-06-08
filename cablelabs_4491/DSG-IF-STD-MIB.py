# SNMP MIB module (DSG-IF-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cablelabs_4491/DSG-IF-STD-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:41:18 2025
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

(clabProjDocsis,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjDocsis")

(docsDevEvId,
 docsDevEvLevel,
 docsDevEvText) = mibBuilder.importSymbols(
    "DOCS-CABLE-DEVICE-MIB",
    "docsDevEvId",
    "docsDevEvLevel",
    "docsDevEvText")

(docsIfCmCmtsAddress,
 docsIfCmStatusDocsisOperMode,
 docsIfCmStatusModulationType,
 docsIfDocsisBaseCapability) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "docsIfCmCmtsAddress",
    "docsIfCmStatusDocsisOperMode",
    "docsIfCmStatusModulationType",
    "docsIfDocsisBaseCapability")

(Dsid,) = mibBuilder.importSymbols(
    "DOCS-IF3-MIB",
    "Dsid")

(ifPhysAddress,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifPhysAddress")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

dsgIfStdMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4)
)
if mibBuilder.loadTexts:
    dsgIfStdMib.setRevisions(
        ("2009-05-29 00:00",
         "2008-06-26 00:00",
         "2007-02-23 00:00",
         "2006-07-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DsgIfStdNotifications_ObjectIdentity = ObjectIdentity
dsgIfStdNotifications = _DsgIfStdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 0)
)
_DsgIfStdMibObjects_ObjectIdentity = ObjectIdentity
dsgIfStdMibObjects = _DsgIfStdMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1)
)
_DsgIfStdConfig_ObjectIdentity = ObjectIdentity
dsgIfStdConfig = _DsgIfStdConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 1)
)


class _DsgIfStdDsgMode_Type(Integer32):
    """Custom type dsgIfStdDsgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("basic", 1),
          ("advanced", 2))
    )


_DsgIfStdDsgMode_Type.__name__ = "Integer32"
_DsgIfStdDsgMode_Object = MibScalar
dsgIfStdDsgMode = _DsgIfStdDsgMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 1, 1),
    _DsgIfStdDsgMode_Type()
)
dsgIfStdDsgMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfStdDsgMode.setStatus("current")


class _DsgIfStdTdsg1_Type(Unsigned32):
    """Custom type dsgIfStdTdsg1 based on Unsigned32"""
    defaultValue = 2


_DsgIfStdTdsg1_Type.__name__ = "Unsigned32"
_DsgIfStdTdsg1_Object = MibScalar
dsgIfStdTdsg1 = _DsgIfStdTdsg1_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 1, 2),
    _DsgIfStdTdsg1_Type()
)
dsgIfStdTdsg1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfStdTdsg1.setStatus("current")
if mibBuilder.loadTexts:
    dsgIfStdTdsg1.setUnits("seconds")


class _DsgIfStdTdsg2_Type(Unsigned32):
    """Custom type dsgIfStdTdsg2 based on Unsigned32"""
    defaultValue = 600


_DsgIfStdTdsg2_Type.__name__ = "Unsigned32"
_DsgIfStdTdsg2_Object = MibScalar
dsgIfStdTdsg2 = _DsgIfStdTdsg2_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 1, 3),
    _DsgIfStdTdsg2_Type()
)
dsgIfStdTdsg2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfStdTdsg2.setStatus("current")
if mibBuilder.loadTexts:
    dsgIfStdTdsg2.setUnits("seconds")


class _DsgIfStdTdsg3_Type(Unsigned32):
    """Custom type dsgIfStdTdsg3 based on Unsigned32"""
    defaultValue = 300


_DsgIfStdTdsg3_Type.__name__ = "Unsigned32"
_DsgIfStdTdsg3_Object = MibScalar
dsgIfStdTdsg3 = _DsgIfStdTdsg3_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 1, 4),
    _DsgIfStdTdsg3_Type()
)
dsgIfStdTdsg3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfStdTdsg3.setStatus("current")
if mibBuilder.loadTexts:
    dsgIfStdTdsg3.setUnits("seconds")


class _DsgIfStdTdsg4_Type(Unsigned32):
    """Custom type dsgIfStdTdsg4 based on Unsigned32"""
    defaultValue = 1800


_DsgIfStdTdsg4_Type.__name__ = "Unsigned32"
_DsgIfStdTdsg4_Object = MibScalar
dsgIfStdTdsg4 = _DsgIfStdTdsg4_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 1, 5),
    _DsgIfStdTdsg4_Type()
)
dsgIfStdTdsg4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfStdTdsg4.setStatus("current")
if mibBuilder.loadTexts:
    dsgIfStdTdsg4.setUnits("seconds")
_DsgIfStdTdsg1Timeouts_Type = Counter32
_DsgIfStdTdsg1Timeouts_Object = MibScalar
dsgIfStdTdsg1Timeouts = _DsgIfStdTdsg1Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 1, 6),
    _DsgIfStdTdsg1Timeouts_Type()
)
dsgIfStdTdsg1Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfStdTdsg1Timeouts.setStatus("current")
_DsgIfStdTdsg2Timeouts_Type = Counter32
_DsgIfStdTdsg2Timeouts_Object = MibScalar
dsgIfStdTdsg2Timeouts = _DsgIfStdTdsg2Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 1, 7),
    _DsgIfStdTdsg2Timeouts_Type()
)
dsgIfStdTdsg2Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfStdTdsg2Timeouts.setStatus("current")
_DsgIfStdTdsg3Timeouts_Type = Counter32
_DsgIfStdTdsg3Timeouts_Object = MibScalar
dsgIfStdTdsg3Timeouts = _DsgIfStdTdsg3Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 1, 8),
    _DsgIfStdTdsg3Timeouts_Type()
)
dsgIfStdTdsg3Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfStdTdsg3Timeouts.setStatus("current")
_DsgIfStdTdsg4Timeouts_Type = Counter32
_DsgIfStdTdsg4Timeouts_Object = MibScalar
dsgIfStdTdsg4Timeouts = _DsgIfStdTdsg4Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 1, 9),
    _DsgIfStdTdsg4Timeouts_Type()
)
dsgIfStdTdsg4Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfStdTdsg4Timeouts.setStatus("current")
_DsgIfStdTunnelFilter_ObjectIdentity = ObjectIdentity
dsgIfStdTunnelFilter = _DsgIfStdTunnelFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 2)
)
_DsgIfStdTunnelFilterTable_Object = MibTable
dsgIfStdTunnelFilterTable = _DsgIfStdTunnelFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dsgIfStdTunnelFilterTable.setStatus("current")
_DsgIfStdTunnelFilterEntry_Object = MibTableRow
dsgIfStdTunnelFilterEntry = _DsgIfStdTunnelFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 2, 1, 1)
)
dsgIfStdTunnelFilterEntry.setIndexNames(
    (0, "DSG-IF-STD-MIB", "dsgIfStdTunnelFilterIndex"),
)
if mibBuilder.loadTexts:
    dsgIfStdTunnelFilterEntry.setStatus("current")
_DsgIfStdTunnelFilterIndex_Type = Unsigned32
_DsgIfStdTunnelFilterIndex_Object = MibTableColumn
dsgIfStdTunnelFilterIndex = _DsgIfStdTunnelFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 2, 1, 1, 1),
    _DsgIfStdTunnelFilterIndex_Type()
)
dsgIfStdTunnelFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsgIfStdTunnelFilterIndex.setStatus("current")


class _DsgIfStdTunnelFilterApplicationId_Type(Integer32):
    """Custom type dsgIfStdTunnelFilterApplicationId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_DsgIfStdTunnelFilterApplicationId_Type.__name__ = "Integer32"
_DsgIfStdTunnelFilterApplicationId_Object = MibTableColumn
dsgIfStdTunnelFilterApplicationId = _DsgIfStdTunnelFilterApplicationId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 2, 1, 1, 2),
    _DsgIfStdTunnelFilterApplicationId_Type()
)
dsgIfStdTunnelFilterApplicationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfStdTunnelFilterApplicationId.setStatus("deprecated")
_DsgIfStdTunnelFilterMacAddress_Type = MacAddress
_DsgIfStdTunnelFilterMacAddress_Object = MibTableColumn
dsgIfStdTunnelFilterMacAddress = _DsgIfStdTunnelFilterMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 2, 1, 1, 3),
    _DsgIfStdTunnelFilterMacAddress_Type()
)
dsgIfStdTunnelFilterMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfStdTunnelFilterMacAddress.setStatus("current")
_DsgIfStdTunnelFilterIpAddressType_Type = InetAddressType
_DsgIfStdTunnelFilterIpAddressType_Object = MibTableColumn
dsgIfStdTunnelFilterIpAddressType = _DsgIfStdTunnelFilterIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 2, 1, 1, 4),
    _DsgIfStdTunnelFilterIpAddressType_Type()
)
dsgIfStdTunnelFilterIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfStdTunnelFilterIpAddressType.setStatus("current")


class _DsgIfStdTunnelFilterSrcIpAddr_Type(InetAddress):
    """Custom type dsgIfStdTunnelFilterSrcIpAddr based on InetAddress"""
    defaultHexValue = "00000000"


_DsgIfStdTunnelFilterSrcIpAddr_Type.__name__ = "InetAddress"
_DsgIfStdTunnelFilterSrcIpAddr_Object = MibTableColumn
dsgIfStdTunnelFilterSrcIpAddr = _DsgIfStdTunnelFilterSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 2, 1, 1, 5),
    _DsgIfStdTunnelFilterSrcIpAddr_Type()
)
dsgIfStdTunnelFilterSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfStdTunnelFilterSrcIpAddr.setStatus("current")


class _DsgIfStdTunnelFilterSrcIpMask_Type(InetAddress):
    """Custom type dsgIfStdTunnelFilterSrcIpMask based on InetAddress"""
    defaultHexValue = "FFFFFFFF"


_DsgIfStdTunnelFilterSrcIpMask_Type.__name__ = "InetAddress"
_DsgIfStdTunnelFilterSrcIpMask_Object = MibTableColumn
dsgIfStdTunnelFilterSrcIpMask = _DsgIfStdTunnelFilterSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 2, 1, 1, 6),
    _DsgIfStdTunnelFilterSrcIpMask_Type()
)
dsgIfStdTunnelFilterSrcIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfStdTunnelFilterSrcIpMask.setStatus("current")


class _DsgIfStdTunnelFilterDestIpAddr_Type(InetAddress):
    """Custom type dsgIfStdTunnelFilterDestIpAddr based on InetAddress"""
    defaultHexValue = "00000000"


_DsgIfStdTunnelFilterDestIpAddr_Type.__name__ = "InetAddress"
_DsgIfStdTunnelFilterDestIpAddr_Object = MibTableColumn
dsgIfStdTunnelFilterDestIpAddr = _DsgIfStdTunnelFilterDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 2, 1, 1, 7),
    _DsgIfStdTunnelFilterDestIpAddr_Type()
)
dsgIfStdTunnelFilterDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfStdTunnelFilterDestIpAddr.setStatus("current")


class _DsgIfStdTunnelFilterDestPortStart_Type(InetPortNumber):
    """Custom type dsgIfStdTunnelFilterDestPortStart based on InetPortNumber"""
    defaultValue = 0


_DsgIfStdTunnelFilterDestPortStart_Type.__name__ = "InetPortNumber"
_DsgIfStdTunnelFilterDestPortStart_Object = MibTableColumn
dsgIfStdTunnelFilterDestPortStart = _DsgIfStdTunnelFilterDestPortStart_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 2, 1, 1, 8),
    _DsgIfStdTunnelFilterDestPortStart_Type()
)
dsgIfStdTunnelFilterDestPortStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfStdTunnelFilterDestPortStart.setStatus("current")


class _DsgIfStdTunnelFilterDestPortEnd_Type(InetPortNumber):
    """Custom type dsgIfStdTunnelFilterDestPortEnd based on InetPortNumber"""
    defaultValue = 65535


_DsgIfStdTunnelFilterDestPortEnd_Type.__name__ = "InetPortNumber"
_DsgIfStdTunnelFilterDestPortEnd_Object = MibTableColumn
dsgIfStdTunnelFilterDestPortEnd = _DsgIfStdTunnelFilterDestPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 2, 1, 1, 9),
    _DsgIfStdTunnelFilterDestPortEnd_Type()
)
dsgIfStdTunnelFilterDestPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfStdTunnelFilterDestPortEnd.setStatus("current")
_DsgIfStdTunnelFilterPkts_Type = Counter32
_DsgIfStdTunnelFilterPkts_Object = MibTableColumn
dsgIfStdTunnelFilterPkts = _DsgIfStdTunnelFilterPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 2, 1, 1, 10),
    _DsgIfStdTunnelFilterPkts_Type()
)
dsgIfStdTunnelFilterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfStdTunnelFilterPkts.setStatus("current")
if mibBuilder.loadTexts:
    dsgIfStdTunnelFilterPkts.setUnits("packets")
_DsgIfStdTunnelFilterOctets_Type = Counter32
_DsgIfStdTunnelFilterOctets_Object = MibTableColumn
dsgIfStdTunnelFilterOctets = _DsgIfStdTunnelFilterOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 2, 1, 1, 11),
    _DsgIfStdTunnelFilterOctets_Type()
)
dsgIfStdTunnelFilterOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfStdTunnelFilterOctets.setStatus("current")
if mibBuilder.loadTexts:
    dsgIfStdTunnelFilterOctets.setUnits("octets")
_DsgIfStdTunnelFilterTimeActive_Type = Counter32
_DsgIfStdTunnelFilterTimeActive_Object = MibTableColumn
dsgIfStdTunnelFilterTimeActive = _DsgIfStdTunnelFilterTimeActive_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 2, 1, 1, 12),
    _DsgIfStdTunnelFilterTimeActive_Type()
)
dsgIfStdTunnelFilterTimeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfStdTunnelFilterTimeActive.setStatus("current")
if mibBuilder.loadTexts:
    dsgIfStdTunnelFilterTimeActive.setUnits("seconds")


class _DsgIfStdTunnelFilterTunnelId_Type(Unsigned32):
    """Custom type dsgIfStdTunnelFilterTunnelId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_DsgIfStdTunnelFilterTunnelId_Type.__name__ = "Unsigned32"
_DsgIfStdTunnelFilterTunnelId_Object = MibTableColumn
dsgIfStdTunnelFilterTunnelId = _DsgIfStdTunnelFilterTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 2, 1, 1, 13),
    _DsgIfStdTunnelFilterTunnelId_Type()
)
dsgIfStdTunnelFilterTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfStdTunnelFilterTunnelId.setStatus("current")
_DsgIfStdTunnelFilterDsid_Type = Dsid
_DsgIfStdTunnelFilterDsid_Object = MibTableColumn
dsgIfStdTunnelFilterDsid = _DsgIfStdTunnelFilterDsid_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 2, 1, 1, 14),
    _DsgIfStdTunnelFilterDsid_Type()
)
dsgIfStdTunnelFilterDsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfStdTunnelFilterDsid.setStatus("current")


class _DsgIfStdTunnelFilterClientIdType_Type(Integer32):
    """Custom type dsgIfStdTunnelFilterClientIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cableCard", 0),
          ("broadcast", 1),
          ("macAddress", 2),
          ("caSystemId", 3),
          ("applicationId", 4))
    )


_DsgIfStdTunnelFilterClientIdType_Type.__name__ = "Integer32"
_DsgIfStdTunnelFilterClientIdType_Object = MibTableColumn
dsgIfStdTunnelFilterClientIdType = _DsgIfStdTunnelFilterClientIdType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 2, 1, 1, 15),
    _DsgIfStdTunnelFilterClientIdType_Type()
)
dsgIfStdTunnelFilterClientIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfStdTunnelFilterClientIdType.setStatus("current")


class _DsgIfStdTunnelFilterClientIdValue_Type(OctetString):
    """Custom type dsgIfStdTunnelFilterClientIdValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 6),
    )


_DsgIfStdTunnelFilterClientIdValue_Type.__name__ = "OctetString"
_DsgIfStdTunnelFilterClientIdValue_Object = MibTableColumn
dsgIfStdTunnelFilterClientIdValue = _DsgIfStdTunnelFilterClientIdValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 2, 1, 1, 16),
    _DsgIfStdTunnelFilterClientIdValue_Type()
)
dsgIfStdTunnelFilterClientIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfStdTunnelFilterClientIdValue.setStatus("current")
_DsgIfStdDsgChannelList_ObjectIdentity = ObjectIdentity
dsgIfStdDsgChannelList = _DsgIfStdDsgChannelList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 3)
)
_DsgIfStdDsgChannelListTable_Object = MibTable
dsgIfStdDsgChannelListTable = _DsgIfStdDsgChannelListTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dsgIfStdDsgChannelListTable.setStatus("current")
_DsgIfStdDsgChannelListEntry_Object = MibTableRow
dsgIfStdDsgChannelListEntry = _DsgIfStdDsgChannelListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 3, 1, 1)
)
dsgIfStdDsgChannelListEntry.setIndexNames(
    (0, "DSG-IF-STD-MIB", "dsgIfStdDsgChannelListIndex"),
)
if mibBuilder.loadTexts:
    dsgIfStdDsgChannelListEntry.setStatus("current")
_DsgIfStdDsgChannelListIndex_Type = Unsigned32
_DsgIfStdDsgChannelListIndex_Object = MibTableColumn
dsgIfStdDsgChannelListIndex = _DsgIfStdDsgChannelListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 3, 1, 1, 1),
    _DsgIfStdDsgChannelListIndex_Type()
)
dsgIfStdDsgChannelListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsgIfStdDsgChannelListIndex.setStatus("current")
_DsgIfStdDsgChannelListFrequency_Type = Unsigned32
_DsgIfStdDsgChannelListFrequency_Object = MibTableColumn
dsgIfStdDsgChannelListFrequency = _DsgIfStdDsgChannelListFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 1, 3, 1, 1, 2),
    _DsgIfStdDsgChannelListFrequency_Type()
)
dsgIfStdDsgChannelListFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfStdDsgChannelListFrequency.setStatus("current")
if mibBuilder.loadTexts:
    dsgIfStdDsgChannelListFrequency.setUnits("Hertz")
_DsgIfStdConformance_ObjectIdentity = ObjectIdentity
dsgIfStdConformance = _DsgIfStdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 2)
)
_DsgIfStdCompliances_ObjectIdentity = ObjectIdentity
dsgIfStdCompliances = _DsgIfStdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 2, 1)
)
_DsgIfStdGroups_ObjectIdentity = ObjectIdentity
dsgIfStdGroups = _DsgIfStdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 2, 2)
)

# Managed Objects groups

dsgIfStdConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 2, 2, 1)
)
dsgIfStdConfigGroup.setObjects(
      *(("DSG-IF-STD-MIB", "dsgIfStdDsgMode"),
        ("DSG-IF-STD-MIB", "dsgIfStdTdsg1"),
        ("DSG-IF-STD-MIB", "dsgIfStdTdsg2"),
        ("DSG-IF-STD-MIB", "dsgIfStdTdsg3"),
        ("DSG-IF-STD-MIB", "dsgIfStdTdsg4"),
        ("DSG-IF-STD-MIB", "dsgIfStdTdsg1Timeouts"),
        ("DSG-IF-STD-MIB", "dsgIfStdTdsg2Timeouts"),
        ("DSG-IF-STD-MIB", "dsgIfStdTdsg3Timeouts"),
        ("DSG-IF-STD-MIB", "dsgIfStdTdsg4Timeouts"),
        ("DSG-IF-STD-MIB", "dsgIfStdTunnelFilterMacAddress"),
        ("DSG-IF-STD-MIB", "dsgIfStdTunnelFilterIpAddressType"),
        ("DSG-IF-STD-MIB", "dsgIfStdTunnelFilterSrcIpAddr"),
        ("DSG-IF-STD-MIB", "dsgIfStdTunnelFilterSrcIpMask"),
        ("DSG-IF-STD-MIB", "dsgIfStdTunnelFilterDestIpAddr"),
        ("DSG-IF-STD-MIB", "dsgIfStdTunnelFilterDestPortStart"),
        ("DSG-IF-STD-MIB", "dsgIfStdTunnelFilterDestPortEnd"),
        ("DSG-IF-STD-MIB", "dsgIfStdTunnelFilterPkts"),
        ("DSG-IF-STD-MIB", "dsgIfStdTunnelFilterOctets"),
        ("DSG-IF-STD-MIB", "dsgIfStdTunnelFilterTimeActive"),
        ("DSG-IF-STD-MIB", "dsgIfStdTunnelFilterTunnelId"),
        ("DSG-IF-STD-MIB", "dsgIfStdTunnelFilterDsid"),
        ("DSG-IF-STD-MIB", "dsgIfStdTunnelFilterClientIdType"),
        ("DSG-IF-STD-MIB", "dsgIfStdTunnelFilterClientIdValue"),
        ("DSG-IF-STD-MIB", "dsgIfStdDsgChannelListFrequency"))
)
if mibBuilder.loadTexts:
    dsgIfStdConfigGroup.setStatus("current")


# Notification objects

dsgIfStdUpstreamEnabledNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 0, 1)
)
dsgIfStdUpstreamEnabledNotify.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"),
        ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    dsgIfStdUpstreamEnabledNotify.setStatus(
        "current"
    )

dsgIfStdUpstreamDisabledNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 0, 2)
)
dsgIfStdUpstreamDisabledNotify.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"),
        ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    dsgIfStdUpstreamDisabledNotify.setStatus(
        "current"
    )

dsgIfStdTdsg2TimeoutNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 0, 3)
)
dsgIfStdTdsg2TimeoutNotify.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("IF-MIB", "ifPhysAddress"),
        ("DOCS-IF-MIB", "docsIfCmCmtsAddress"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("DOCS-IF-MIB", "docsIfCmStatusDocsisOperMode"),
        ("DOCS-IF-MIB", "docsIfCmStatusModulationType"))
)
if mibBuilder.loadTexts:
    dsgIfStdTdsg2TimeoutNotify.setStatus(
        "current"
    )


# Notifications groups

dsgIfStdNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 2, 2, 2)
)
dsgIfStdNotifyGroup.setObjects(
      *(("DSG-IF-STD-MIB", "dsgIfStdUpstreamEnabledNotify"),
        ("DSG-IF-STD-MIB", "dsgIfStdUpstreamDisabledNotify"),
        ("DSG-IF-STD-MIB", "dsgIfStdTdsg2TimeoutNotify"))
)
if mibBuilder.loadTexts:
    dsgIfStdNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dsgIfStdBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 4, 2, 1, 1)
)
dsgIfStdBasicCompliance.setObjects(
      *(("DSG-IF-STD-MIB", "dsgIfStdConfigGroup"),
        ("DSG-IF-STD-MIB", "dsgIfStdNotifyGroup"))
)
if mibBuilder.loadTexts:
    dsgIfStdBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DSG-IF-STD-MIB",
    **{"dsgIfStdMib": dsgIfStdMib,
       "dsgIfStdNotifications": dsgIfStdNotifications,
       "dsgIfStdUpstreamEnabledNotify": dsgIfStdUpstreamEnabledNotify,
       "dsgIfStdUpstreamDisabledNotify": dsgIfStdUpstreamDisabledNotify,
       "dsgIfStdTdsg2TimeoutNotify": dsgIfStdTdsg2TimeoutNotify,
       "dsgIfStdMibObjects": dsgIfStdMibObjects,
       "dsgIfStdConfig": dsgIfStdConfig,
       "dsgIfStdDsgMode": dsgIfStdDsgMode,
       "dsgIfStdTdsg1": dsgIfStdTdsg1,
       "dsgIfStdTdsg2": dsgIfStdTdsg2,
       "dsgIfStdTdsg3": dsgIfStdTdsg3,
       "dsgIfStdTdsg4": dsgIfStdTdsg4,
       "dsgIfStdTdsg1Timeouts": dsgIfStdTdsg1Timeouts,
       "dsgIfStdTdsg2Timeouts": dsgIfStdTdsg2Timeouts,
       "dsgIfStdTdsg3Timeouts": dsgIfStdTdsg3Timeouts,
       "dsgIfStdTdsg4Timeouts": dsgIfStdTdsg4Timeouts,
       "dsgIfStdTunnelFilter": dsgIfStdTunnelFilter,
       "dsgIfStdTunnelFilterTable": dsgIfStdTunnelFilterTable,
       "dsgIfStdTunnelFilterEntry": dsgIfStdTunnelFilterEntry,
       "dsgIfStdTunnelFilterIndex": dsgIfStdTunnelFilterIndex,
       "dsgIfStdTunnelFilterApplicationId": dsgIfStdTunnelFilterApplicationId,
       "dsgIfStdTunnelFilterMacAddress": dsgIfStdTunnelFilterMacAddress,
       "dsgIfStdTunnelFilterIpAddressType": dsgIfStdTunnelFilterIpAddressType,
       "dsgIfStdTunnelFilterSrcIpAddr": dsgIfStdTunnelFilterSrcIpAddr,
       "dsgIfStdTunnelFilterSrcIpMask": dsgIfStdTunnelFilterSrcIpMask,
       "dsgIfStdTunnelFilterDestIpAddr": dsgIfStdTunnelFilterDestIpAddr,
       "dsgIfStdTunnelFilterDestPortStart": dsgIfStdTunnelFilterDestPortStart,
       "dsgIfStdTunnelFilterDestPortEnd": dsgIfStdTunnelFilterDestPortEnd,
       "dsgIfStdTunnelFilterPkts": dsgIfStdTunnelFilterPkts,
       "dsgIfStdTunnelFilterOctets": dsgIfStdTunnelFilterOctets,
       "dsgIfStdTunnelFilterTimeActive": dsgIfStdTunnelFilterTimeActive,
       "dsgIfStdTunnelFilterTunnelId": dsgIfStdTunnelFilterTunnelId,
       "dsgIfStdTunnelFilterDsid": dsgIfStdTunnelFilterDsid,
       "dsgIfStdTunnelFilterClientIdType": dsgIfStdTunnelFilterClientIdType,
       "dsgIfStdTunnelFilterClientIdValue": dsgIfStdTunnelFilterClientIdValue,
       "dsgIfStdDsgChannelList": dsgIfStdDsgChannelList,
       "dsgIfStdDsgChannelListTable": dsgIfStdDsgChannelListTable,
       "dsgIfStdDsgChannelListEntry": dsgIfStdDsgChannelListEntry,
       "dsgIfStdDsgChannelListIndex": dsgIfStdDsgChannelListIndex,
       "dsgIfStdDsgChannelListFrequency": dsgIfStdDsgChannelListFrequency,
       "dsgIfStdConformance": dsgIfStdConformance,
       "dsgIfStdCompliances": dsgIfStdCompliances,
       "dsgIfStdBasicCompliance": dsgIfStdBasicCompliance,
       "dsgIfStdGroups": dsgIfStdGroups,
       "dsgIfStdConfigGroup": dsgIfStdConfigGroup,
       "dsgIfStdNotifyGroup": dsgIfStdNotifyGroup}
)
