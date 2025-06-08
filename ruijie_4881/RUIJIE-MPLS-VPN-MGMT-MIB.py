# SNMP MIB module (RUIJIE-MPLS-VPN-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-MPLS-VPN-MGMT-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:12 2025
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

(Dscp,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "Dscp")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(mplsL3VpnVrfName,) = mibBuilder.importSymbols(
    "MPLS-L3VPN-STD-MIB",
    "mplsL3VpnVrfName")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp")

(VPNIdOrZero,) = mibBuilder.importSymbols(
    "VPN-TC-STD-MIB",
    "VPNIdOrZero")


# MODULE-IDENTITY

ruijieMplsVPNMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122)
)
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtMIB.setRevisions(
        ("2013-01-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieMplsVPNMgmtMIBObjects_ObjectIdentity = ObjectIdentity
ruijieMplsVPNMgmtMIBObjects = _RuijieMplsVPNMgmtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1)
)
_RuijieMplsVPNMgmtVrf_ObjectIdentity = ObjectIdentity
ruijieMplsVPNMgmtVrf = _RuijieMplsVPNMgmtVrf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 1)
)
_RuijieMplsVPNMgmtVrfTable_Object = MibTable
ruijieMplsVPNMgmtVrfTable = _RuijieMplsVPNMgmtVrfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtVrfTable.setStatus("current")
_RuijieMplsVPNMgmtVrfEntry_Object = MibTableRow
ruijieMplsVPNMgmtVrfEntry = _RuijieMplsVPNMgmtVrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 1, 1, 1)
)
ruijieMplsVPNMgmtVrfEntry.setIndexNames(
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfName"),
)
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtVrfEntry.setStatus("current")
_RuijieMplsVPNMgmtVrfName_Type = DisplayString
_RuijieMplsVPNMgmtVrfName_Object = MibTableColumn
ruijieMplsVPNMgmtVrfName = _RuijieMplsVPNMgmtVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 1, 1, 1, 1),
    _RuijieMplsVPNMgmtVrfName_Type()
)
ruijieMplsVPNMgmtVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtVrfName.setStatus("current")
_RuijieMplsVPNMgmtVrfIntfFault_Type = Unsigned32
_RuijieMplsVPNMgmtVrfIntfFault_Object = MibTableColumn
ruijieMplsVPNMgmtVrfIntfFault = _RuijieMplsVPNMgmtVrfIntfFault_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 1, 1, 1, 2),
    _RuijieMplsVPNMgmtVrfIntfFault_Type()
)
ruijieMplsVPNMgmtVrfIntfFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtVrfIntfFault.setStatus("current")
_RuijieMplsVPNMgmtVrfVpnId_Type = VPNIdOrZero
_RuijieMplsVPNMgmtVrfVpnId_Object = MibTableColumn
ruijieMplsVPNMgmtVrfVpnId = _RuijieMplsVPNMgmtVrfVpnId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 1, 1, 1, 3),
    _RuijieMplsVPNMgmtVrfVpnId_Type()
)
ruijieMplsVPNMgmtVrfVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtVrfVpnId.setStatus("current")


class _RuijieMplsVPNMgmtVrfVpnIdType_Type(Integer32):
    """Custom type ruijieMplsVPNMgmtVrfVpnIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l3vpn", 1),
          ("l2vpn", 2),
          ("other", 3))
    )


_RuijieMplsVPNMgmtVrfVpnIdType_Type.__name__ = "Integer32"
_RuijieMplsVPNMgmtVrfVpnIdType_Object = MibTableColumn
ruijieMplsVPNMgmtVrfVpnIdType = _RuijieMplsVPNMgmtVrfVpnIdType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 1, 1, 1, 4),
    _RuijieMplsVPNMgmtVrfVpnIdType_Type()
)
ruijieMplsVPNMgmtVrfVpnIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtVrfVpnIdType.setStatus("current")


class _RuijieMplsVPNMgmtVrfVpnRunState_Type(Integer32):
    """Custom type ruijieMplsVPNMgmtVrfVpnRunState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ACTIVE", 1),
          ("INACTIVE", 2))
    )


