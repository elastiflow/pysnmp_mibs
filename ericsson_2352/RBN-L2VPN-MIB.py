# SNMP MIB module (RBN-L2VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_2352/RBN-L2VPN-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:10:47 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(RbnCircuitHandle,) = mibBuilder.importSymbols(
    "RBN-TC",
    "RbnCircuitHandle")

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

rbnL2VpnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39)
)
if mibBuilder.loadTexts:
    rbnL2VpnMIB.setRevisions(
        ("2010-11-16 00:00",
         "2011-01-19 18:00",
         "2010-04-01 00:00",
         "2009-06-02 00:00",
         "2008-10-13 00:00",
         "2005-10-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RbnVpnVcType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("frame", 1),
          ("aal5", 2),
          ("atmTransCell", 3),
          ("vlan", 4),
          ("ethernet", 5),
          ("hdlc", 6),
          ("ppp", 7),
          ("cem", 8),
          ("atmVccCell", 9),
          ("atmVpcCell", 10))
    )



class RbnVpnXcFlagsType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("none", 0),
          ("inRib", 1),
          ("deletingSignal", 2),
          ("deletingConfig", 3),
          ("inLblmap", 4),
          ("updating", 5),
          ("up", 6),
          ("inLdp", 7),
          ("fromLdp", 8),
          ("fromConfig", 9),
          ("stale", 10),
          ("expSet", 11),
          ("ismUp", 12),
          ("peerUp", 13),
          ("remoteEncap", 14),
          ("localCbit", 15),
          ("remoteCbit", 16),
          ("primary", 17),
          ("backup", 18),
          ("primaryAutoRevert", 19),
          ("standby", 20),
          ("cwMismatch", 21),
          ("sigParamsMatch", 22))
    )


class RbnVpnPwFlagsType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("none", 0),
          ("inRib", 1),
          ("deletingSignal", 2),
          ("deletingConfig", 3),
          ("inLblmap", 4),
          ("updating", 5),
          ("up", 6),
          ("inLdp", 7),
          ("fromLdp", 8),
          ("fromConfig", 9),
          ("stale", 10),
          ("expSet", 11),
          ("ismUp", 12),
          ("peerUp", 13),
          ("remoteEncap", 14),
          ("localCbit", 15),
          ("remoteCbit", 16),
          ("primary", 17),
          ("backup", 18),
          ("primaryAutoRevert", 19),
          ("standby", 20),
          ("cwMismatch", 21),
          ("sigParamsMatch", 22),
          ("encapError", 23))
    )


class RbnVpnPwStateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("up", 1),
          ("down", 2),
          ("standby", 3))
    )



class RbnVpnPsnType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ip", 1),
          ("ipsec", 2),
          ("mpls", 3))
    )



# MIB Managed Objects in the order of their OIDs

_RbnMplsL2VpnMIBNotifications_ObjectIdentity = ObjectIdentity
rbnMplsL2VpnMIBNotifications = _RbnMplsL2VpnMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 0)
)
_RbnL2VpnMIBObjects_ObjectIdentity = ObjectIdentity
rbnL2VpnMIBObjects = _RbnL2VpnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1)
)
_RbnL2VpnStaticTable_Object = MibTable
rbnL2VpnStaticTable = _RbnL2VpnStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 1)
)
if mibBuilder.loadTexts:
    rbnL2VpnStaticTable.setStatus("obsolete")
_RbnL2VpnStaticEntry_Object = MibTableRow
rbnL2VpnStaticEntry = _RbnL2VpnStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 1, 1)
)
rbnL2VpnStaticEntry.setIndexNames(
    (0, "RBN-L2VPN-MIB", "rbnL2VpnStaticPeerAddr"),
    (0, "RBN-L2VPN-MIB", "rbnL2VpnStaticVpnLabel"),
)
if mibBuilder.loadTexts:
    rbnL2VpnStaticEntry.setStatus("obsolete")
_RbnL2VpnStaticPeerAddr_Type = IpAddress
_RbnL2VpnStaticPeerAddr_Object = MibTableColumn
rbnL2VpnStaticPeerAddr = _RbnL2VpnStaticPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 1, 1, 1),
    _RbnL2VpnStaticPeerAddr_Type()
)
rbnL2VpnStaticPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnL2VpnStaticPeerAddr.setStatus("obsolete")


class _RbnL2VpnStaticVpnLabel_Type(Unsigned32):
    """Custom type rbnL2VpnStaticVpnLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 65535),
    )


_RbnL2VpnStaticVpnLabel_Type.__name__ = "Unsigned32"
_RbnL2VpnStaticVpnLabel_Object = MibTableColumn
rbnL2VpnStaticVpnLabel = _RbnL2VpnStaticVpnLabel_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 1, 1, 2),
    _RbnL2VpnStaticVpnLabel_Type()
)
rbnL2VpnStaticVpnLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnL2VpnStaticVpnLabel.setStatus("obsolete")
_RbnL2VpnStaticCctHandle_Type = RbnCircuitHandle
_RbnL2VpnStaticCctHandle_Object = MibTableColumn
rbnL2VpnStaticCctHandle = _RbnL2VpnStaticCctHandle_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 1, 1, 3),
    _RbnL2VpnStaticCctHandle_Type()
)
rbnL2VpnStaticCctHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2VpnStaticCctHandle.setStatus("obsolete")
_RbnL2VpnStaticVpnCctHandle_Type = RbnCircuitHandle
_RbnL2VpnStaticVpnCctHandle_Object = MibTableColumn
rbnL2VpnStaticVpnCctHandle = _RbnL2VpnStaticVpnCctHandle_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 1, 1, 4),
    _RbnL2VpnStaticVpnCctHandle_Type()
)
rbnL2VpnStaticVpnCctHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2VpnStaticVpnCctHandle.setStatus("obsolete")
_RbnL2VpnStaticExpBits_Type = Unsigned32
_RbnL2VpnStaticExpBits_Object = MibTableColumn
rbnL2VpnStaticExpBits = _RbnL2VpnStaticExpBits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 1, 1, 5),
    _RbnL2VpnStaticExpBits_Type()
)
rbnL2VpnStaticExpBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2VpnStaticExpBits.setStatus("obsolete")
_RbnL2VpnStaticInputCctUp_Type = TruthValue
_RbnL2VpnStaticInputCctUp_Object = MibTableColumn
rbnL2VpnStaticInputCctUp = _RbnL2VpnStaticInputCctUp_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 1, 1, 6),
    _RbnL2VpnStaticInputCctUp_Type()
)
rbnL2VpnStaticInputCctUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2VpnStaticInputCctUp.setStatus("obsolete")
_RbnL2VpnStaticXcFlags_Type = RbnVpnXcFlagsType
_RbnL2VpnStaticXcFlags_Object = MibTableColumn
rbnL2VpnStaticXcFlags = _RbnL2VpnStaticXcFlags_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 1, 1, 7),
    _RbnL2VpnStaticXcFlags_Type()
)
rbnL2VpnStaticXcFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2VpnStaticXcFlags.setStatus("obsolete")
_RbnL2VpnStaticIfIndexOrZero_Type = InterfaceIndexOrZero
_RbnL2VpnStaticIfIndexOrZero_Object = MibTableColumn
rbnL2VpnStaticIfIndexOrZero = _RbnL2VpnStaticIfIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 1, 1, 8),
    _RbnL2VpnStaticIfIndexOrZero_Type()
)
rbnL2VpnStaticIfIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2VpnStaticIfIndexOrZero.setStatus("obsolete")
_RbnL2VpnLdpTable_Object = MibTable
rbnL2VpnLdpTable = _RbnL2VpnLdpTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 2)
)
if mibBuilder.loadTexts:
    rbnL2VpnLdpTable.setStatus("obsolete")
_RbnL2VpnLdpEntry_Object = MibTableRow
rbnL2VpnLdpEntry = _RbnL2VpnLdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 2, 1)
)
rbnL2VpnLdpEntry.setIndexNames(
    (0, "RBN-L2VPN-MIB", "rbnL2VpnLdpPeerAddr"),
    (0, "RBN-L2VPN-MIB", "rbnL2VpnLdpVcId"),
)
if mibBuilder.loadTexts:
    rbnL2VpnLdpEntry.setStatus("obsolete")
_RbnL2VpnLdpPeerAddr_Type = IpAddress
_RbnL2VpnLdpPeerAddr_Object = MibTableColumn
rbnL2VpnLdpPeerAddr = _RbnL2VpnLdpPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 2, 1, 1),
    _RbnL2VpnLdpPeerAddr_Type()
)
rbnL2VpnLdpPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnL2VpnLdpPeerAddr.setStatus("obsolete")


class _RbnL2VpnLdpVcId_Type(Integer32):
    """Custom type rbnL2VpnLdpVcId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RbnL2VpnLdpVcId_Type.__name__ = "Integer32"
