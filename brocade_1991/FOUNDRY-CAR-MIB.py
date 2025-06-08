# SNMP MIB module (FOUNDRY-CAR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/brocade_1991/FOUNDRY-CAR-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:18:53 2025
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

(snSwitch,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "snSwitch")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

snCAR = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16)
)
if mibBuilder.loadTexts:
    snCAR.setRevisions(
        ("2010-06-02 00:00",
         "2009-09-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PacketSource(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("input", 0),
          ("output", 1))
    )



class RateLimitType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("standardAcc", 1),
          ("quickAcc", 2),
          ("all", 3))
    )



class RateLimitAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("continue", 1),
          ("drop", 2),
          ("precedCont", 3),
          ("precedXmit", 4),
          ("xmit", 5))
    )



class BUMPacketType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknownunicast", 1),
          ("multicast", 2),
          ("unknownunicastmulticast", 3),
          ("broadcast", 4),
          ("broadcastunknownunicast", 5),
          ("broadcastmulticast", 6),
          ("broadcastunknownunicastmulticast", 7))
    )



# MIB Managed Objects in the order of their OIDs

_SnPortCARs_ObjectIdentity = ObjectIdentity
snPortCARs = _SnPortCARs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1)
)
_SnPortCARTable_Object = MibTable
snPortCARTable = _SnPortCARTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1)
)
if mibBuilder.loadTexts:
    snPortCARTable.setStatus("current")
_SnPortCAREntry_Object = MibTableRow
snPortCAREntry = _SnPortCAREntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1)
)
snPortCAREntry.setIndexNames(
    (0, "FOUNDRY-CAR-MIB", "snPortCARifIndex"),
    (0, "FOUNDRY-CAR-MIB", "snPortCARDirection"),
    (0, "FOUNDRY-CAR-MIB", "snPortCARRowIndex"),
)
if mibBuilder.loadTexts:
    snPortCAREntry.setStatus("current")
_SnPortCARifIndex_Type = InterfaceIndex
_SnPortCARifIndex_Object = MibTableColumn
snPortCARifIndex = _SnPortCARifIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 1),
    _SnPortCARifIndex_Type()
)
snPortCARifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARifIndex.setStatus("current")
_SnPortCARDirection_Type = PacketSource
_SnPortCARDirection_Object = MibTableColumn
snPortCARDirection = _SnPortCARDirection_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 2),
    _SnPortCARDirection_Type()
)
snPortCARDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARDirection.setStatus("current")


