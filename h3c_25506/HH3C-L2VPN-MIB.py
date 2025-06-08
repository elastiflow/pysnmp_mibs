# SNMP MIB module (HH3C-L2VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/h3c_25506/HH3C-L2VPN-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:38:10 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cL2vpn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162)
)
if mibBuilder.loadTexts:
    hh3cL2vpn.setRevisions(
        ("2015-01-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cL2vpnPwNotifications_ObjectIdentity = ObjectIdentity
hh3cL2vpnPwNotifications = _Hh3cL2vpnPwNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 0)
)
_Hh3cL2vpnGlobalTable_ObjectIdentity = ObjectIdentity
hh3cL2vpnGlobalTable = _Hh3cL2vpnGlobalTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2)
)
_Hh3cL2vpnPwcTable_Object = MibTable
hh3cL2vpnPwcTable = _Hh3cL2vpnPwcTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cL2vpnPwcTable.setStatus("current")
_Hh3cL2vpnPwcEntry_Object = MibTableRow
hh3cL2vpnPwcEntry = _Hh3cL2vpnPwcEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2, 1, 1)
)
hh3cL2vpnPwcEntry.setIndexNames(
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnPwcName"),
)
if mibBuilder.loadTexts:
    hh3cL2vpnPwcEntry.setStatus("current")


class _Hh3cL2vpnPwcName_Type(OctetString):
    """Custom type hh3cL2vpnPwcName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_Hh3cL2vpnPwcName_Type.__name__ = "OctetString"
_Hh3cL2vpnPwcName_Object = MibTableColumn
hh3cL2vpnPwcName = _Hh3cL2vpnPwcName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2, 1, 1, 1),
    _Hh3cL2vpnPwcName_Type()
)
hh3cL2vpnPwcName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cL2vpnPwcName.setStatus("current")


class _Hh3cL2vpnPwcCvType_Type(Integer32):
    """Custom type hh3cL2vpnPwcCvType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("bfd", 2),
          ("rawBFD", 3))
    )


_Hh3cL2vpnPwcCvType_Type.__name__ = "Integer32"
_Hh3cL2vpnPwcCvType_Object = MibTableColumn
hh3cL2vpnPwcCvType = _Hh3cL2vpnPwcCvType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2, 1, 1, 2),
    _Hh3cL2vpnPwcCvType_Type()
)
hh3cL2vpnPwcCvType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnPwcCvType.setStatus("current")


class _Hh3cL2vpnPwcCcType_Type(Integer32):
    """Custom type hh3cL2vpnPwcCcType based on Integer32"""
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
        *(("unknown", 1),
          ("controlWord", 2),
          ("routerAlert", 3),
          ("ttl", 4))
    )


_Hh3cL2vpnPwcCcType_Type.__name__ = "Integer32"
_Hh3cL2vpnPwcCcType_Object = MibTableColumn
hh3cL2vpnPwcCcType = _Hh3cL2vpnPwcCcType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2, 1, 1, 3),
    _Hh3cL2vpnPwcCcType_Type()
)
hh3cL2vpnPwcCcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnPwcCcType.setStatus("current")


class _Hh3cL2vpnPwcControlWord_Type(TruthValue):
    """Custom type hh3cL2vpnPwcControlWord based on TruthValue"""
    defaultValue = 2


_Hh3cL2vpnPwcControlWord_Type.__name__ = "TruthValue"
_Hh3cL2vpnPwcControlWord_Object = MibTableColumn
hh3cL2vpnPwcControlWord = _Hh3cL2vpnPwcControlWord_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2, 1, 1, 4),
    _Hh3cL2vpnPwcControlWord_Type()
)
hh3cL2vpnPwcControlWord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnPwcControlWord.setStatus("current")