_RuijieMplsVPNMgmtVrfVpnRunState_Type.__name__ = "Integer32"
_RuijieMplsVPNMgmtVrfVpnRunState_Object = MibTableColumn
ruijieMplsVPNMgmtVrfVpnRunState = _RuijieMplsVPNMgmtVrfVpnRunState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 1, 1, 1, 5),
    _RuijieMplsVPNMgmtVrfVpnRunState_Type()
)
ruijieMplsVPNMgmtVrfVpnRunState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtVrfVpnRunState.setStatus("current")
_RuijieMplsVPNMgmtRoute_ObjectIdentity = ObjectIdentity
ruijieMplsVPNMgmtRoute = _RuijieMplsVPNMgmtRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 2)
)
_RuijieMplsVPNMgmtVrfRteTable_Object = MibTable
ruijieMplsVPNMgmtVrfRteTable = _RuijieMplsVPNMgmtVrfRteTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtVrfRteTable.setStatus("current")
_RuijieMplsVPNMgmtVrfRteEntry_Object = MibTableRow
ruijieMplsVPNMgmtVrfRteEntry = _RuijieMplsVPNMgmtVrfRteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 2, 1, 1)
)
ruijieMplsVPNMgmtVrfRteEntry.setIndexNames(
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfName"),
    (0, "RUIJIE-MPLS-VPN-MGMT-MIB", "ruijieMplsVPNMgmtRteDestType"),
    (0, "RUIJIE-MPLS-VPN-MGMT-MIB", "ruijieMplsVPNMgmtRteDest"),
    (0, "RUIJIE-MPLS-VPN-MGMT-MIB", "ruijieMplsVPNMgmtRtePfxLen"),
    (0, "RUIJIE-MPLS-VPN-MGMT-MIB", "ruijieMplsVPNMgmtRtePolicy"),
    (0, "RUIJIE-MPLS-VPN-MGMT-MIB", "ruijieMplsVPNMgmtRteNHopType"),
    (0, "RUIJIE-MPLS-VPN-MGMT-MIB", "ruijieMplsVPNMgmtRteNextHop"),
)
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtVrfRteEntry.setStatus("current")
_RuijieMplsVPNMgmtRteDestType_Type = InetAddressType
_RuijieMplsVPNMgmtRteDestType_Object = MibTableColumn
ruijieMplsVPNMgmtRteDestType = _RuijieMplsVPNMgmtRteDestType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 2, 1, 1, 1),
    _RuijieMplsVPNMgmtRteDestType_Type()
)
ruijieMplsVPNMgmtRteDestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtRteDestType.setStatus("current")
_RuijieMplsVPNMgmtRteDest_Type = InetAddress
_RuijieMplsVPNMgmtRteDest_Object = MibTableColumn
ruijieMplsVPNMgmtRteDest = _RuijieMplsVPNMgmtRteDest_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 2, 1, 1, 2),
    _RuijieMplsVPNMgmtRteDest_Type()
)
ruijieMplsVPNMgmtRteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtRteDest.setStatus("current")