class _SnPortCARRowIndex_Type(Integer32):
    """Custom type snPortCARRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SnPortCARRowIndex_Type.__name__ = "Integer32"
_SnPortCARRowIndex_Object = MibTableColumn
snPortCARRowIndex = _SnPortCARRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 3),
    _SnPortCARRowIndex_Type()
)
snPortCARRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARRowIndex.setStatus("current")
_SnPortCARType_Type = RateLimitType
_SnPortCARType_Object = MibTableColumn
snPortCARType = _SnPortCARType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 4),
    _SnPortCARType_Type()
)
snPortCARType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARType.setStatus("current")
_SnPortCARAccIdx_Type = Integer32
_SnPortCARAccIdx_Object = MibTableColumn
snPortCARAccIdx = _SnPortCARAccIdx_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 5),
    _SnPortCARAccIdx_Type()
)
snPortCARAccIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARAccIdx.setStatus("current")
_SnPortCARRate_Type = Integer32
_SnPortCARRate_Object = MibTableColumn
snPortCARRate = _SnPortCARRate_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 6),
    _SnPortCARRate_Type()
)
snPortCARRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARRate.setStatus("current")
_SnPortCARLimit_Type = Integer32
_SnPortCARLimit_Object = MibTableColumn
snPortCARLimit = _SnPortCARLimit_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 7),
    _SnPortCARLimit_Type()
)
snPortCARLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARLimit.setStatus("current")
_SnPortCARExtLimit_Type = Integer32
_SnPortCARExtLimit_Object = MibTableColumn
snPortCARExtLimit = _SnPortCARExtLimit_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 8),
    _SnPortCARExtLimit_Type()
)
snPortCARExtLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARExtLimit.setStatus("current")
_SnPortCARConformAction_Type = RateLimitAction
_SnPortCARConformAction_Object = MibTableColumn
snPortCARConformAction = _SnPortCARConformAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 9),
    _SnPortCARConformAction_Type()
)
snPortCARConformAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARConformAction.setStatus("current")
_SnPortCARExceedAction_Type = RateLimitAction
_SnPortCARExceedAction_Object = MibTableColumn
snPortCARExceedAction = _SnPortCARExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 10),
    _SnPortCARExceedAction_Type()
)
snPortCARExceedAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARExceedAction.setStatus("current")
_SnPortCARStatSwitchedPkts_Type = Counter64
_SnPortCARStatSwitchedPkts_Object = MibTableColumn
snPortCARStatSwitchedPkts = _SnPortCARStatSwitchedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 11),
    _SnPortCARStatSwitchedPkts_Type()
)
snPortCARStatSwitchedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARStatSwitchedPkts.setStatus("current")
_SnPortCARStatSwitchedBytes_Type = Counter64
_SnPortCARStatSwitchedBytes_Object = MibTableColumn
snPortCARStatSwitchedBytes = _SnPortCARStatSwitchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 12),
    _SnPortCARStatSwitchedBytes_Type()
)
snPortCARStatSwitchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARStatSwitchedBytes.setStatus("current")
_SnPortCARStatFilteredPkts_Type = Counter64
_SnPortCARStatFilteredPkts_Object = MibTableColumn
snPortCARStatFilteredPkts = _SnPortCARStatFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 13),
    _SnPortCARStatFilteredPkts_Type()
)
snPortCARStatFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARStatFilteredPkts.setStatus("current")
_SnPortCARStatFilteredBytes_Type = Counter64
_SnPortCARStatFilteredBytes_Object = MibTableColumn
snPortCARStatFilteredBytes = _SnPortCARStatFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 14),
    _SnPortCARStatFilteredBytes_Type()
)
snPortCARStatFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARStatFilteredBytes.setStatus("current")
_SnPortCARStatCurBurst_Type = Gauge32
_SnPortCARStatCurBurst_Object = MibTableColumn
snPortCARStatCurBurst = _SnPortCARStatCurBurst_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 15),
    _SnPortCARStatCurBurst_Type()
)
snPortCARStatCurBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortCARStatCurBurst.setStatus("current")
_AgRateLimitCounterTable_Object = MibTable
agRateLimitCounterTable = _AgRateLimitCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 2)
)
if mibBuilder.loadTexts:
    agRateLimitCounterTable.setStatus("current")
_AgRateLimitCounterEntry_Object = MibTableRow
agRateLimitCounterEntry = _AgRateLimitCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 2, 1)
)
agRateLimitCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FOUNDRY-CAR-MIB", "snPortCARRowIndex"),
)
if mibBuilder.loadTexts:
    agRateLimitCounterEntry.setStatus("current")
_AgRateLimitCounterFwdedOctets_Type = Counter64
_AgRateLimitCounterFwdedOctets_Object = MibTableColumn
agRateLimitCounterFwdedOctets = _AgRateLimitCounterFwdedOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 2, 1, 1),
    _AgRateLimitCounterFwdedOctets_Type()
)
agRateLimitCounterFwdedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agRateLimitCounterFwdedOctets.setStatus("current")
_AgRateLimitCounterDroppedOctets_Type = Counter64
_AgRateLimitCounterDroppedOctets_Object = MibTableColumn
agRateLimitCounterDroppedOctets = _AgRateLimitCounterDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 2, 1, 2),
    _AgRateLimitCounterDroppedOctets_Type()
)
agRateLimitCounterDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agRateLimitCounterDroppedOctets.setStatus("current")
_AgRateLimitCounterReMarkedOctets_Type = Counter64
_AgRateLimitCounterReMarkedOctets_Object = MibTableColumn
agRateLimitCounterReMarkedOctets = _AgRateLimitCounterReMarkedOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 2, 1, 3),
    _AgRateLimitCounterReMarkedOctets_Type()
)
agRateLimitCounterReMarkedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agRateLimitCounterReMarkedOctets.setStatus("current")
_AgRateLimitCounterTotalOctets_Type = Counter64
_AgRateLimitCounterTotalOctets_Object = MibTableColumn
agRateLimitCounterTotalOctets = _AgRateLimitCounterTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 2, 1, 4),
    _AgRateLimitCounterTotalOctets_Type()
)
agRateLimitCounterTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agRateLimitCounterTotalOctets.setStatus("current")
_AgRateLimitCounterIndexTable_Object = MibTable
agRateLimitCounterIndexTable = _AgRateLimitCounterIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 3)
)
if mibBuilder.loadTexts:
    agRateLimitCounterIndexTable.setStatus("current")
_AgRateLimitCounterIndexEntry_Object = MibTableRow
agRateLimitCounterIndexEntry = _AgRateLimitCounterIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 3, 1)
)
agRateLimitCounterIndexEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FOUNDRY-CAR-MIB", "snPortCARRowIndex"),
)
if mibBuilder.loadTexts:
    agRateLimitCounterIndexEntry.setStatus("current")


class _AgRateLimitCounterIndexRowIndex_Type(Integer32):
    """Custom type agRateLimitCounterIndexRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AgRateLimitCounterIndexRowIndex_Type.__name__ = "Integer32"