class _Hh3cL2vpnPwcPwType_Type(Integer32):
    """Custom type hh3cL2vpnPwcPwType based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("vlan", 4),
          ("ethernet", 5))
    )


_Hh3cL2vpnPwcPwType_Type.__name__ = "Integer32"
_Hh3cL2vpnPwcPwType_Object = MibTableColumn
hh3cL2vpnPwcPwType = _Hh3cL2vpnPwcPwType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2, 1, 1, 5),
    _Hh3cL2vpnPwcPwType_Type()
)
hh3cL2vpnPwcPwType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnPwcPwType.setStatus("current")
_Hh3cL2vpnPwcRowStatus_Type = RowStatus
_Hh3cL2vpnPwcRowStatus_Object = MibTableColumn
hh3cL2vpnPwcRowStatus = _Hh3cL2vpnPwcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 2, 1, 1, 6),
    _Hh3cL2vpnPwcRowStatus_Type()
)
hh3cL2vpnPwcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnPwcRowStatus.setStatus("current")
_Hh3cL2vpnVpwsTable_ObjectIdentity = ObjectIdentity
hh3cL2vpnVpwsTable = _Hh3cL2vpnVpwsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3)
)
_Hh3cL2vpnXcgTable_Object = MibTable
hh3cL2vpnXcgTable = _Hh3cL2vpnXcgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cL2vpnXcgTable.setStatus("current")
_Hh3cL2vpnXcgEntry_Object = MibTableRow
hh3cL2vpnXcgEntry = _Hh3cL2vpnXcgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 1, 1)
)
hh3cL2vpnXcgEntry.setIndexNames(
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnXcgName"),
)
if mibBuilder.loadTexts:
    hh3cL2vpnXcgEntry.setStatus("current")


class _Hh3cL2vpnXcgName_Type(OctetString):
    """Custom type hh3cL2vpnXcgName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cL2vpnXcgName_Type.__name__ = "OctetString"
_Hh3cL2vpnXcgName_Object = MibTableColumn
hh3cL2vpnXcgName = _Hh3cL2vpnXcgName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 1, 1, 1),
    _Hh3cL2vpnXcgName_Type()
)
hh3cL2vpnXcgName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgName.setStatus("current")


class _Hh3cL2vpnXcgAdminState_Type(Integer32):
    """Custom type hh3cL2vpnXcgAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminUp", 1),
          ("adminDown", 2))
    )


_Hh3cL2vpnXcgAdminState_Type.__name__ = "Integer32"
_Hh3cL2vpnXcgAdminState_Object = MibTableColumn
hh3cL2vpnXcgAdminState = _Hh3cL2vpnXcgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 1, 1, 2),
    _Hh3cL2vpnXcgAdminState_Type()
)
hh3cL2vpnXcgAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgAdminState.setStatus("current")
_Hh3cL2vpnXcgRowStatus_Type = RowStatus
_Hh3cL2vpnXcgRowStatus_Object = MibTableColumn
hh3cL2vpnXcgRowStatus = _Hh3cL2vpnXcgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 1, 1, 3),
    _Hh3cL2vpnXcgRowStatus_Type()
)
hh3cL2vpnXcgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgRowStatus.setStatus("current")
_Hh3cL2vpnXcgConnTable_Object = MibTable
hh3cL2vpnXcgConnTable = _Hh3cL2vpnXcgConnTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cL2vpnXcgConnTable.setStatus("current")
_Hh3cL2vpnXcgConnEntry_Object = MibTableRow
hh3cL2vpnXcgConnEntry = _Hh3cL2vpnXcgConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 2, 1)
)
hh3cL2vpnXcgConnEntry.setIndexNames(
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnXcgName"),
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnXcgConnName"),
)
if mibBuilder.loadTexts:
    hh3cL2vpnXcgConnEntry.setStatus("current")


class _Hh3cL2vpnXcgConnName_Type(OctetString):
    """Custom type hh3cL2vpnXcgConnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Hh3cL2vpnXcgConnName_Type.__name__ = "OctetString"