_RbnL2VpnLdpVcId_Object = MibTableColumn
rbnL2VpnLdpVcId = _RbnL2VpnLdpVcId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 2, 1, 2),
    _RbnL2VpnLdpVcId_Type()
)
rbnL2VpnLdpVcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnL2VpnLdpVcId.setStatus("obsolete")
_RbnL2VpnLdpCctHandle_Type = RbnCircuitHandle
_RbnL2VpnLdpCctHandle_Object = MibTableColumn
rbnL2VpnLdpCctHandle = _RbnL2VpnLdpCctHandle_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 2, 1, 3),
    _RbnL2VpnLdpCctHandle_Type()
)
rbnL2VpnLdpCctHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2VpnLdpCctHandle.setStatus("obsolete")
_RbnL2VpnLdpVpnCctHandle_Type = RbnCircuitHandle
_RbnL2VpnLdpVpnCctHandle_Object = MibTableColumn
rbnL2VpnLdpVpnCctHandle = _RbnL2VpnLdpVpnCctHandle_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 2, 1, 4),
    _RbnL2VpnLdpVpnCctHandle_Type()
)
rbnL2VpnLdpVpnCctHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2VpnLdpVpnCctHandle.setStatus("obsolete")
_RbnL2VpnLdpInLabel_Type = Unsigned32
_RbnL2VpnLdpInLabel_Object = MibTableColumn
rbnL2VpnLdpInLabel = _RbnL2VpnLdpInLabel_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 2, 1, 5),
    _RbnL2VpnLdpInLabel_Type()
)
rbnL2VpnLdpInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2VpnLdpInLabel.setStatus("obsolete")
_RbnL2VpnLdpVpnLabel_Type = Unsigned32
_RbnL2VpnLdpVpnLabel_Object = MibTableColumn
rbnL2VpnLdpVpnLabel = _RbnL2VpnLdpVpnLabel_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 2, 1, 6),
    _RbnL2VpnLdpVpnLabel_Type()
)
rbnL2VpnLdpVpnLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2VpnLdpVpnLabel.setStatus("obsolete")
_RbnL2VpnLdpRemGrpId_Type = Unsigned32
_RbnL2VpnLdpRemGrpId_Object = MibTableColumn
rbnL2VpnLdpRemGrpId = _RbnL2VpnLdpRemGrpId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 2, 1, 7),
    _RbnL2VpnLdpRemGrpId_Type()
)
rbnL2VpnLdpRemGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2VpnLdpRemGrpId.setStatus("obsolete")


class _RbnL2VpnLdpLocEncap_Type(SnmpAdminString):
    """Custom type rbnL2VpnLdpLocEncap based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RbnL2VpnLdpLocEncap_Type.__name__ = "SnmpAdminString"
_RbnL2VpnLdpLocEncap_Object = MibTableColumn
rbnL2VpnLdpLocEncap = _RbnL2VpnLdpLocEncap_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 2, 1, 8),
    _RbnL2VpnLdpLocEncap_Type()
)
rbnL2VpnLdpLocEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2VpnLdpLocEncap.setStatus("obsolete")


class _RbnL2VpnLdpRemEncap_Type(SnmpAdminString):
    """Custom type rbnL2VpnLdpRemEncap based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RbnL2VpnLdpRemEncap_Type.__name__ = "SnmpAdminString"
_RbnL2VpnLdpRemEncap_Object = MibTableColumn
rbnL2VpnLdpRemEncap = _RbnL2VpnLdpRemEncap_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 2, 1, 9),
    _RbnL2VpnLdpRemEncap_Type()
)
rbnL2VpnLdpRemEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2VpnLdpRemEncap.setStatus("obsolete")
_RbnL2VpnLdpLocVcType_Type = RbnVpnVcType
_RbnL2VpnLdpLocVcType_Object = MibTableColumn
rbnL2VpnLdpLocVcType = _RbnL2VpnLdpLocVcType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 2, 1, 10),
    _RbnL2VpnLdpLocVcType_Type()
)
rbnL2VpnLdpLocVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2VpnLdpLocVcType.setStatus("obsolete")
_RbnL2VpnLdpRemVcType_Type = RbnVpnVcType
_RbnL2VpnLdpRemVcType_Object = MibTableColumn
rbnL2VpnLdpRemVcType = _RbnL2VpnLdpRemVcType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 2, 1, 11),
    _RbnL2VpnLdpRemVcType_Type()
)
rbnL2VpnLdpRemVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2VpnLdpRemVcType.setStatus("obsolete")
_RbnL2VpnLdpLocMtu_Type = Unsigned32
_RbnL2VpnLdpLocMtu_Object = MibTableColumn
rbnL2VpnLdpLocMtu = _RbnL2VpnLdpLocMtu_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 2, 1, 12),
    _RbnL2VpnLdpLocMtu_Type()
)
rbnL2VpnLdpLocMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2VpnLdpLocMtu.setStatus("obsolete")
_RbnL2VpnLdpRemMtu_Type = Unsigned32
_RbnL2VpnLdpRemMtu_Object = MibTableColumn
rbnL2VpnLdpRemMtu = _RbnL2VpnLdpRemMtu_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 2, 1, 13),
    _RbnL2VpnLdpRemMtu_Type()
)
rbnL2VpnLdpRemMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2VpnLdpRemMtu.setStatus("obsolete")
_RbnL2VpnLdpXcCctUp_Type = TruthValue
_RbnL2VpnLdpXcCctUp_Object = MibTableColumn
rbnL2VpnLdpXcCctUp = _RbnL2VpnLdpXcCctUp_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 2, 1, 14),
    _RbnL2VpnLdpXcCctUp_Type()
)
rbnL2VpnLdpXcCctUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2VpnLdpXcCctUp.setStatus("obsolete")
_RbnL2VpnLdpExpBits_Type = Unsigned32
_RbnL2VpnLdpExpBits_Object = MibTableColumn
rbnL2VpnLdpExpBits = _RbnL2VpnLdpExpBits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 2, 1, 15),
    _RbnL2VpnLdpExpBits_Type()
)
rbnL2VpnLdpExpBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2VpnLdpExpBits.setStatus("obsolete")
_RbnL2VpnLdpInputCctUp_Type = TruthValue
_RbnL2VpnLdpInputCctUp_Object = MibTableColumn
rbnL2VpnLdpInputCctUp = _RbnL2VpnLdpInputCctUp_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 2, 1, 16),
    _RbnL2VpnLdpInputCctUp_Type()
)
rbnL2VpnLdpInputCctUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2VpnLdpInputCctUp.setStatus("obsolete")
_RbnL2VpnLdpXcFlags_Type = RbnVpnXcFlagsType
_RbnL2VpnLdpXcFlags_Object = MibTableColumn
rbnL2VpnLdpXcFlags = _RbnL2VpnLdpXcFlags_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 2, 1, 17),
    _RbnL2VpnLdpXcFlags_Type()
)
rbnL2VpnLdpXcFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2VpnLdpXcFlags.setStatus("obsolete")
_RbnL2VpnLdpIfIndexOrZero_Type = InterfaceIndexOrZero
_RbnL2VpnLdpIfIndexOrZero_Object = MibTableColumn
rbnL2VpnLdpIfIndexOrZero = _RbnL2VpnLdpIfIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 1, 2, 1, 18),
    _RbnL2VpnLdpIfIndexOrZero_Type()
)
rbnL2VpnLdpIfIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnL2VpnLdpIfIndexOrZero.setStatus("obsolete")
_RbnL2VpnMIBConformance_ObjectIdentity = ObjectIdentity
rbnL2VpnMIBConformance = _RbnL2VpnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 2)
)
_RbnL2VpnMIBGroups_ObjectIdentity = ObjectIdentity
rbnL2VpnMIBGroups = _RbnL2VpnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 2, 1)
)
_RbnL2VpnMIBCompliances_ObjectIdentity = ObjectIdentity
rbnL2VpnMIBCompliances = _RbnL2VpnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 2, 2)
)
_RbnMplsL2VpnMIBGroups_ObjectIdentity = ObjectIdentity
rbnMplsL2VpnMIBGroups = _RbnMplsL2VpnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 2, 3)
)
_RbnMplsL2VpnMIBCompliances_ObjectIdentity = ObjectIdentity
rbnMplsL2VpnMIBCompliances = _RbnMplsL2VpnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 2, 4)
)
_RbnMplsL2VpnMIBObjects_ObjectIdentity = ObjectIdentity
rbnMplsL2VpnMIBObjects = _RbnMplsL2VpnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3)
)
_RbnMplsL2VpnStaticTable_Object = MibTable
rbnMplsL2VpnStaticTable = _RbnMplsL2VpnStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 3)
)
if mibBuilder.loadTexts:
    rbnMplsL2VpnStaticTable.setStatus("current")