class _RuijieMplsVPNMgmtRtePfxLen_Type(InetAddressPrefixLength):
    """Custom type ruijieMplsVPNMgmtRtePfxLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RuijieMplsVPNMgmtRtePfxLen_Type.__name__ = "InetAddressPrefixLength"
_RuijieMplsVPNMgmtRtePfxLen_Object = MibTableColumn
ruijieMplsVPNMgmtRtePfxLen = _RuijieMplsVPNMgmtRtePfxLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 2, 1, 1, 3),
    _RuijieMplsVPNMgmtRtePfxLen_Type()
)
ruijieMplsVPNMgmtRtePfxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtRtePfxLen.setStatus("current")
_RuijieMplsVPNMgmtRtePolicy_Type = ObjectIdentifier
_RuijieMplsVPNMgmtRtePolicy_Object = MibTableColumn
ruijieMplsVPNMgmtRtePolicy = _RuijieMplsVPNMgmtRtePolicy_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 2, 1, 1, 4),
    _RuijieMplsVPNMgmtRtePolicy_Type()
)
ruijieMplsVPNMgmtRtePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtRtePolicy.setStatus("current")
_RuijieMplsVPNMgmtRteNHopType_Type = InetAddressType
_RuijieMplsVPNMgmtRteNHopType_Object = MibTableColumn
ruijieMplsVPNMgmtRteNHopType = _RuijieMplsVPNMgmtRteNHopType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 2, 1, 1, 5),
    _RuijieMplsVPNMgmtRteNHopType_Type()
)
ruijieMplsVPNMgmtRteNHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtRteNHopType.setStatus("current")
_RuijieMplsVPNMgmtRteNextHop_Type = InetAddress
_RuijieMplsVPNMgmtRteNextHop_Object = MibTableColumn
ruijieMplsVPNMgmtRteNextHop = _RuijieMplsVPNMgmtRteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 2, 1, 1, 6),
    _RuijieMplsVPNMgmtRteNextHop_Type()
)
ruijieMplsVPNMgmtRteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtRteNextHop.setStatus("current")
_RuijieMplsVPNMgmtRteDscp_Type = Dscp
_RuijieMplsVPNMgmtRteDscp_Object = MibTableColumn
ruijieMplsVPNMgmtRteDscp = _RuijieMplsVPNMgmtRteDscp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 2, 1, 1, 7),
    _RuijieMplsVPNMgmtRteDscp_Type()
)
ruijieMplsVPNMgmtRteDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtRteDscp.setStatus("current")
_RuijieMplsVPNMgmtRteStorageType_Type = StorageType
_RuijieMplsVPNMgmtRteStorageType_Object = MibTableColumn
ruijieMplsVPNMgmtRteStorageType = _RuijieMplsVPNMgmtRteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 2, 1, 1, 8),
    _RuijieMplsVPNMgmtRteStorageType_Type()
)
ruijieMplsVPNMgmtRteStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtRteStorageType.setStatus("current")
_RuijieMplsVPNMgmtQos_ObjectIdentity = ObjectIdentity
ruijieMplsVPNMgmtQos = _RuijieMplsVPNMgmtQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 3)
)
_RuijieMplsVPNMgmtQosLSP_ObjectIdentity = ObjectIdentity
ruijieMplsVPNMgmtQosLSP = _RuijieMplsVPNMgmtQosLSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 3, 1)
)
_RuijieMplsVPNMgmtLSPNum_Type = Unsigned32
_RuijieMplsVPNMgmtLSPNum_Object = MibScalar
ruijieMplsVPNMgmtLSPNum = _RuijieMplsVPNMgmtLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 3, 1, 1),
    _RuijieMplsVPNMgmtLSPNum_Type()
)
ruijieMplsVPNMgmtLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtLSPNum.setStatus("current")
_RuijieMplsVPNMgmtBackupLSPNum_Type = Unsigned32
_RuijieMplsVPNMgmtBackupLSPNum_Object = MibScalar
ruijieMplsVPNMgmtBackupLSPNum = _RuijieMplsVPNMgmtBackupLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 3, 1, 2),
    _RuijieMplsVPNMgmtBackupLSPNum_Type()
)
ruijieMplsVPNMgmtBackupLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtBackupLSPNum.setStatus("current")
_RuijieMplsVPNMgmtLDPLSPNum_Type = Unsigned32
_RuijieMplsVPNMgmtLDPLSPNum_Object = MibScalar
ruijieMplsVPNMgmtLDPLSPNum = _RuijieMplsVPNMgmtLDPLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 3, 1, 3),
    _RuijieMplsVPNMgmtLDPLSPNum_Type()
)
ruijieMplsVPNMgmtLDPLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtLDPLSPNum.setStatus("current")
_RuijieMplsVPNMgmtBGPLSPNum_Type = Unsigned32
_RuijieMplsVPNMgmtBGPLSPNum_Object = MibScalar
ruijieMplsVPNMgmtBGPLSPNum = _RuijieMplsVPNMgmtBGPLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 3, 1, 4),
    _RuijieMplsVPNMgmtBGPLSPNum_Type()
)
ruijieMplsVPNMgmtBGPLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtBGPLSPNum.setStatus("current")
_RuijieMplsVPNMgmtStaticLSPNum_Type = Unsigned32
_RuijieMplsVPNMgmtStaticLSPNum_Object = MibScalar
ruijieMplsVPNMgmtStaticLSPNum = _RuijieMplsVPNMgmtStaticLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 3, 1, 5),
    _RuijieMplsVPNMgmtStaticLSPNum_Type()
)
ruijieMplsVPNMgmtStaticLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtStaticLSPNum.setStatus("current")
_RuijieMplsVPNMgmtCRLDPLSPNum_Type = Unsigned32
_RuijieMplsVPNMgmtCRLDPLSPNum_Object = MibScalar
ruijieMplsVPNMgmtCRLDPLSPNum = _RuijieMplsVPNMgmtCRLDPLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 3, 1, 6),
    _RuijieMplsVPNMgmtCRLDPLSPNum_Type()
)
ruijieMplsVPNMgmtCRLDPLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtCRLDPLSPNum.setStatus("current")
_RuijieMplsVPNMgmtRsvpLSPNum_Type = Unsigned32
_RuijieMplsVPNMgmtRsvpLSPNum_Object = MibScalar
ruijieMplsVPNMgmtRsvpLSPNum = _RuijieMplsVPNMgmtRsvpLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 3, 1, 7),
    _RuijieMplsVPNMgmtRsvpLSPNum_Type()
)
ruijieMplsVPNMgmtRsvpLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtRsvpLSPNum.setStatus("current")
_RuijieMplsVPNMgmtBFDLSPNum_Type = Unsigned32
_RuijieMplsVPNMgmtBFDLSPNum_Object = MibScalar
ruijieMplsVPNMgmtBFDLSPNum = _RuijieMplsVPNMgmtBFDLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 3, 1, 8),
    _RuijieMplsVPNMgmtBFDLSPNum_Type()
)
ruijieMplsVPNMgmtBFDLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtBFDLSPNum.setStatus("current")
_RuijieMplsVPNMgmtOAMLSPNum_Type = Unsigned32
_RuijieMplsVPNMgmtOAMLSPNum_Object = MibScalar
ruijieMplsVPNMgmtOAMLSPNum = _RuijieMplsVPNMgmtOAMLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 3, 1, 9),
    _RuijieMplsVPNMgmtOAMLSPNum_Type()
)
ruijieMplsVPNMgmtOAMLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtOAMLSPNum.setStatus("current")
_RuijieMplsVPNMgmtIngressLSPNum_Type = Unsigned32
_RuijieMplsVPNMgmtIngressLSPNum_Object = MibScalar
ruijieMplsVPNMgmtIngressLSPNum = _RuijieMplsVPNMgmtIngressLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 3, 1, 10),
    _RuijieMplsVPNMgmtIngressLSPNum_Type()
)
ruijieMplsVPNMgmtIngressLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtIngressLSPNum.setStatus("current")
_RuijieMplsVPNMgmtTransitLSPNum_Type = Unsigned32
_RuijieMplsVPNMgmtTransitLSPNum_Object = MibScalar
ruijieMplsVPNMgmtTransitLSPNum = _RuijieMplsVPNMgmtTransitLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 3, 1, 11),
    _RuijieMplsVPNMgmtTransitLSPNum_Type()
)
ruijieMplsVPNMgmtTransitLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtTransitLSPNum.setStatus("current")
_RuijieMplsVPNMgmtEgressLSPNum_Type = Unsigned32
_RuijieMplsVPNMgmtEgressLSPNum_Object = MibScalar
ruijieMplsVPNMgmtEgressLSPNum = _RuijieMplsVPNMgmtEgressLSPNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 3, 1, 12),
    _RuijieMplsVPNMgmtEgressLSPNum_Type()
)
ruijieMplsVPNMgmtEgressLSPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtEgressLSPNum.setStatus("current")
_RuijieMplsVPNMgmtQosFault_ObjectIdentity = ObjectIdentity
ruijieMplsVPNMgmtQosFault = _RuijieMplsVPNMgmtQosFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 3, 2)
)
_RuijieMplsLSPFaultBFD_Type = Unsigned32
_RuijieMplsLSPFaultBFD_Object = MibScalar
ruijieMplsLSPFaultBFD = _RuijieMplsLSPFaultBFD_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 3, 2, 1),
    _RuijieMplsLSPFaultBFD_Type()
)
ruijieMplsLSPFaultBFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsLSPFaultBFD.setStatus("current")
_RuijieMplsLSPFaultOAM_Type = Unsigned32
_RuijieMplsLSPFaultOAM_Object = MibScalar
ruijieMplsLSPFaultOAM = _RuijieMplsLSPFaultOAM_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 3, 2, 2),
    _RuijieMplsLSPFaultOAM_Type()
)
ruijieMplsLSPFaultOAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsLSPFaultOAM.setStatus("current")
_RuijieMplsVrfFault_Type = Unsigned32
_RuijieMplsVrfFault_Object = MibScalar
ruijieMplsVrfFault = _RuijieMplsVrfFault_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 3, 2, 3),
    _RuijieMplsVrfFault_Type()
)
ruijieMplsVrfFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVrfFault.setStatus("current")
_RuijieMplsPWFault_Type = Unsigned32
_RuijieMplsPWFault_Object = MibScalar
ruijieMplsPWFault = _RuijieMplsPWFault_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 3, 2, 4),
    _RuijieMplsPWFault_Type()
)
ruijieMplsPWFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsPWFault.setStatus("current")
_RuijieMplsVPNMgmtL2vpn_ObjectIdentity = ObjectIdentity
ruijieMplsVPNMgmtL2vpn = _RuijieMplsVPNMgmtL2vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 4)
)
_RuijieMplsVPNMgmtL2vpnTable_Object = MibTable
ruijieMplsVPNMgmtL2vpnTable = _RuijieMplsVPNMgmtL2vpnTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtL2vpnTable.setStatus("current")
_RuijieMplsVPNMgmtL2vpnEntry_Object = MibTableRow
ruijieMplsVPNMgmtL2vpnEntry = _RuijieMplsVPNMgmtL2vpnEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 4, 1, 1)
)
ruijieMplsVPNMgmtL2vpnEntry.setIndexNames(
    (0, "RUIJIE-MPLS-VPN-MGMT-MIB", "ruijieMplsVPNMgmtL2vpnRmUID"),
)
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtL2vpnEntry.setStatus("current")


class _RuijieMplsVPNMgmtL2vpnRmUID_Type(OctetString):
    """Custom type ruijieMplsVPNMgmtL2vpnRmUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RuijieMplsVPNMgmtL2vpnRmUID_Type.__name__ = "OctetString"