_Hh3cL2vpnXcgConnName_Object = MibTableColumn
hh3cL2vpnXcgConnName = _Hh3cL2vpnXcgConnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 2, 1, 1),
    _Hh3cL2vpnXcgConnName_Type()
)
hh3cL2vpnXcgConnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgConnName.setStatus("current")
_Hh3cL2vpnXcgConnRowStatus_Type = RowStatus
_Hh3cL2vpnXcgConnRowStatus_Object = MibTableColumn
hh3cL2vpnXcgConnRowStatus = _Hh3cL2vpnXcgConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 2, 1, 2),
    _Hh3cL2vpnXcgConnRowStatus_Type()
)
hh3cL2vpnXcgConnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgConnRowStatus.setStatus("current")
_Hh3cL2vpnXcgAcTable_Object = MibTable
hh3cL2vpnXcgAcTable = _Hh3cL2vpnXcgAcTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 3)
)
if mibBuilder.loadTexts:
    hh3cL2vpnXcgAcTable.setStatus("current")
_Hh3cL2vpnXcgAcEntry_Object = MibTableRow
hh3cL2vpnXcgAcEntry = _Hh3cL2vpnXcgAcEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 3, 1)
)
hh3cL2vpnXcgAcEntry.setIndexNames(
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnXcgName"),
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnXcgConnName"),
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnXcgAcIfIndex"),
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnXcgAcEvcSrvInstId"),
)
if mibBuilder.loadTexts:
    hh3cL2vpnXcgAcEntry.setStatus("current")
_Hh3cL2vpnXcgAcIfIndex_Type = InterfaceIndex
_Hh3cL2vpnXcgAcIfIndex_Object = MibTableColumn
hh3cL2vpnXcgAcIfIndex = _Hh3cL2vpnXcgAcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 3, 1, 1),
    _Hh3cL2vpnXcgAcIfIndex_Type()
)
hh3cL2vpnXcgAcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgAcIfIndex.setStatus("current")
_Hh3cL2vpnXcgAcEvcSrvInstId_Type = Unsigned32
_Hh3cL2vpnXcgAcEvcSrvInstId_Object = MibTableColumn
hh3cL2vpnXcgAcEvcSrvInstId = _Hh3cL2vpnXcgAcEvcSrvInstId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 3, 1, 2),
    _Hh3cL2vpnXcgAcEvcSrvInstId_Type()
)
hh3cL2vpnXcgAcEvcSrvInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgAcEvcSrvInstId.setStatus("current")


class _Hh3cL2vpnXcgAcAccessMode_Type(Integer32):
    """Custom type hh3cL2vpnXcgAcAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlan", 1),
          ("ethernet", 2))
    )


_Hh3cL2vpnXcgAcAccessMode_Type.__name__ = "Integer32"
_Hh3cL2vpnXcgAcAccessMode_Object = MibTableColumn
hh3cL2vpnXcgAcAccessMode = _Hh3cL2vpnXcgAcAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 3, 1, 3),
    _Hh3cL2vpnXcgAcAccessMode_Type()
)
hh3cL2vpnXcgAcAccessMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgAcAccessMode.setStatus("current")
_Hh3cL2vpnXcgAcRowStatus_Type = RowStatus
_Hh3cL2vpnXcgAcRowStatus_Object = MibTableColumn
hh3cL2vpnXcgAcRowStatus = _Hh3cL2vpnXcgAcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 3, 1, 4),
    _Hh3cL2vpnXcgAcRowStatus_Type()
)
hh3cL2vpnXcgAcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgAcRowStatus.setStatus("current")
_Hh3cL2vpnXcgPwTable_Object = MibTable
hh3cL2vpnXcgPwTable = _Hh3cL2vpnXcgPwTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 4)
)
if mibBuilder.loadTexts:
    hh3cL2vpnXcgPwTable.setStatus("current")
_Hh3cL2vpnXcgPwEntry_Object = MibTableRow
hh3cL2vpnXcgPwEntry = _Hh3cL2vpnXcgPwEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 4, 1)
)
hh3cL2vpnXcgPwEntry.setIndexNames(
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnXcgName"),
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnXcgConnName"),
    (0, "HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwIndex"),
)
if mibBuilder.loadTexts:
    hh3cL2vpnXcgPwEntry.setStatus("current")
_Hh3cL2vpnXcgPwIndex_Type = Unsigned32
_Hh3cL2vpnXcgPwIndex_Object = MibTableColumn
hh3cL2vpnXcgPwIndex = _Hh3cL2vpnXcgPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 4, 1, 1),
    _Hh3cL2vpnXcgPwIndex_Type()
)
hh3cL2vpnXcgPwIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgPwIndex.setStatus("current")


class _Hh3cL2vpnXcgPwCfgType_Type(Integer32):
    """Custom type hh3cL2vpnXcgPwCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("backup", 2))
    )