_AgRateLimitCounterIndexRowIndex_Object = MibTableColumn
agRateLimitCounterIndexRowIndex = _AgRateLimitCounterIndexRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 3, 1, 1),
    _AgRateLimitCounterIndexRowIndex_Type()
)
agRateLimitCounterIndexRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agRateLimitCounterIndexRowIndex.setStatus("current")
_AgRateLimitCounterIndexDirection_Type = PacketSource
_AgRateLimitCounterIndexDirection_Object = MibTableColumn
agRateLimitCounterIndexDirection = _AgRateLimitCounterIndexDirection_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 3, 1, 2),
    _AgRateLimitCounterIndexDirection_Type()
)
agRateLimitCounterIndexDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agRateLimitCounterIndexDirection.setStatus("current")
_AgRateLimitCounterIndexACLID_Type = Integer32
_AgRateLimitCounterIndexACLID_Object = MibTableColumn
agRateLimitCounterIndexACLID = _AgRateLimitCounterIndexACLID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 3, 1, 3),
    _AgRateLimitCounterIndexACLID_Type()
)
agRateLimitCounterIndexACLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agRateLimitCounterIndexACLID.setStatus("current")
_AgRateLimitCounterIndexVLANID_Type = Integer32
_AgRateLimitCounterIndexVLANID_Object = MibTableColumn
agRateLimitCounterIndexVLANID = _AgRateLimitCounterIndexVLANID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 3, 1, 4),
    _AgRateLimitCounterIndexVLANID_Type()
)
agRateLimitCounterIndexVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agRateLimitCounterIndexVLANID.setStatus("current")
_AgRateLimitCounterIndexVLANGroupID_Type = Integer32
_AgRateLimitCounterIndexVLANGroupID_Object = MibTableColumn
agRateLimitCounterIndexVLANGroupID = _AgRateLimitCounterIndexVLANGroupID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 3, 1, 5),
    _AgRateLimitCounterIndexVLANGroupID_Type()
)
agRateLimitCounterIndexVLANGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agRateLimitCounterIndexVLANGroupID.setStatus("current")