_RuijieMplsVPNMgmtL2vpnRmUID_Object = MibTableColumn
ruijieMplsVPNMgmtL2vpnRmUID = _RuijieMplsVPNMgmtL2vpnRmUID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 4, 1, 1, 1),
    _RuijieMplsVPNMgmtL2vpnRmUID_Type()
)
ruijieMplsVPNMgmtL2vpnRmUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtL2vpnRmUID.setStatus("current")


class _RuijieMplsVPNMgmtL2vpnNativeName_Type(OctetString):
    """Custom type ruijieMplsVPNMgmtL2vpnNativeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieMplsVPNMgmtL2vpnNativeName_Type.__name__ = "OctetString"
_RuijieMplsVPNMgmtL2vpnNativeName_Object = MibTableColumn
ruijieMplsVPNMgmtL2vpnNativeName = _RuijieMplsVPNMgmtL2vpnNativeName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 4, 1, 1, 2),
    _RuijieMplsVPNMgmtL2vpnNativeName_Type()
)
ruijieMplsVPNMgmtL2vpnNativeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtL2vpnNativeName.setStatus("current")


class _RuijieMplsVPNMgmtL2vpnServiceType_Type(Integer32):
    """Custom type ruijieMplsVPNMgmtL2vpnServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("PWE3", 1),
          ("VPLS", 2))
    )