_RbnMplsL2VpnStaticEntry_Object = MibTableRow
rbnMplsL2VpnStaticEntry = _RbnMplsL2VpnStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 3, 1)
)
rbnMplsL2VpnStaticEntry.setIndexNames(
    (0, "RBN-L2VPN-MIB", "rbnMplsL2VpnStaticVpnLabel"),
    (0, "RBN-L2VPN-MIB", "rbnMplsL2VpnStaticPeerAddr"),
)
if mibBuilder.loadTexts:
    rbnMplsL2VpnStaticEntry.setStatus("current")


class _RbnMplsL2VpnStaticVpnLabel_Type(Unsigned32):
    """Custom type rbnMplsL2VpnStaticVpnLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 65535),
    )


_RbnMplsL2VpnStaticVpnLabel_Type.__name__ = "Unsigned32"
_RbnMplsL2VpnStaticVpnLabel_Object = MibTableColumn
rbnMplsL2VpnStaticVpnLabel = _RbnMplsL2VpnStaticVpnLabel_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 3, 1, 1),
    _RbnMplsL2VpnStaticVpnLabel_Type()
)
rbnMplsL2VpnStaticVpnLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnMplsL2VpnStaticVpnLabel.setStatus("current")
_RbnMplsL2VpnStaticPeerAddr_Type = IpAddress
_RbnMplsL2VpnStaticPeerAddr_Object = MibTableColumn
rbnMplsL2VpnStaticPeerAddr = _RbnMplsL2VpnStaticPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 3, 1, 2),
    _RbnMplsL2VpnStaticPeerAddr_Type()
)
rbnMplsL2VpnStaticPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnMplsL2VpnStaticPeerAddr.setStatus("current")
_RbnMplsL2VpnStaticCctHandle_Type = RbnCircuitHandle
_RbnMplsL2VpnStaticCctHandle_Object = MibTableColumn
rbnMplsL2VpnStaticCctHandle = _RbnMplsL2VpnStaticCctHandle_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 3, 1, 3),
    _RbnMplsL2VpnStaticCctHandle_Type()
)
rbnMplsL2VpnStaticCctHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnStaticCctHandle.setStatus("current")
_RbnMplsL2VpnStaticVpnCctHandle_Type = RbnCircuitHandle
_RbnMplsL2VpnStaticVpnCctHandle_Object = MibTableColumn
rbnMplsL2VpnStaticVpnCctHandle = _RbnMplsL2VpnStaticVpnCctHandle_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 3, 1, 4),
    _RbnMplsL2VpnStaticVpnCctHandle_Type()
)
rbnMplsL2VpnStaticVpnCctHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnStaticVpnCctHandle.setStatus("current")
_RbnMplsL2VpnStaticExpBits_Type = Unsigned32
_RbnMplsL2VpnStaticExpBits_Object = MibTableColumn
rbnMplsL2VpnStaticExpBits = _RbnMplsL2VpnStaticExpBits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 3, 1, 5),
    _RbnMplsL2VpnStaticExpBits_Type()
)
rbnMplsL2VpnStaticExpBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnStaticExpBits.setStatus("current")
_RbnMplsL2VpnStaticInputCctUp_Type = TruthValue
_RbnMplsL2VpnStaticInputCctUp_Object = MibTableColumn
rbnMplsL2VpnStaticInputCctUp = _RbnMplsL2VpnStaticInputCctUp_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 3, 1, 6),
    _RbnMplsL2VpnStaticInputCctUp_Type()
)
rbnMplsL2VpnStaticInputCctUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnStaticInputCctUp.setStatus("current")
_RbnMplsL2VpnStaticXcFlags_Type = RbnVpnXcFlagsType
_RbnMplsL2VpnStaticXcFlags_Object = MibTableColumn
rbnMplsL2VpnStaticXcFlags = _RbnMplsL2VpnStaticXcFlags_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 3, 1, 7),
    _RbnMplsL2VpnStaticXcFlags_Type()
)
rbnMplsL2VpnStaticXcFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnStaticXcFlags.setStatus("current")
_RbnMplsL2VpnStaticIfIndexOrZero_Type = InterfaceIndexOrZero
_RbnMplsL2VpnStaticIfIndexOrZero_Object = MibTableColumn
rbnMplsL2VpnStaticIfIndexOrZero = _RbnMplsL2VpnStaticIfIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 3, 1, 8),
    _RbnMplsL2VpnStaticIfIndexOrZero_Type()
)
rbnMplsL2VpnStaticIfIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnStaticIfIndexOrZero.setStatus("current")
_RbnMplsL2VpnStaticPwFlags_Type = RbnVpnPwFlagsType
_RbnMplsL2VpnStaticPwFlags_Object = MibTableColumn
rbnMplsL2VpnStaticPwFlags = _RbnMplsL2VpnStaticPwFlags_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 3, 1, 9),
    _RbnMplsL2VpnStaticPwFlags_Type()
)
rbnMplsL2VpnStaticPwFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnStaticPwFlags.setStatus("current")
_RbnMplsL2VpnStaticPwState_Type = RbnVpnPwStateType
_RbnMplsL2VpnStaticPwState_Object = MibTableColumn
rbnMplsL2VpnStaticPwState = _RbnMplsL2VpnStaticPwState_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 3, 1, 10),
    _RbnMplsL2VpnStaticPwState_Type()
)
rbnMplsL2VpnStaticPwState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnStaticPwState.setStatus("current")
_RbnMplsL2VpnStaticInLabel_Type = Unsigned32
_RbnMplsL2VpnStaticInLabel_Object = MibTableColumn
rbnMplsL2VpnStaticInLabel = _RbnMplsL2VpnStaticInLabel_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 3, 1, 11),
    _RbnMplsL2VpnStaticInLabel_Type()
)
rbnMplsL2VpnStaticInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnStaticInLabel.setStatus("current")
_RbnMplsL2VpnLdpTable_Object = MibTable
rbnMplsL2VpnLdpTable = _RbnMplsL2VpnLdpTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 4)
)
if mibBuilder.loadTexts:
    rbnMplsL2VpnLdpTable.setStatus("current")
_RbnMplsL2VpnLdpEntry_Object = MibTableRow
rbnMplsL2VpnLdpEntry = _RbnMplsL2VpnLdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 4, 1)
)
rbnMplsL2VpnLdpEntry.setIndexNames(
    (0, "RBN-L2VPN-MIB", "rbnMplsL2VpnLdpVcId"),
    (0, "RBN-L2VPN-MIB", "rbnMplsL2VpnLdpPeerAddr"),
)
if mibBuilder.loadTexts:
    rbnMplsL2VpnLdpEntry.setStatus("current")


class _RbnMplsL2VpnLdpVcId_Type(Unsigned32):
    """Custom type rbnMplsL2VpnLdpVcId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RbnMplsL2VpnLdpVcId_Type.__name__ = "Unsigned32"