_Hh3cL2vpnXcgPwCfgType_Type.__name__ = "Integer32"
_Hh3cL2vpnXcgPwCfgType_Object = MibTableColumn
hh3cL2vpnXcgPwCfgType = _Hh3cL2vpnXcgPwCfgType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 4, 1, 2),
    _Hh3cL2vpnXcgPwCfgType_Type()
)
hh3cL2vpnXcgPwCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgPwCfgType.setStatus("current")


class _Hh3cL2vpnXcgPwClassName_Type(OctetString):
    """Custom type hh3cL2vpnXcgPwClassName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_Hh3cL2vpnXcgPwClassName_Type.__name__ = "OctetString"
_Hh3cL2vpnXcgPwClassName_Object = MibTableColumn
hh3cL2vpnXcgPwClassName = _Hh3cL2vpnXcgPwClassName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 4, 1, 3),
    _Hh3cL2vpnXcgPwClassName_Type()
)
hh3cL2vpnXcgPwClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgPwClassName.setStatus("current")


class _Hh3cL2vpnXcgPwTunnelPolicy_Type(OctetString):
    """Custom type hh3cL2vpnXcgPwTunnelPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_Hh3cL2vpnXcgPwTunnelPolicy_Type.__name__ = "OctetString"
_Hh3cL2vpnXcgPwTunnelPolicy_Object = MibTableColumn
hh3cL2vpnXcgPwTunnelPolicy = _Hh3cL2vpnXcgPwTunnelPolicy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 4, 1, 4),
    _Hh3cL2vpnXcgPwTunnelPolicy_Type()
)
hh3cL2vpnXcgPwTunnelPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgPwTunnelPolicy.setStatus("current")
_Hh3cL2vpnXcgPwPeerIp_Type = IpAddress
_Hh3cL2vpnXcgPwPeerIp_Object = MibTableColumn
hh3cL2vpnXcgPwPeerIp = _Hh3cL2vpnXcgPwPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 4, 1, 5),
    _Hh3cL2vpnXcgPwPeerIp_Type()
)
hh3cL2vpnXcgPwPeerIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgPwPeerIp.setStatus("current")
_Hh3cL2vpnXcgPwPwID_Type = Unsigned32
_Hh3cL2vpnXcgPwPwID_Object = MibTableColumn
hh3cL2vpnXcgPwPwID = _Hh3cL2vpnXcgPwPwID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 4, 1, 6),
    _Hh3cL2vpnXcgPwPwID_Type()
)
hh3cL2vpnXcgPwPwID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgPwPwID.setStatus("current")
_Hh3cL2vpnXcgPwRowStatus_Type = RowStatus
_Hh3cL2vpnXcgPwRowStatus_Object = MibTableColumn
hh3cL2vpnXcgPwRowStatus = _Hh3cL2vpnXcgPwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 3, 4, 1, 7),
    _Hh3cL2vpnXcgPwRowStatus_Type()
)
hh3cL2vpnXcgPwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL2vpnXcgPwRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cL2vpnPwSwitchPtoB = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 0, 1)
)
hh3cL2vpnPwSwitchPtoB.setObjects(
      *(("HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwIndex"),
        ("HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwPeerIp"),
        ("HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwPwID"),
        ("HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwIndex"),
        ("HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwPeerIp"),
        ("HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwPwID"))
)
if mibBuilder.loadTexts:
    hh3cL2vpnPwSwitchPtoB.setStatus(
        "current"
    )