_RuijieMplsVPNMgmtL2vpnServiceType_Type.__name__ = "Integer32"
_RuijieMplsVPNMgmtL2vpnServiceType_Object = MibTableColumn
ruijieMplsVPNMgmtL2vpnServiceType = _RuijieMplsVPNMgmtL2vpnServiceType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 4, 1, 1, 3),
    _RuijieMplsVPNMgmtL2vpnServiceType_Type()
)
ruijieMplsVPNMgmtL2vpnServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtL2vpnServiceType.setStatus("current")


class _RuijieMplsVPNMgmtL2vpnOwner_Type(OctetString):
    """Custom type ruijieMplsVPNMgmtL2vpnOwner based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RuijieMplsVPNMgmtL2vpnOwner_Type.__name__ = "OctetString"
_RuijieMplsVPNMgmtL2vpnOwner_Object = MibTableColumn
ruijieMplsVPNMgmtL2vpnOwner = _RuijieMplsVPNMgmtL2vpnOwner_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 4, 1, 1, 4),
    _RuijieMplsVPNMgmtL2vpnOwner_Type()
)
ruijieMplsVPNMgmtL2vpnOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtL2vpnOwner.setStatus("current")


class _RuijieMplsVPNMgmtL2vpnRunState_Type(Integer32):
    """Custom type ruijieMplsVPNMgmtL2vpnRunState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("UP", 1),
          ("DOWN", 2))
    )


_RuijieMplsVPNMgmtL2vpnRunState_Type.__name__ = "Integer32"
_RuijieMplsVPNMgmtL2vpnRunState_Object = MibTableColumn
ruijieMplsVPNMgmtL2vpnRunState = _RuijieMplsVPNMgmtL2vpnRunState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 4, 1, 1, 5),
    _RuijieMplsVPNMgmtL2vpnRunState_Type()
)
ruijieMplsVPNMgmtL2vpnRunState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtL2vpnRunState.setStatus("current")


class _RuijieMplsVPNMgmtL2vpnCIR_Type(OctetString):
    """Custom type ruijieMplsVPNMgmtL2vpnCIR based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RuijieMplsVPNMgmtL2vpnCIR_Type.__name__ = "OctetString"
_RuijieMplsVPNMgmtL2vpnCIR_Object = MibTableColumn
ruijieMplsVPNMgmtL2vpnCIR = _RuijieMplsVPNMgmtL2vpnCIR_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 4, 1, 1, 6),
    _RuijieMplsVPNMgmtL2vpnCIR_Type()
)
ruijieMplsVPNMgmtL2vpnCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtL2vpnCIR.setStatus("current")


class _RuijieMplsVPNMgmtL2vpnPIR_Type(OctetString):
    """Custom type ruijieMplsVPNMgmtL2vpnPIR based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RuijieMplsVPNMgmtL2vpnPIR_Type.__name__ = "OctetString"
_RuijieMplsVPNMgmtL2vpnPIR_Object = MibTableColumn
ruijieMplsVPNMgmtL2vpnPIR = _RuijieMplsVPNMgmtL2vpnPIR_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 4, 1, 1, 7),
    _RuijieMplsVPNMgmtL2vpnPIR_Type()
)
ruijieMplsVPNMgmtL2vpnPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtL2vpnPIR.setStatus("current")
_RuijieMplsVPNMgmtL2vpnAc_ObjectIdentity = ObjectIdentity
ruijieMplsVPNMgmtL2vpnAc = _RuijieMplsVPNMgmtL2vpnAc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 5)
)
_RuijieMplsVPNMgmtL2vpnAcTable_Object = MibTable
ruijieMplsVPNMgmtL2vpnAcTable = _RuijieMplsVPNMgmtL2vpnAcTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtL2vpnAcTable.setStatus("current")
_RuijieMplsVPNMgmtL2vpnAcEntry_Object = MibTableRow
ruijieMplsVPNMgmtL2vpnAcEntry = _RuijieMplsVPNMgmtL2vpnAcEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 5, 1, 1)
)
ruijieMplsVPNMgmtL2vpnAcEntry.setIndexNames(
    (0, "RUIJIE-MPLS-VPN-MGMT-MIB", "ruijieMplsVPNMgmtL2vpnAcRmUID"),
    (0, "RUIJIE-MPLS-VPN-MGMT-MIB", "ruijieMplsVPNMgmtL2vpnAcNermUID"),
    (0, "RUIJIE-MPLS-VPN-MGMT-MIB", "ruijieMplsVPNMgmtL2vpnAcPortrmUID"),
)
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtL2vpnAcEntry.setStatus("current")