_RbnMplsL2VpnLdpVcId_Object = MibTableColumn
rbnMplsL2VpnLdpVcId = _RbnMplsL2VpnLdpVcId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 4, 1, 1),
    _RbnMplsL2VpnLdpVcId_Type()
)
rbnMplsL2VpnLdpVcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnMplsL2VpnLdpVcId.setStatus("current")
_RbnMplsL2VpnLdpPeerAddr_Type = IpAddress
_RbnMplsL2VpnLdpPeerAddr_Object = MibTableColumn
rbnMplsL2VpnLdpPeerAddr = _RbnMplsL2VpnLdpPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 4, 1, 2),
    _RbnMplsL2VpnLdpPeerAddr_Type()
)
rbnMplsL2VpnLdpPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnMplsL2VpnLdpPeerAddr.setStatus("current")
_RbnMplsL2VpnLdpCctHandle_Type = RbnCircuitHandle
_RbnMplsL2VpnLdpCctHandle_Object = MibTableColumn
rbnMplsL2VpnLdpCctHandle = _RbnMplsL2VpnLdpCctHandle_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 4, 1, 3),
    _RbnMplsL2VpnLdpCctHandle_Type()
)
rbnMplsL2VpnLdpCctHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnLdpCctHandle.setStatus("current")
_RbnMplsL2VpnLdpVpnCctHandle_Type = RbnCircuitHandle
_RbnMplsL2VpnLdpVpnCctHandle_Object = MibTableColumn
rbnMplsL2VpnLdpVpnCctHandle = _RbnMplsL2VpnLdpVpnCctHandle_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 4, 1, 4),
    _RbnMplsL2VpnLdpVpnCctHandle_Type()
)
rbnMplsL2VpnLdpVpnCctHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnLdpVpnCctHandle.setStatus("current")
_RbnMplsL2VpnLdpInLabel_Type = Unsigned32
_RbnMplsL2VpnLdpInLabel_Object = MibTableColumn
rbnMplsL2VpnLdpInLabel = _RbnMplsL2VpnLdpInLabel_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 4, 1, 5),
    _RbnMplsL2VpnLdpInLabel_Type()
)
rbnMplsL2VpnLdpInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnLdpInLabel.setStatus("current")
_RbnMplsL2VpnLdpVpnLabel_Type = Unsigned32
_RbnMplsL2VpnLdpVpnLabel_Object = MibTableColumn
rbnMplsL2VpnLdpVpnLabel = _RbnMplsL2VpnLdpVpnLabel_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 4, 1, 6),
    _RbnMplsL2VpnLdpVpnLabel_Type()
)
rbnMplsL2VpnLdpVpnLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnLdpVpnLabel.setStatus("current")
_RbnMplsL2VpnLdpRemGrpId_Type = Unsigned32
_RbnMplsL2VpnLdpRemGrpId_Object = MibTableColumn
rbnMplsL2VpnLdpRemGrpId = _RbnMplsL2VpnLdpRemGrpId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 4, 1, 7),
    _RbnMplsL2VpnLdpRemGrpId_Type()
)
rbnMplsL2VpnLdpRemGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnLdpRemGrpId.setStatus("current")


class _RbnMplsL2VpnLdpLocEncap_Type(SnmpAdminString):
    """Custom type rbnMplsL2VpnLdpLocEncap based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RbnMplsL2VpnLdpLocEncap_Type.__name__ = "SnmpAdminString"
_RbnMplsL2VpnLdpLocEncap_Object = MibTableColumn
rbnMplsL2VpnLdpLocEncap = _RbnMplsL2VpnLdpLocEncap_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 4, 1, 8),
    _RbnMplsL2VpnLdpLocEncap_Type()
)
rbnMplsL2VpnLdpLocEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnLdpLocEncap.setStatus("current")


class _RbnMplsL2VpnLdpRemEncap_Type(SnmpAdminString):
    """Custom type rbnMplsL2VpnLdpRemEncap based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RbnMplsL2VpnLdpRemEncap_Type.__name__ = "SnmpAdminString"