hh3cL2vpnPwSwitchBtoP = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162, 0, 2)
)
hh3cL2vpnPwSwitchBtoP.setObjects(
      *(("HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwIndex"),
        ("HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwPeerIp"),
        ("HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwPwID"),
        ("HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwIndex"),
        ("HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwPeerIp"),
        ("HH3C-L2VPN-MIB", "hh3cL2vpnXcgPwPwID"))
)
if mibBuilder.loadTexts:
    hh3cL2vpnPwSwitchBtoP.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-L2VPN-MIB",
    **{"hh3cL2vpn": hh3cL2vpn,
       "hh3cL2vpnPwNotifications": hh3cL2vpnPwNotifications,
       "hh3cL2vpnPwSwitchPtoB": hh3cL2vpnPwSwitchPtoB,
       "hh3cL2vpnPwSwitchBtoP": hh3cL2vpnPwSwitchBtoP,
       "hh3cL2vpnGlobalTable": hh3cL2vpnGlobalTable,
       "hh3cL2vpnPwcTable": hh3cL2vpnPwcTable,
       "hh3cL2vpnPwcEntry": hh3cL2vpnPwcEntry,
       "hh3cL2vpnPwcName": hh3cL2vpnPwcName,
       "hh3cL2vpnPwcCvType": hh3cL2vpnPwcCvType,
       "hh3cL2vpnPwcCcType": hh3cL2vpnPwcCcType,
       "hh3cL2vpnPwcControlWord": hh3cL2vpnPwcControlWord,
       "hh3cL2vpnPwcPwType": hh3cL2vpnPwcPwType,
       "hh3cL2vpnPwcRowStatus": hh3cL2vpnPwcRowStatus,
       "hh3cL2vpnVpwsTable": hh3cL2vpnVpwsTable,
       "hh3cL2vpnXcgTable": hh3cL2vpnXcgTable,
       "hh3cL2vpnXcgEntry": hh3cL2vpnXcgEntry,
       "hh3cL2vpnXcgName": hh3cL2vpnXcgName,
       "hh3cL2vpnXcgAdminState": hh3cL2vpnXcgAdminState,
       "hh3cL2vpnXcgRowStatus": hh3cL2vpnXcgRowStatus,
       "hh3cL2vpnXcgConnTable": hh3cL2vpnXcgConnTable,
       "hh3cL2vpnXcgConnEntry": hh3cL2vpnXcgConnEntry,
       "hh3cL2vpnXcgConnName": hh3cL2vpnXcgConnName,
       "hh3cL2vpnXcgConnRowStatus": hh3cL2vpnXcgConnRowStatus,
       "hh3cL2vpnXcgAcTable": hh3cL2vpnXcgAcTable,
       "hh3cL2vpnXcgAcEntry": hh3cL2vpnXcgAcEntry,
       "hh3cL2vpnXcgAcIfIndex": hh3cL2vpnXcgAcIfIndex,
       "hh3cL2vpnXcgAcEvcSrvInstId": hh3cL2vpnXcgAcEvcSrvInstId,
       "hh3cL2vpnXcgAcAccessMode": hh3cL2vpnXcgAcAccessMode,
       "hh3cL2vpnXcgAcRowStatus": hh3cL2vpnXcgAcRowStatus,
       "hh3cL2vpnXcgPwTable": hh3cL2vpnXcgPwTable,
       "hh3cL2vpnXcgPwEntry": hh3cL2vpnXcgPwEntry,
       "hh3cL2vpnXcgPwIndex": hh3cL2vpnXcgPwIndex,
       "hh3cL2vpnXcgPwCfgType": hh3cL2vpnXcgPwCfgType,
       "hh3cL2vpnXcgPwClassName": hh3cL2vpnXcgPwClassName,
       "hh3cL2vpnXcgPwTunnelPolicy": hh3cL2vpnXcgPwTunnelPolicy,
       "hh3cL2vpnXcgPwPeerIp": hh3cL2vpnXcgPwPeerIp,
       "hh3cL2vpnXcgPwPwID": hh3cL2vpnXcgPwPwID,
       "hh3cL2vpnXcgPwRowStatus": hh3cL2vpnXcgPwRowStatus}
)