class _RuijieMplsVPNMgmtL2vpnAcRmUID_Type(OctetString):
    """Custom type ruijieMplsVPNMgmtL2vpnAcRmUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RuijieMplsVPNMgmtL2vpnAcRmUID_Type.__name__ = "OctetString"
_RuijieMplsVPNMgmtL2vpnAcRmUID_Object = MibTableColumn
ruijieMplsVPNMgmtL2vpnAcRmUID = _RuijieMplsVPNMgmtL2vpnAcRmUID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 5, 1, 1, 1),
    _RuijieMplsVPNMgmtL2vpnAcRmUID_Type()
)
ruijieMplsVPNMgmtL2vpnAcRmUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtL2vpnAcRmUID.setStatus("current")


class _RuijieMplsVPNMgmtL2vpnAcNermUID_Type(OctetString):
    """Custom type ruijieMplsVPNMgmtL2vpnAcNermUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RuijieMplsVPNMgmtL2vpnAcNermUID_Type.__name__ = "OctetString"
_RuijieMplsVPNMgmtL2vpnAcNermUID_Object = MibTableColumn
ruijieMplsVPNMgmtL2vpnAcNermUID = _RuijieMplsVPNMgmtL2vpnAcNermUID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 5, 1, 1, 2),
    _RuijieMplsVPNMgmtL2vpnAcNermUID_Type()
)
ruijieMplsVPNMgmtL2vpnAcNermUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtL2vpnAcNermUID.setStatus("current")


class _RuijieMplsVPNMgmtL2vpnAcPortrmUID_Type(OctetString):
    """Custom type ruijieMplsVPNMgmtL2vpnAcPortrmUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RuijieMplsVPNMgmtL2vpnAcPortrmUID_Type.__name__ = "OctetString"
_RuijieMplsVPNMgmtL2vpnAcPortrmUID_Object = MibTableColumn
ruijieMplsVPNMgmtL2vpnAcPortrmUID = _RuijieMplsVPNMgmtL2vpnAcPortrmUID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 5, 1, 1, 3),
    _RuijieMplsVPNMgmtL2vpnAcPortrmUID_Type()
)
ruijieMplsVPNMgmtL2vpnAcPortrmUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtL2vpnAcPortrmUID.setStatus("current")


class _RuijieMplsVPNMgmtL2vpnAcCvid_Type(OctetString):
    """Custom type ruijieMplsVPNMgmtL2vpnAcCvid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_RuijieMplsVPNMgmtL2vpnAcCvid_Type.__name__ = "OctetString"
_RuijieMplsVPNMgmtL2vpnAcCvid_Object = MibTableColumn
ruijieMplsVPNMgmtL2vpnAcCvid = _RuijieMplsVPNMgmtL2vpnAcCvid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 5, 1, 1, 4),
    _RuijieMplsVPNMgmtL2vpnAcCvid_Type()
)
ruijieMplsVPNMgmtL2vpnAcCvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtL2vpnAcCvid.setStatus("current")


class _RuijieMplsVPNMgmtL2vpnAcSvid_Type(OctetString):
    """Custom type ruijieMplsVPNMgmtL2vpnAcSvid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_RuijieMplsVPNMgmtL2vpnAcSvid_Type.__name__ = "OctetString"
_RuijieMplsVPNMgmtL2vpnAcSvid_Object = MibTableColumn
ruijieMplsVPNMgmtL2vpnAcSvid = _RuijieMplsVPNMgmtL2vpnAcSvid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 5, 1, 1, 5),
    _RuijieMplsVPNMgmtL2vpnAcSvid_Type()
)
ruijieMplsVPNMgmtL2vpnAcSvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtL2vpnAcSvid.setStatus("current")


class _RuijieMplsVPNMgmtL2vpnAcIngCIR_Type(OctetString):
    """Custom type ruijieMplsVPNMgmtL2vpnAcIngCIR based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RuijieMplsVPNMgmtL2vpnAcIngCIR_Type.__name__ = "OctetString"
_RuijieMplsVPNMgmtL2vpnAcIngCIR_Object = MibTableColumn
ruijieMplsVPNMgmtL2vpnAcIngCIR = _RuijieMplsVPNMgmtL2vpnAcIngCIR_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 5, 1, 1, 6),
    _RuijieMplsVPNMgmtL2vpnAcIngCIR_Type()
)
ruijieMplsVPNMgmtL2vpnAcIngCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtL2vpnAcIngCIR.setStatus("current")