_RbnMplsL2VpnLdpRemEncap_Object = MibTableColumn
rbnMplsL2VpnLdpRemEncap = _RbnMplsL2VpnLdpRemEncap_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 4, 1, 9),
    _RbnMplsL2VpnLdpRemEncap_Type()
)
rbnMplsL2VpnLdpRemEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnLdpRemEncap.setStatus("current")
_RbnMplsL2VpnLdpLocVcType_Type = RbnVpnVcType
_RbnMplsL2VpnLdpLocVcType_Object = MibTableColumn
rbnMplsL2VpnLdpLocVcType = _RbnMplsL2VpnLdpLocVcType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 4, 1, 10),
    _RbnMplsL2VpnLdpLocVcType_Type()
)
rbnMplsL2VpnLdpLocVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnLdpLocVcType.setStatus("current")
_RbnMplsL2VpnLdpRemVcType_Type = RbnVpnVcType
_RbnMplsL2VpnLdpRemVcType_Object = MibTableColumn
rbnMplsL2VpnLdpRemVcType = _RbnMplsL2VpnLdpRemVcType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 4, 1, 11),
    _RbnMplsL2VpnLdpRemVcType_Type()
)
rbnMplsL2VpnLdpRemVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnLdpRemVcType.setStatus("current")
_RbnMplsL2VpnLdpLocMtu_Type = Unsigned32
_RbnMplsL2VpnLdpLocMtu_Object = MibTableColumn
rbnMplsL2VpnLdpLocMtu = _RbnMplsL2VpnLdpLocMtu_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 4, 1, 12),
    _RbnMplsL2VpnLdpLocMtu_Type()
)
rbnMplsL2VpnLdpLocMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnLdpLocMtu.setStatus("current")
_RbnMplsL2VpnLdpRemMtu_Type = Unsigned32
_RbnMplsL2VpnLdpRemMtu_Object = MibTableColumn
rbnMplsL2VpnLdpRemMtu = _RbnMplsL2VpnLdpRemMtu_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 4, 1, 13),
    _RbnMplsL2VpnLdpRemMtu_Type()
)
rbnMplsL2VpnLdpRemMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnLdpRemMtu.setStatus("current")
_RbnMplsL2VpnLdpXcCctUp_Type = TruthValue
_RbnMplsL2VpnLdpXcCctUp_Object = MibTableColumn
rbnMplsL2VpnLdpXcCctUp = _RbnMplsL2VpnLdpXcCctUp_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 4, 1, 14),
    _RbnMplsL2VpnLdpXcCctUp_Type()
)
rbnMplsL2VpnLdpXcCctUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnLdpXcCctUp.setStatus("deprecated")
_RbnMplsL2VpnLdpExpBits_Type = Unsigned32
_RbnMplsL2VpnLdpExpBits_Object = MibTableColumn
rbnMplsL2VpnLdpExpBits = _RbnMplsL2VpnLdpExpBits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 4, 1, 15),
    _RbnMplsL2VpnLdpExpBits_Type()
)
rbnMplsL2VpnLdpExpBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnLdpExpBits.setStatus("current")
_RbnMplsL2VpnLdpInputCctUp_Type = TruthValue
_RbnMplsL2VpnLdpInputCctUp_Object = MibTableColumn
rbnMplsL2VpnLdpInputCctUp = _RbnMplsL2VpnLdpInputCctUp_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 4, 1, 16),
    _RbnMplsL2VpnLdpInputCctUp_Type()
)
rbnMplsL2VpnLdpInputCctUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnLdpInputCctUp.setStatus("current")
_RbnMplsL2VpnLdpXcFlags_Type = RbnVpnXcFlagsType
_RbnMplsL2VpnLdpXcFlags_Object = MibTableColumn
rbnMplsL2VpnLdpXcFlags = _RbnMplsL2VpnLdpXcFlags_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 4, 1, 17),
    _RbnMplsL2VpnLdpXcFlags_Type()
)
rbnMplsL2VpnLdpXcFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnLdpXcFlags.setStatus("deprecated")
_RbnMplsL2VpnLdpIfIndexOrZero_Type = InterfaceIndexOrZero
_RbnMplsL2VpnLdpIfIndexOrZero_Object = MibTableColumn
rbnMplsL2VpnLdpIfIndexOrZero = _RbnMplsL2VpnLdpIfIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 4, 1, 18),
    _RbnMplsL2VpnLdpIfIndexOrZero_Type()
)
rbnMplsL2VpnLdpIfIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnLdpIfIndexOrZero.setStatus("current")
_RbnMplsL2VpnLdpPwFlags_Type = RbnVpnPwFlagsType
_RbnMplsL2VpnLdpPwFlags_Object = MibTableColumn
rbnMplsL2VpnLdpPwFlags = _RbnMplsL2VpnLdpPwFlags_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 4, 1, 19),
    _RbnMplsL2VpnLdpPwFlags_Type()
)
rbnMplsL2VpnLdpPwFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnLdpPwFlags.setStatus("current")
_RbnMplsL2VpnLdpPwState_Type = RbnVpnPwStateType
_RbnMplsL2VpnLdpPwState_Object = MibTableColumn
rbnMplsL2VpnLdpPwState = _RbnMplsL2VpnLdpPwState_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 3, 4, 1, 20),
    _RbnMplsL2VpnLdpPwState_Type()
)
rbnMplsL2VpnLdpPwState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMplsL2VpnLdpPwState.setStatus("current")
_RbnMplsL2VpnMIBConformance_ObjectIdentity = ObjectIdentity
rbnMplsL2VpnMIBConformance = _RbnMplsL2VpnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 4)
)
_RbnMplsL2VpnMIBScalars_ObjectIdentity = ObjectIdentity
rbnMplsL2VpnMIBScalars = _RbnMplsL2VpnMIBScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 5)
)


class _RbnMplsL2VpnNotificationEnable_Type(TruthValue):
    """Custom type rbnMplsL2VpnNotificationEnable based on TruthValue"""
    defaultValue = 2


_RbnMplsL2VpnNotificationEnable_Type.__name__ = "TruthValue"
_RbnMplsL2VpnNotificationEnable_Object = MibScalar
rbnMplsL2VpnNotificationEnable = _RbnMplsL2VpnNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 5, 1),
    _RbnMplsL2VpnNotificationEnable_Type()
)
rbnMplsL2VpnNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnMplsL2VpnNotificationEnable.setStatus("current")
_RbnUdpL2VpnMIBObjects_ObjectIdentity = ObjectIdentity
rbnUdpL2VpnMIBObjects = _RbnUdpL2VpnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 6)
)
_RbnUdpL2VpnStaticTable_Object = MibTable
rbnUdpL2VpnStaticTable = _RbnUdpL2VpnStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 6, 1)
)
if mibBuilder.loadTexts:
    rbnUdpL2VpnStaticTable.setStatus("current")
_RbnUdpL2VpnStaticEntry_Object = MibTableRow
rbnUdpL2VpnStaticEntry = _RbnUdpL2VpnStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 6, 1, 1)
)
rbnUdpL2VpnStaticEntry.setIndexNames(
    (0, "RBN-L2VPN-MIB", "rbnUdpL2VpnStaticPeerPort"),
    (0, "RBN-L2VPN-MIB", "rbnUdpL2VpnStaticPeerAddressType"),
    (0, "RBN-L2VPN-MIB", "rbnUdpL2VpnStaticPeerAddress"),
)
if mibBuilder.loadTexts:
    rbnUdpL2VpnStaticEntry.setStatus("current")