class _AgRateLimitCounterIndexMACAddress_Type(MacAddress):
    """Custom type agRateLimitCounterIndexMACAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_AgRateLimitCounterIndexMACAddress_Type.__name__ = "MacAddress"
_AgRateLimitCounterIndexMACAddress_Object = MibTableColumn
agRateLimitCounterIndexMACAddress = _AgRateLimitCounterIndexMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 3, 1, 6),
    _AgRateLimitCounterIndexMACAddress_Type()
)
agRateLimitCounterIndexMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agRateLimitCounterIndexMACAddress.setStatus("current")
_AgRateLimitBUMCounterTable_Object = MibTable
agRateLimitBUMCounterTable = _AgRateLimitBUMCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 4)
)
if mibBuilder.loadTexts:
    agRateLimitBUMCounterTable.setStatus("current")
_AgRateLimitBUMCounterEntry_Object = MibTableRow
agRateLimitBUMCounterEntry = _AgRateLimitBUMCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 4, 1)
)
agRateLimitBUMCounterEntry.setIndexNames(
    (0, "FOUNDRY-CAR-MIB", "agRateLimitBUMCounterIfindex"),
    (0, "FOUNDRY-CAR-MIB", "agRateLimitBUMCounterVLANID"),
    (0, "FOUNDRY-CAR-MIB", "agRateLimitBUMCounterPacketType"),
)
if mibBuilder.loadTexts:
    agRateLimitBUMCounterEntry.setStatus("current")
_AgRateLimitBUMCounterIfindex_Type = InterfaceIndex
_AgRateLimitBUMCounterIfindex_Object = MibTableColumn
agRateLimitBUMCounterIfindex = _AgRateLimitBUMCounterIfindex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 4, 1, 1),
    _AgRateLimitBUMCounterIfindex_Type()
)
agRateLimitBUMCounterIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agRateLimitBUMCounterIfindex.setStatus("current")
_AgRateLimitBUMCounterVLANID_Type = Integer32
_AgRateLimitBUMCounterVLANID_Object = MibTableColumn
agRateLimitBUMCounterVLANID = _AgRateLimitBUMCounterVLANID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 4, 1, 2),
    _AgRateLimitBUMCounterVLANID_Type()
)
agRateLimitBUMCounterVLANID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agRateLimitBUMCounterVLANID.setStatus("current")
_AgRateLimitBUMCounterPacketType_Type = BUMPacketType
_AgRateLimitBUMCounterPacketType_Object = MibTableColumn
agRateLimitBUMCounterPacketType = _AgRateLimitBUMCounterPacketType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 4, 1, 3),
    _AgRateLimitBUMCounterPacketType_Type()
)
agRateLimitBUMCounterPacketType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agRateLimitBUMCounterPacketType.setStatus("current")
_AgRateLimitBUMCounterDroppedOctets_Type = Counter64
_AgRateLimitBUMCounterDroppedOctets_Object = MibTableColumn
agRateLimitBUMCounterDroppedOctets = _AgRateLimitBUMCounterDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 4, 1, 4),
    _AgRateLimitBUMCounterDroppedOctets_Type()
)
agRateLimitBUMCounterDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agRateLimitBUMCounterDroppedOctets.setStatus("current")
_AgRateLimitBUMCounterCBS_Type = Counter64
_AgRateLimitBUMCounterCBS_Object = MibTableColumn
agRateLimitBUMCounterCBS = _AgRateLimitBUMCounterCBS_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 4, 1, 5),
    _AgRateLimitBUMCounterCBS_Type()
)
agRateLimitBUMCounterCBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agRateLimitBUMCounterCBS.setStatus("current")
_AgRateLimitBUMCounterCIR_Type = Counter64
_AgRateLimitBUMCounterCIR_Object = MibTableColumn
agRateLimitBUMCounterCIR = _AgRateLimitBUMCounterCIR_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 4, 1, 6),
    _AgRateLimitBUMCounterCIR_Type()
)
agRateLimitBUMCounterCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agRateLimitBUMCounterCIR.setStatus("current")
_AgRateLimitBUMCounterAlertLowLevelThreshold_Type = Counter64
_AgRateLimitBUMCounterAlertLowLevelThreshold_Object = MibTableColumn
agRateLimitBUMCounterAlertLowLevelThreshold = _AgRateLimitBUMCounterAlertLowLevelThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 4, 1, 7),
    _AgRateLimitBUMCounterAlertLowLevelThreshold_Type()
)
agRateLimitBUMCounterAlertLowLevelThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agRateLimitBUMCounterAlertLowLevelThreshold.setStatus("current")
_AgRateLimitBUMCounterAlertHighLevelThreshold_Type = Counter64
_AgRateLimitBUMCounterAlertHighLevelThreshold_Object = MibTableColumn
agRateLimitBUMCounterAlertHighLevelThreshold = _AgRateLimitBUMCounterAlertHighLevelThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 4, 1, 8),
    _AgRateLimitBUMCounterAlertHighLevelThreshold_Type()
)
agRateLimitBUMCounterAlertHighLevelThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agRateLimitBUMCounterAlertHighLevelThreshold.setStatus("current")
_AgRateLimitBUMCounterShutdownTimeout_Type = Integer32
_AgRateLimitBUMCounterShutdownTimeout_Object = MibTableColumn
agRateLimitBUMCounterShutdownTimeout = _AgRateLimitBUMCounterShutdownTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 4, 1, 9),
    _AgRateLimitBUMCounterShutdownTimeout_Type()
)
agRateLimitBUMCounterShutdownTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agRateLimitBUMCounterShutdownTimeout.setStatus("current")
_SnBUMRLNotifications_ObjectIdentity = ObjectIdentity
snBUMRLNotifications = _SnBUMRLNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 5)
)

# Managed Objects groups


# Notification objects

snTrapBUMratelimitAlertLowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 5, 1)
)
snTrapBUMratelimitAlertLowThreshold.setObjects(
      *(("FOUNDRY-CAR-MIB", "agRateLimitBUMCounterCIR"),
        ("FOUNDRY-CAR-MIB", "agRateLimitBUMCounterAlertLowLevelThreshold"))
)
if mibBuilder.loadTexts:
    snTrapBUMratelimitAlertLowThreshold.setStatus(
        "current"
    )

snTrapBUMratelimitAlertHighThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 5, 2)
)
snTrapBUMratelimitAlertHighThreshold.setObjects(
      *(("FOUNDRY-CAR-MIB", "agRateLimitBUMCounterCIR"),
        ("FOUNDRY-CAR-MIB", "agRateLimitBUMCounterAlertHighLevelThreshold"))
)
if mibBuilder.loadTexts:
    snTrapBUMratelimitAlertHighThreshold.setStatus(
        "current"
    )

snTrapBUMratelimitShutdownLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 5, 3)
)
snTrapBUMratelimitShutdownLinkDown.setObjects(
    ("FOUNDRY-CAR-MIB", "agRateLimitBUMCounterCIR")
)
if mibBuilder.loadTexts:
    snTrapBUMratelimitShutdownLinkDown.setStatus(
        "current"
    )

snTrapBUMratelimitShutdownLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 5, 4)
)
snTrapBUMratelimitShutdownLinkUp.setObjects(
    ("FOUNDRY-CAR-MIB", "agRateLimitBUMCounterCIR")
)
if mibBuilder.loadTexts:
    snTrapBUMratelimitShutdownLinkUp.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-CAR-MIB",
    **{"PacketSource": PacketSource,
       "RateLimitType": RateLimitType,
       "RateLimitAction": RateLimitAction,
       "BUMPacketType": BUMPacketType,
       "snCAR": snCAR,
       "snPortCARs": snPortCARs,
       "snPortCARTable": snPortCARTable,
       "snPortCAREntry": snPortCAREntry,
       "snPortCARifIndex": snPortCARifIndex,
       "snPortCARDirection": snPortCARDirection,
       "snPortCARRowIndex": snPortCARRowIndex,
       "snPortCARType": snPortCARType,
       "snPortCARAccIdx": snPortCARAccIdx,
       "snPortCARRate": snPortCARRate,
       "snPortCARLimit": snPortCARLimit,
       "snPortCARExtLimit": snPortCARExtLimit,
       "snPortCARConformAction": snPortCARConformAction,
       "snPortCARExceedAction": snPortCARExceedAction,
       "snPortCARStatSwitchedPkts": snPortCARStatSwitchedPkts,
       "snPortCARStatSwitchedBytes": snPortCARStatSwitchedBytes,
       "snPortCARStatFilteredPkts": snPortCARStatFilteredPkts,
       "snPortCARStatFilteredBytes": snPortCARStatFilteredBytes,
       "snPortCARStatCurBurst": snPortCARStatCurBurst,
       "agRateLimitCounterTable": agRateLimitCounterTable,
       "agRateLimitCounterEntry": agRateLimitCounterEntry,
       "agRateLimitCounterFwdedOctets": agRateLimitCounterFwdedOctets,
       "agRateLimitCounterDroppedOctets": agRateLimitCounterDroppedOctets,
       "agRateLimitCounterReMarkedOctets": agRateLimitCounterReMarkedOctets,
       "agRateLimitCounterTotalOctets": agRateLimitCounterTotalOctets,
       "agRateLimitCounterIndexTable": agRateLimitCounterIndexTable,
       "agRateLimitCounterIndexEntry": agRateLimitCounterIndexEntry,
       "agRateLimitCounterIndexRowIndex": agRateLimitCounterIndexRowIndex,
       "agRateLimitCounterIndexDirection": agRateLimitCounterIndexDirection,
       "agRateLimitCounterIndexACLID": agRateLimitCounterIndexACLID,
       "agRateLimitCounterIndexVLANID": agRateLimitCounterIndexVLANID,
       "agRateLimitCounterIndexVLANGroupID": agRateLimitCounterIndexVLANGroupID,
       "agRateLimitCounterIndexMACAddress": agRateLimitCounterIndexMACAddress,
       "agRateLimitBUMCounterTable": agRateLimitBUMCounterTable,
       "agRateLimitBUMCounterEntry": agRateLimitBUMCounterEntry,
       "agRateLimitBUMCounterIfindex": agRateLimitBUMCounterIfindex,
       "agRateLimitBUMCounterVLANID": agRateLimitBUMCounterVLANID,
       "agRateLimitBUMCounterPacketType": agRateLimitBUMCounterPacketType,
       "agRateLimitBUMCounterDroppedOctets": agRateLimitBUMCounterDroppedOctets,
       "agRateLimitBUMCounterCBS": agRateLimitBUMCounterCBS,
       "agRateLimitBUMCounterCIR": agRateLimitBUMCounterCIR,
       "agRateLimitBUMCounterAlertLowLevelThreshold": agRateLimitBUMCounterAlertLowLevelThreshold,
       "agRateLimitBUMCounterAlertHighLevelThreshold": agRateLimitBUMCounterAlertHighLevelThreshold,
       "agRateLimitBUMCounterShutdownTimeout": agRateLimitBUMCounterShutdownTimeout,
       "snBUMRLNotifications": snBUMRLNotifications,
       "snTrapBUMratelimitAlertLowThreshold": snTrapBUMratelimitAlertLowThreshold,
       "snTrapBUMratelimitAlertHighThreshold": snTrapBUMratelimitAlertHighThreshold,
       "snTrapBUMratelimitShutdownLinkDown": snTrapBUMratelimitShutdownLinkDown,
       "snTrapBUMratelimitShutdownLinkUp": snTrapBUMratelimitShutdownLinkUp}
)