class _RuijieMplsVPNMgmtL2vpnAcIngPIR_Type(OctetString):
    """Custom type ruijieMplsVPNMgmtL2vpnAcIngPIR based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RuijieMplsVPNMgmtL2vpnAcIngPIR_Type.__name__ = "OctetString"
_RuijieMplsVPNMgmtL2vpnAcIngPIR_Object = MibTableColumn
ruijieMplsVPNMgmtL2vpnAcIngPIR = _RuijieMplsVPNMgmtL2vpnAcIngPIR_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 5, 1, 1, 7),
    _RuijieMplsVPNMgmtL2vpnAcIngPIR_Type()
)
ruijieMplsVPNMgmtL2vpnAcIngPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtL2vpnAcIngPIR.setStatus("current")


class _RuijieMplsVPNMgmtL2vpnAcEgCIR_Type(OctetString):
    """Custom type ruijieMplsVPNMgmtL2vpnAcEgCIR based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RuijieMplsVPNMgmtL2vpnAcEgCIR_Type.__name__ = "OctetString"
_RuijieMplsVPNMgmtL2vpnAcEgCIR_Object = MibTableColumn
ruijieMplsVPNMgmtL2vpnAcEgCIR = _RuijieMplsVPNMgmtL2vpnAcEgCIR_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 5, 1, 1, 8),
    _RuijieMplsVPNMgmtL2vpnAcEgCIR_Type()
)
ruijieMplsVPNMgmtL2vpnAcEgCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtL2vpnAcEgCIR.setStatus("current")