_RbnUdpL2VpnStaticPeerPort_Type = InetPortNumber
_RbnUdpL2VpnStaticPeerPort_Object = MibTableColumn
rbnUdpL2VpnStaticPeerPort = _RbnUdpL2VpnStaticPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 6, 1, 1, 1),
    _RbnUdpL2VpnStaticPeerPort_Type()
)
rbnUdpL2VpnStaticPeerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnUdpL2VpnStaticPeerPort.setStatus("current")
_RbnUdpL2VpnStaticPeerAddressType_Type = InetAddressType
_RbnUdpL2VpnStaticPeerAddressType_Object = MibTableColumn
rbnUdpL2VpnStaticPeerAddressType = _RbnUdpL2VpnStaticPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 6, 1, 1, 2),
    _RbnUdpL2VpnStaticPeerAddressType_Type()
)
rbnUdpL2VpnStaticPeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnUdpL2VpnStaticPeerAddressType.setStatus("current")
_RbnUdpL2VpnStaticPeerAddress_Type = InetAddress
_RbnUdpL2VpnStaticPeerAddress_Object = MibTableColumn
rbnUdpL2VpnStaticPeerAddress = _RbnUdpL2VpnStaticPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 6, 1, 1, 3),
    _RbnUdpL2VpnStaticPeerAddress_Type()
)
rbnUdpL2VpnStaticPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnUdpL2VpnStaticPeerAddress.setStatus("current")
_RbnUdpL2VpnStaticSourceAddressType_Type = InetAddressType
_RbnUdpL2VpnStaticSourceAddressType_Object = MibTableColumn
rbnUdpL2VpnStaticSourceAddressType = _RbnUdpL2VpnStaticSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 6, 1, 1, 4),
    _RbnUdpL2VpnStaticSourceAddressType_Type()
)
rbnUdpL2VpnStaticSourceAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnUdpL2VpnStaticSourceAddressType.setStatus("current")
_RbnUdpL2VpnStaticSourceAddress_Type = InetAddress
_RbnUdpL2VpnStaticSourceAddress_Object = MibTableColumn
rbnUdpL2VpnStaticSourceAddress = _RbnUdpL2VpnStaticSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 6, 1, 1, 5),
    _RbnUdpL2VpnStaticSourceAddress_Type()
)
rbnUdpL2VpnStaticSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnUdpL2VpnStaticSourceAddress.setStatus("current")
_RbnUdpL2VpnStaticSourcePort_Type = InetPortNumber
_RbnUdpL2VpnStaticSourcePort_Object = MibTableColumn
rbnUdpL2VpnStaticSourcePort = _RbnUdpL2VpnStaticSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 6, 1, 1, 6),
    _RbnUdpL2VpnStaticSourcePort_Type()
)
rbnUdpL2VpnStaticSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnUdpL2VpnStaticSourcePort.setStatus("current")
_RbnUdpL2vpnStaticAccessCctHandle_Type = RbnCircuitHandle
_RbnUdpL2vpnStaticAccessCctHandle_Object = MibTableColumn
rbnUdpL2vpnStaticAccessCctHandle = _RbnUdpL2vpnStaticAccessCctHandle_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 6, 1, 1, 7),
    _RbnUdpL2vpnStaticAccessCctHandle_Type()
)
rbnUdpL2vpnStaticAccessCctHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnUdpL2vpnStaticAccessCctHandle.setStatus("current")
_RbnUdpL2VpnStaticVpnCctHandle_Type = RbnCircuitHandle
_RbnUdpL2VpnStaticVpnCctHandle_Object = MibTableColumn
rbnUdpL2VpnStaticVpnCctHandle = _RbnUdpL2VpnStaticVpnCctHandle_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 6, 1, 1, 8),
    _RbnUdpL2VpnStaticVpnCctHandle_Type()
)
rbnUdpL2VpnStaticVpnCctHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnUdpL2VpnStaticVpnCctHandle.setStatus("current")
_RbnUdpL2VpnStaticInputCctUp_Type = TruthValue
_RbnUdpL2VpnStaticInputCctUp_Object = MibTableColumn
rbnUdpL2VpnStaticInputCctUp = _RbnUdpL2VpnStaticInputCctUp_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 6, 1, 1, 9),
    _RbnUdpL2VpnStaticInputCctUp_Type()
)
rbnUdpL2VpnStaticInputCctUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnUdpL2VpnStaticInputCctUp.setStatus("current")
_RbnUdpL2VpnStaticIfIndexOrZero_Type = InterfaceIndexOrZero
_RbnUdpL2VpnStaticIfIndexOrZero_Object = MibTableColumn
rbnUdpL2VpnStaticIfIndexOrZero = _RbnUdpL2VpnStaticIfIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 6, 1, 1, 10),
    _RbnUdpL2VpnStaticIfIndexOrZero_Type()
)
rbnUdpL2VpnStaticIfIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnUdpL2VpnStaticIfIndexOrZero.setStatus("current")
_RbnUdpL2VpnStaticPwFlags_Type = RbnVpnPwFlagsType
_RbnUdpL2VpnStaticPwFlags_Object = MibTableColumn
rbnUdpL2VpnStaticPwFlags = _RbnUdpL2VpnStaticPwFlags_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 6, 1, 1, 11),
    _RbnUdpL2VpnStaticPwFlags_Type()
)
rbnUdpL2VpnStaticPwFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnUdpL2VpnStaticPwFlags.setStatus("current")
_RbnUdpL2vpnStaticDscpCode_Type = Integer32
_RbnUdpL2vpnStaticDscpCode_Object = MibTableColumn
rbnUdpL2vpnStaticDscpCode = _RbnUdpL2vpnStaticDscpCode_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 6, 1, 1, 12),
    _RbnUdpL2vpnStaticDscpCode_Type()
)
rbnUdpL2vpnStaticDscpCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnUdpL2vpnStaticDscpCode.setStatus("current")
_RbnUdpL2VpnStaticPwState_Type = RbnVpnPwStateType
_RbnUdpL2VpnStaticPwState_Object = MibTableColumn
rbnUdpL2VpnStaticPwState = _RbnUdpL2VpnStaticPwState_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 6, 1, 1, 13),
    _RbnUdpL2VpnStaticPwState_Type()
)
rbnUdpL2VpnStaticPwState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnUdpL2VpnStaticPwState.setStatus("current")
_RbnUdpL2VpnStaticPsnType_Type = RbnVpnPsnType
_RbnUdpL2VpnStaticPsnType_Object = MibTableColumn
rbnUdpL2VpnStaticPsnType = _RbnUdpL2VpnStaticPsnType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 6, 1, 1, 14),
    _RbnUdpL2VpnStaticPsnType_Type()
)
rbnUdpL2VpnStaticPsnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnUdpL2VpnStaticPsnType.setStatus("current")

# Managed Objects groups

rbnL2VpnStaticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 2, 1, 1)
)
rbnL2VpnStaticGroup.setObjects(
      *(("RBN-L2VPN-MIB", "rbnL2VpnStaticCctHandle"),
        ("RBN-L2VPN-MIB", "rbnL2VpnStaticVpnCctHandle"),
        ("RBN-L2VPN-MIB", "rbnL2VpnStaticExpBits"),
        ("RBN-L2VPN-MIB", "rbnL2VpnStaticInputCctUp"),
        ("RBN-L2VPN-MIB", "rbnL2VpnStaticXcFlags"),
        ("RBN-L2VPN-MIB", "rbnL2VpnStaticIfIndexOrZero"))
)
if mibBuilder.loadTexts:
    rbnL2VpnStaticGroup.setStatus("obsolete")

rbnL2VpnLdpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 2, 1, 2)
)
rbnL2VpnLdpGroup.setObjects(
      *(("RBN-L2VPN-MIB", "rbnL2VpnLdpCctHandle"),
        ("RBN-L2VPN-MIB", "rbnL2VpnLdpVpnCctHandle"),
        ("RBN-L2VPN-MIB", "rbnL2VpnLdpInLabel"),
        ("RBN-L2VPN-MIB", "rbnL2VpnLdpVpnLabel"),
        ("RBN-L2VPN-MIB", "rbnL2VpnLdpRemGrpId"),
        ("RBN-L2VPN-MIB", "rbnL2VpnLdpLocEncap"),
        ("RBN-L2VPN-MIB", "rbnL2VpnLdpRemEncap"),
        ("RBN-L2VPN-MIB", "rbnL2VpnLdpLocVcType"),
        ("RBN-L2VPN-MIB", "rbnL2VpnLdpRemVcType"),
        ("RBN-L2VPN-MIB", "rbnL2VpnLdpLocMtu"),
        ("RBN-L2VPN-MIB", "rbnL2VpnLdpRemMtu"),
        ("RBN-L2VPN-MIB", "rbnL2VpnLdpXcCctUp"),
        ("RBN-L2VPN-MIB", "rbnL2VpnLdpExpBits"),
        ("RBN-L2VPN-MIB", "rbnL2VpnLdpInputCctUp"),
        ("RBN-L2VPN-MIB", "rbnL2VpnLdpXcFlags"),
        ("RBN-L2VPN-MIB", "rbnL2VpnLdpIfIndexOrZero"))
)
if mibBuilder.loadTexts:
    rbnL2VpnLdpGroup.setStatus("obsolete")

rbnMplsL2VpnPwScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 2, 1, 3)
)
rbnMplsL2VpnPwScalarGroup.setObjects(
    ("RBN-L2VPN-MIB", "rbnMplsL2VpnNotificationEnable")
)
if mibBuilder.loadTexts:
    rbnMplsL2VpnPwScalarGroup.setStatus("current")

rbnMplsL2VpnStaticPwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 2, 1, 4)
)
rbnMplsL2VpnStaticPwGroup.setObjects(
      *(("RBN-L2VPN-MIB", "rbnMplsL2VpnStaticCctHandle"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnStaticVpnCctHandle"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnStaticInputCctUp"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnStaticExpBits"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnStaticIfIndexOrZero"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnStaticPwFlags"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnStaticPwState"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnStaticInLabel"))
)
if mibBuilder.loadTexts:
    rbnMplsL2VpnStaticPwGroup.setStatus("current")

rbnMplsL2VpnLdpPwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 2, 1, 5)
)
rbnMplsL2VpnLdpPwGroup.setObjects(
      *(("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpCctHandle"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpVpnCctHandle"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpInLabel"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpVpnLabel"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpRemGrpId"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpLocEncap"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpRemEncap"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpLocVcType"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpRemVcType"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpLocMtu"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpRemMtu"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpExpBits"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpIfIndexOrZero"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpPwFlags"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpPwState"))
)
if mibBuilder.loadTexts:
    rbnMplsL2VpnLdpPwGroup.setStatus("current")

rbnUdpL2VpnStaticPwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 2, 1, 7)
)
rbnUdpL2VpnStaticPwGroup.setObjects(
      *(("RBN-L2VPN-MIB", "rbnUdpL2VpnStaticSourceAddressType"),
        ("RBN-L2VPN-MIB", "rbnUdpL2VpnStaticSourceAddress"),
        ("RBN-L2VPN-MIB", "rbnUdpL2VpnStaticSourcePort"),
        ("RBN-L2VPN-MIB", "rbnUdpL2vpnStaticAccessCctHandle"),
        ("RBN-L2VPN-MIB", "rbnUdpL2VpnStaticVpnCctHandle"),
        ("RBN-L2VPN-MIB", "rbnUdpL2VpnStaticInputCctUp"),
        ("RBN-L2VPN-MIB", "rbnUdpL2VpnStaticIfIndexOrZero"),
        ("RBN-L2VPN-MIB", "rbnUdpL2VpnStaticPwFlags"),
        ("RBN-L2VPN-MIB", "rbnUdpL2VpnStaticPwState"),
        ("RBN-L2VPN-MIB", "rbnUdpL2vpnStaticDscpCode"),
        ("RBN-L2VPN-MIB", "rbnUdpL2VpnStaticPsnType"))
)
if mibBuilder.loadTexts:
    rbnUdpL2VpnStaticPwGroup.setStatus("current")

rbnMplsL2VpnStaticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 2, 3, 1)
)
rbnMplsL2VpnStaticGroup.setObjects(
      *(("RBN-L2VPN-MIB", "rbnMplsL2VpnStaticCctHandle"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnStaticVpnCctHandle"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnStaticExpBits"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnStaticInputCctUp"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnStaticXcFlags"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnStaticIfIndexOrZero"))
)
if mibBuilder.loadTexts:
    rbnMplsL2VpnStaticGroup.setStatus("current")

rbnMplsL2VpnLdpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 2, 3, 2)
)
rbnMplsL2VpnLdpGroup.setObjects(
      *(("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpCctHandle"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpVpnCctHandle"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpInLabel"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpVpnLabel"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpRemGrpId"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpLocEncap"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpRemEncap"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpLocVcType"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpRemVcType"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpLocMtu"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpRemMtu"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpXcCctUp"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpExpBits"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpInputCctUp"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpXcFlags"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpIfIndexOrZero"))
)
if mibBuilder.loadTexts:
    rbnMplsL2VpnLdpGroup.setStatus("current")


# Notification objects

rbnMplsL2VpnLdpPwStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 0, 1)
)
rbnMplsL2VpnLdpPwStateChange.setObjects(
    ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpPwState")
)
if mibBuilder.loadTexts:
    rbnMplsL2VpnLdpPwStateChange.setStatus(
        "current"
    )


# Notifications groups

rbnMplsL2VpnPwNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 2, 1, 6)
)
rbnMplsL2VpnPwNotificationGroup.setObjects(
    ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpPwStateChange")
)
if mibBuilder.loadTexts:
    rbnMplsL2VpnPwNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbnL2VpnMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 2, 2, 1)
)
rbnL2VpnMIBCompliance.setObjects(
      *(("RBN-L2VPN-MIB", "rbnL2VpnStaticGroup"),
        ("RBN-L2VPN-MIB", "rbnL2VpnLdpGroup"))
)
if mibBuilder.loadTexts:
    rbnL2VpnMIBCompliance.setStatus(
        "obsolete"
    )

rbnMplsL2VpnPwMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 2, 2, 2)
)
rbnMplsL2VpnPwMIBCompliance.setObjects(
      *(("RBN-L2VPN-MIB", "rbnMplsL2VpnPwScalarGroup"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnStaticPwGroup"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpPwGroup"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnPwNotificationGroup"))
)
if mibBuilder.loadTexts:
    rbnMplsL2VpnPwMIBCompliance.setStatus(
        "current"
    )

rbnUdpL2VpnPwMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 2, 2, 3)
)
rbnUdpL2VpnPwMIBCompliance.setObjects(
    ("RBN-L2VPN-MIB", "rbnUdpL2VpnStaticPwGroup")
)
if mibBuilder.loadTexts:
    rbnUdpL2VpnPwMIBCompliance.setStatus(
        "current"
    )