class _RuijieMplsVPNMgmtL2vpnAcEgPIR_Type(OctetString):
    """Custom type ruijieMplsVPNMgmtL2vpnAcEgPIR based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RuijieMplsVPNMgmtL2vpnAcEgPIR_Type.__name__ = "OctetString"
_RuijieMplsVPNMgmtL2vpnAcEgPIR_Object = MibTableColumn
ruijieMplsVPNMgmtL2vpnAcEgPIR = _RuijieMplsVPNMgmtL2vpnAcEgPIR_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 1, 5, 1, 1, 9),
    _RuijieMplsVPNMgmtL2vpnAcEgPIR_Type()
)
ruijieMplsVPNMgmtL2vpnAcEgPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVPNMgmtL2vpnAcEgPIR.setStatus("current")
_RuijieMplsVPNMgmtMIBConformance_ObjectIdentity = ObjectIdentity
ruijieMplsVPNMgmtMIBConformance = _RuijieMplsVPNMgmtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 122, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-MPLS-VPN-MGMT-MIB",
    **{"ruijieMplsVPNMgmtMIB": ruijieMplsVPNMgmtMIB,
       "ruijieMplsVPNMgmtMIBObjects": ruijieMplsVPNMgmtMIBObjects,
       "ruijieMplsVPNMgmtVrf": ruijieMplsVPNMgmtVrf,
       "ruijieMplsVPNMgmtVrfTable": ruijieMplsVPNMgmtVrfTable,
       "ruijieMplsVPNMgmtVrfEntry": ruijieMplsVPNMgmtVrfEntry,
       "ruijieMplsVPNMgmtVrfName": ruijieMplsVPNMgmtVrfName,
       "ruijieMplsVPNMgmtVrfIntfFault": ruijieMplsVPNMgmtVrfIntfFault,
       "ruijieMplsVPNMgmtVrfVpnId": ruijieMplsVPNMgmtVrfVpnId,
       "ruijieMplsVPNMgmtVrfVpnIdType": ruijieMplsVPNMgmtVrfVpnIdType,
       "ruijieMplsVPNMgmtVrfVpnRunState": ruijieMplsVPNMgmtVrfVpnRunState,
       "ruijieMplsVPNMgmtRoute": ruijieMplsVPNMgmtRoute,
       "ruijieMplsVPNMgmtVrfRteTable": ruijieMplsVPNMgmtVrfRteTable,
       "ruijieMplsVPNMgmtVrfRteEntry": ruijieMplsVPNMgmtVrfRteEntry,
       "ruijieMplsVPNMgmtRteDestType": ruijieMplsVPNMgmtRteDestType,
       "ruijieMplsVPNMgmtRteDest": ruijieMplsVPNMgmtRteDest,
       "ruijieMplsVPNMgmtRtePfxLen": ruijieMplsVPNMgmtRtePfxLen,
       "ruijieMplsVPNMgmtRtePolicy": ruijieMplsVPNMgmtRtePolicy,
       "ruijieMplsVPNMgmtRteNHopType": ruijieMplsVPNMgmtRteNHopType,
       "ruijieMplsVPNMgmtRteNextHop": ruijieMplsVPNMgmtRteNextHop,
       "ruijieMplsVPNMgmtRteDscp": ruijieMplsVPNMgmtRteDscp,
       "ruijieMplsVPNMgmtRteStorageType": ruijieMplsVPNMgmtRteStorageType,
       "ruijieMplsVPNMgmtQos": ruijieMplsVPNMgmtQos,
       "ruijieMplsVPNMgmtQosLSP": ruijieMplsVPNMgmtQosLSP,
       "ruijieMplsVPNMgmtLSPNum": ruijieMplsVPNMgmtLSPNum,
       "ruijieMplsVPNMgmtBackupLSPNum": ruijieMplsVPNMgmtBackupLSPNum,
       "ruijieMplsVPNMgmtLDPLSPNum": ruijieMplsVPNMgmtLDPLSPNum,
       "ruijieMplsVPNMgmtBGPLSPNum": ruijieMplsVPNMgmtBGPLSPNum,
       "ruijieMplsVPNMgmtStaticLSPNum": ruijieMplsVPNMgmtStaticLSPNum,
       "ruijieMplsVPNMgmtCRLDPLSPNum": ruijieMplsVPNMgmtCRLDPLSPNum,
       "ruijieMplsVPNMgmtRsvpLSPNum": ruijieMplsVPNMgmtRsvpLSPNum,
       "ruijieMplsVPNMgmtBFDLSPNum": ruijieMplsVPNMgmtBFDLSPNum,
       "ruijieMplsVPNMgmtOAMLSPNum": ruijieMplsVPNMgmtOAMLSPNum,
       "ruijieMplsVPNMgmtIngressLSPNum": ruijieMplsVPNMgmtIngressLSPNum,
       "ruijieMplsVPNMgmtTransitLSPNum": ruijieMplsVPNMgmtTransitLSPNum,
       "ruijieMplsVPNMgmtEgressLSPNum": ruijieMplsVPNMgmtEgressLSPNum,
       "ruijieMplsVPNMgmtQosFault": ruijieMplsVPNMgmtQosFault,
       "ruijieMplsLSPFaultBFD": ruijieMplsLSPFaultBFD,
       "ruijieMplsLSPFaultOAM": ruijieMplsLSPFaultOAM,
       "ruijieMplsVrfFault": ruijieMplsVrfFault,
       "ruijieMplsPWFault": ruijieMplsPWFault,
       "ruijieMplsVPNMgmtL2vpn": ruijieMplsVPNMgmtL2vpn,
       "ruijieMplsVPNMgmtL2vpnTable": ruijieMplsVPNMgmtL2vpnTable,
       "ruijieMplsVPNMgmtL2vpnEntry": ruijieMplsVPNMgmtL2vpnEntry,
       "ruijieMplsVPNMgmtL2vpnRmUID": ruijieMplsVPNMgmtL2vpnRmUID,
       "ruijieMplsVPNMgmtL2vpnNativeName": ruijieMplsVPNMgmtL2vpnNativeName,
       "ruijieMplsVPNMgmtL2vpnServiceType": ruijieMplsVPNMgmtL2vpnServiceType,
       "ruijieMplsVPNMgmtL2vpnOwner": ruijieMplsVPNMgmtL2vpnOwner,
       "ruijieMplsVPNMgmtL2vpnRunState": ruijieMplsVPNMgmtL2vpnRunState,
       "ruijieMplsVPNMgmtL2vpnCIR": ruijieMplsVPNMgmtL2vpnCIR,
       "ruijieMplsVPNMgmtL2vpnPIR": ruijieMplsVPNMgmtL2vpnPIR,
       "ruijieMplsVPNMgmtL2vpnAc": ruijieMplsVPNMgmtL2vpnAc,
       "ruijieMplsVPNMgmtL2vpnAcTable": ruijieMplsVPNMgmtL2vpnAcTable,
       "ruijieMplsVPNMgmtL2vpnAcEntry": ruijieMplsVPNMgmtL2vpnAcEntry,
       "ruijieMplsVPNMgmtL2vpnAcRmUID": ruijieMplsVPNMgmtL2vpnAcRmUID,
       "ruijieMplsVPNMgmtL2vpnAcNermUID": ruijieMplsVPNMgmtL2vpnAcNermUID,
       "ruijieMplsVPNMgmtL2vpnAcPortrmUID": ruijieMplsVPNMgmtL2vpnAcPortrmUID,
       "ruijieMplsVPNMgmtL2vpnAcCvid": ruijieMplsVPNMgmtL2vpnAcCvid,
       "ruijieMplsVPNMgmtL2vpnAcSvid": ruijieMplsVPNMgmtL2vpnAcSvid,
       "ruijieMplsVPNMgmtL2vpnAcIngCIR": ruijieMplsVPNMgmtL2vpnAcIngCIR,
       "ruijieMplsVPNMgmtL2vpnAcIngPIR": ruijieMplsVPNMgmtL2vpnAcIngPIR,
       "ruijieMplsVPNMgmtL2vpnAcEgCIR": ruijieMplsVPNMgmtL2vpnAcEgCIR,
       "ruijieMplsVPNMgmtL2vpnAcEgPIR": ruijieMplsVPNMgmtL2vpnAcEgPIR,
       "ruijieMplsVPNMgmtMIBConformance": ruijieMplsVPNMgmtMIBConformance}
)