rbnMplsL2VpnMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 39, 2, 4, 1)
)
rbnMplsL2VpnMIBCompliance.setObjects(
      *(("RBN-L2VPN-MIB", "rbnMplsL2VpnStaticGroup"),
        ("RBN-L2VPN-MIB", "rbnMplsL2VpnLdpGroup"))
)
if mibBuilder.loadTexts:
    rbnMplsL2VpnMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-L2VPN-MIB",
    **{"RbnVpnVcType": RbnVpnVcType,
       "RbnVpnXcFlagsType": RbnVpnXcFlagsType,
       "RbnVpnPwFlagsType": RbnVpnPwFlagsType,
       "RbnVpnPwStateType": RbnVpnPwStateType,
       "RbnVpnPsnType": RbnVpnPsnType,
       "rbnL2VpnMIB": rbnL2VpnMIB,
       "rbnMplsL2VpnMIBNotifications": rbnMplsL2VpnMIBNotifications,
       "rbnMplsL2VpnLdpPwStateChange": rbnMplsL2VpnLdpPwStateChange,
       "rbnL2VpnMIBObjects": rbnL2VpnMIBObjects,
       "rbnL2VpnStaticTable": rbnL2VpnStaticTable,
       "rbnL2VpnStaticEntry": rbnL2VpnStaticEntry,
       "rbnL2VpnStaticPeerAddr": rbnL2VpnStaticPeerAddr,
       "rbnL2VpnStaticVpnLabel": rbnL2VpnStaticVpnLabel,
       "rbnL2VpnStaticCctHandle": rbnL2VpnStaticCctHandle,
       "rbnL2VpnStaticVpnCctHandle": rbnL2VpnStaticVpnCctHandle,
       "rbnL2VpnStaticExpBits": rbnL2VpnStaticExpBits,
       "rbnL2VpnStaticInputCctUp": rbnL2VpnStaticInputCctUp,
       "rbnL2VpnStaticXcFlags": rbnL2VpnStaticXcFlags,
       "rbnL2VpnStaticIfIndexOrZero": rbnL2VpnStaticIfIndexOrZero,
       "rbnL2VpnLdpTable": rbnL2VpnLdpTable,
       "rbnL2VpnLdpEntry": rbnL2VpnLdpEntry,
       "rbnL2VpnLdpPeerAddr": rbnL2VpnLdpPeerAddr,
       "rbnL2VpnLdpVcId": rbnL2VpnLdpVcId,
       "rbnL2VpnLdpCctHandle": rbnL2VpnLdpCctHandle,
       "rbnL2VpnLdpVpnCctHandle": rbnL2VpnLdpVpnCctHandle,
       "rbnL2VpnLdpInLabel": rbnL2VpnLdpInLabel,
       "rbnL2VpnLdpVpnLabel": rbnL2VpnLdpVpnLabel,
       "rbnL2VpnLdpRemGrpId": rbnL2VpnLdpRemGrpId,
       "rbnL2VpnLdpLocEncap": rbnL2VpnLdpLocEncap,
       "rbnL2VpnLdpRemEncap": rbnL2VpnLdpRemEncap,
       "rbnL2VpnLdpLocVcType": rbnL2VpnLdpLocVcType,
       "rbnL2VpnLdpRemVcType": rbnL2VpnLdpRemVcType,
       "rbnL2VpnLdpLocMtu": rbnL2VpnLdpLocMtu,
       "rbnL2VpnLdpRemMtu": rbnL2VpnLdpRemMtu,
       "rbnL2VpnLdpXcCctUp": rbnL2VpnLdpXcCctUp,
       "rbnL2VpnLdpExpBits": rbnL2VpnLdpExpBits,
       "rbnL2VpnLdpInputCctUp": rbnL2VpnLdpInputCctUp,
       "rbnL2VpnLdpXcFlags": rbnL2VpnLdpXcFlags,
       "rbnL2VpnLdpIfIndexOrZero": rbnL2VpnLdpIfIndexOrZero,
       "rbnL2VpnMIBConformance": rbnL2VpnMIBConformance,
       "rbnL2VpnMIBGroups": rbnL2VpnMIBGroups,
       "rbnL2VpnStaticGroup": rbnL2VpnStaticGroup,
       "rbnL2VpnLdpGroup": rbnL2VpnLdpGroup,
       "rbnMplsL2VpnPwScalarGroup": rbnMplsL2VpnPwScalarGroup,
       "rbnMplsL2VpnStaticPwGroup": rbnMplsL2VpnStaticPwGroup,
       "rbnMplsL2VpnLdpPwGroup": rbnMplsL2VpnLdpPwGroup,
       "rbnMplsL2VpnPwNotificationGroup": rbnMplsL2VpnPwNotificationGroup,
       "rbnUdpL2VpnStaticPwGroup": rbnUdpL2VpnStaticPwGroup,
       "rbnL2VpnMIBCompliances": rbnL2VpnMIBCompliances,
       "rbnL2VpnMIBCompliance": rbnL2VpnMIBCompliance,
       "rbnMplsL2VpnPwMIBCompliance": rbnMplsL2VpnPwMIBCompliance,
       "rbnUdpL2VpnPwMIBCompliance": rbnUdpL2VpnPwMIBCompliance,
       "rbnMplsL2VpnMIBGroups": rbnMplsL2VpnMIBGroups,
       "rbnMplsL2VpnStaticGroup": rbnMplsL2VpnStaticGroup,
       "rbnMplsL2VpnLdpGroup": rbnMplsL2VpnLdpGroup,
       "rbnMplsL2VpnMIBCompliances": rbnMplsL2VpnMIBCompliances,
       "rbnMplsL2VpnMIBCompliance": rbnMplsL2VpnMIBCompliance,
       "rbnMplsL2VpnMIBObjects": rbnMplsL2VpnMIBObjects,
       "rbnMplsL2VpnStaticTable": rbnMplsL2VpnStaticTable,
       "rbnMplsL2VpnStaticEntry": rbnMplsL2VpnStaticEntry,
       "rbnMplsL2VpnStaticVpnLabel": rbnMplsL2VpnStaticVpnLabel,
       "rbnMplsL2VpnStaticPeerAddr": rbnMplsL2VpnStaticPeerAddr,
       "rbnMplsL2VpnStaticCctHandle": rbnMplsL2VpnStaticCctHandle,
       "rbnMplsL2VpnStaticVpnCctHandle": rbnMplsL2VpnStaticVpnCctHandle,
       "rbnMplsL2VpnStaticExpBits": rbnMplsL2VpnStaticExpBits,
       "rbnMplsL2VpnStaticInputCctUp": rbnMplsL2VpnStaticInputCctUp,
       "rbnMplsL2VpnStaticXcFlags": rbnMplsL2VpnStaticXcFlags,
       "rbnMplsL2VpnStaticIfIndexOrZero": rbnMplsL2VpnStaticIfIndexOrZero,
       "rbnMplsL2VpnStaticPwFlags": rbnMplsL2VpnStaticPwFlags,
       "rbnMplsL2VpnStaticPwState": rbnMplsL2VpnStaticPwState,
       "rbnMplsL2VpnStaticInLabel": rbnMplsL2VpnStaticInLabel,
       "rbnMplsL2VpnLdpTable": rbnMplsL2VpnLdpTable,
       "rbnMplsL2VpnLdpEntry": rbnMplsL2VpnLdpEntry,
       "rbnMplsL2VpnLdpVcId": rbnMplsL2VpnLdpVcId,
       "rbnMplsL2VpnLdpPeerAddr": rbnMplsL2VpnLdpPeerAddr,
       "rbnMplsL2VpnLdpCctHandle": rbnMplsL2VpnLdpCctHandle,
       "rbnMplsL2VpnLdpVpnCctHandle": rbnMplsL2VpnLdpVpnCctHandle,
       "rbnMplsL2VpnLdpInLabel": rbnMplsL2VpnLdpInLabel,
       "rbnMplsL2VpnLdpVpnLabel": rbnMplsL2VpnLdpVpnLabel,
       "rbnMplsL2VpnLdpRemGrpId": rbnMplsL2VpnLdpRemGrpId,
       "rbnMplsL2VpnLdpLocEncap": rbnMplsL2VpnLdpLocEncap,
       "rbnMplsL2VpnLdpRemEncap": rbnMplsL2VpnLdpRemEncap,
       "rbnMplsL2VpnLdpLocVcType": rbnMplsL2VpnLdpLocVcType,
       "rbnMplsL2VpnLdpRemVcType": rbnMplsL2VpnLdpRemVcType,
       "rbnMplsL2VpnLdpLocMtu": rbnMplsL2VpnLdpLocMtu,
       "rbnMplsL2VpnLdpRemMtu": rbnMplsL2VpnLdpRemMtu,
       "rbnMplsL2VpnLdpXcCctUp": rbnMplsL2VpnLdpXcCctUp,
       "rbnMplsL2VpnLdpExpBits": rbnMplsL2VpnLdpExpBits,
       "rbnMplsL2VpnLdpInputCctUp": rbnMplsL2VpnLdpInputCctUp,
       "rbnMplsL2VpnLdpXcFlags": rbnMplsL2VpnLdpXcFlags,
       "rbnMplsL2VpnLdpIfIndexOrZero": rbnMplsL2VpnLdpIfIndexOrZero,
       "rbnMplsL2VpnLdpPwFlags": rbnMplsL2VpnLdpPwFlags,
       "rbnMplsL2VpnLdpPwState": rbnMplsL2VpnLdpPwState,
       "rbnMplsL2VpnMIBConformance": rbnMplsL2VpnMIBConformance,
       "rbnMplsL2VpnMIBScalars": rbnMplsL2VpnMIBScalars,
       "rbnMplsL2VpnNotificationEnable": rbnMplsL2VpnNotificationEnable,
       "rbnUdpL2VpnMIBObjects": rbnUdpL2VpnMIBObjects,
       "rbnUdpL2VpnStaticTable": rbnUdpL2VpnStaticTable,
       "rbnUdpL2VpnStaticEntry": rbnUdpL2VpnStaticEntry,
       "rbnUdpL2VpnStaticPeerPort": rbnUdpL2VpnStaticPeerPort,
       "rbnUdpL2VpnStaticPeerAddressType": rbnUdpL2VpnStaticPeerAddressType,
       "rbnUdpL2VpnStaticPeerAddress": rbnUdpL2VpnStaticPeerAddress,
       "rbnUdpL2VpnStaticSourceAddressType": rbnUdpL2VpnStaticSourceAddressType,
       "rbnUdpL2VpnStaticSourceAddress": rbnUdpL2VpnStaticSourceAddress,
       "rbnUdpL2VpnStaticSourcePort": rbnUdpL2VpnStaticSourcePort,
       "rbnUdpL2vpnStaticAccessCctHandle": rbnUdpL2vpnStaticAccessCctHandle,
       "rbnUdpL2VpnStaticVpnCctHandle": rbnUdpL2VpnStaticVpnCctHandle,
       "rbnUdpL2VpnStaticInputCctUp": rbnUdpL2VpnStaticInputCctUp,
       "rbnUdpL2VpnStaticIfIndexOrZero": rbnUdpL2VpnStaticIfIndexOrZero,
       "rbnUdpL2VpnStaticPwFlags": rbnUdpL2VpnStaticPwFlags,
       "rbnUdpL2vpnStaticDscpCode": rbnUdpL2vpnStaticDscpCode,
       "rbnUdpL2VpnStaticPwState": rbnUdpL2VpnStaticPwState,
       "rbnUdpL2VpnStaticPsnType": rbnUdpL2VpnStaticPsnType}
)
