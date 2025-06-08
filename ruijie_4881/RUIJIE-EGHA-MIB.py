# SNMP MIB module (RUIJIE-EGHA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-EGHA-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:21 2025
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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruijieEghaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139)
)
if mibBuilder.loadTexts:
    ruijieEghaMIB.setRevisions(
        ("2015-06-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieEghaMIBObjects_ObjectIdentity = ObjectIdentity
ruijieEghaMIBObjects = _RuijieEghaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1)
)
_RuijieEghaTopo_ObjectIdentity = ObjectIdentity
ruijieEghaTopo = _RuijieEghaTopo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 1)
)


class _RuijieEghaTopoShape_Type(Integer32):
    """Custom type ruijieEghaTopoShape based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chain", 1),
          ("ring", 2))
    )


_RuijieEghaTopoShape_Type.__name__ = "Integer32"
_RuijieEghaTopoShape_Object = MibScalar
ruijieEghaTopoShape = _RuijieEghaTopoShape_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 1, 1),
    _RuijieEghaTopoShape_Type()
)
ruijieEghaTopoShape.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaTopoShape.setStatus("current")
_RuijieEghaTopoConn_Type = DisplayString
_RuijieEghaTopoConn_Object = MibScalar
ruijieEghaTopoConn = _RuijieEghaTopoConn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 1, 2),
    _RuijieEghaTopoConn_Type()
)
ruijieEghaTopoConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaTopoConn.setStatus("current")
_RuijieEghaDeviceInfo_ObjectIdentity = ObjectIdentity
ruijieEghaDeviceInfo = _RuijieEghaDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 2)
)
_RuijieEghaDomainID_Type = Integer32
_RuijieEghaDomainID_Object = MibScalar
ruijieEghaDomainID = _RuijieEghaDomainID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 2, 1),
    _RuijieEghaDomainID_Type()
)
ruijieEghaDomainID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaDomainID.setStatus("current")
_RuijieEghaDeviceTable_Object = MibTable
ruijieEghaDeviceTable = _RuijieEghaDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ruijieEghaDeviceTable.setStatus("current")
_RuijieEghaDeviceEntry_Object = MibTableRow
ruijieEghaDeviceEntry = _RuijieEghaDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 2, 2, 1)
)
ruijieEghaDeviceEntry.setIndexNames(
    (0, "RUIJIE-EGHA-MIB", "ruijieEghaDeviceID"),
)
if mibBuilder.loadTexts:
    ruijieEghaDeviceEntry.setStatus("current")
_RuijieEghaDeviceID_Type = Integer32
_RuijieEghaDeviceID_Object = MibTableColumn
ruijieEghaDeviceID = _RuijieEghaDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 2, 2, 1, 1),
    _RuijieEghaDeviceID_Type()
)
ruijieEghaDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaDeviceID.setStatus("current")
_RuijieEghaDeviceMac_Type = MacAddress
_RuijieEghaDeviceMac_Object = MibTableColumn
ruijieEghaDeviceMac = _RuijieEghaDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 2, 2, 1, 2),
    _RuijieEghaDeviceMac_Type()
)
ruijieEghaDeviceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaDeviceMac.setStatus("current")
_RuijieEghaDevicePri_Type = Integer32
_RuijieEghaDevicePri_Object = MibTableColumn
ruijieEghaDevicePri = _RuijieEghaDevicePri_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 2, 2, 1, 3),
    _RuijieEghaDevicePri_Type()
)
ruijieEghaDevicePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaDevicePri.setStatus("current")
_RuijieEghaDeviceDescr_Type = DisplayString
_RuijieEghaDeviceDescr_Object = MibTableColumn
ruijieEghaDeviceDescr = _RuijieEghaDeviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 2, 2, 1, 4),
    _RuijieEghaDeviceDescr_Type()
)
ruijieEghaDeviceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaDeviceDescr.setStatus("current")


class _RuijieEghaDeviceStatus_Type(Integer32):
    """Custom type ruijieEghaDeviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("recovery", 2))
    )


_RuijieEghaDeviceStatus_Type.__name__ = "Integer32"
_RuijieEghaDeviceStatus_Object = MibTableColumn
ruijieEghaDeviceStatus = _RuijieEghaDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 2, 2, 1, 5),
    _RuijieEghaDeviceStatus_Type()
)
ruijieEghaDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaDeviceStatus.setStatus("current")


class _RuijieEghaDeviceRole_Type(Integer32):
    """Custom type ruijieEghaDeviceRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2),
          ("candidate", 3))
    )


_RuijieEghaDeviceRole_Type.__name__ = "Integer32"
_RuijieEghaDeviceRole_Object = MibTableColumn
ruijieEghaDeviceRole = _RuijieEghaDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 2, 2, 1, 6),
    _RuijieEghaDeviceRole_Type()
)
ruijieEghaDeviceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaDeviceRole.setStatus("current")
_RuijieEghaLink_ObjectIdentity = ObjectIdentity
ruijieEghaLink = _RuijieEghaLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 3)
)
_RuijieEghaPortTable_Object = MibTable
ruijieEghaPortTable = _RuijieEghaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ruijieEghaPortTable.setStatus("current")
_RuijieEghaPortEntry_Object = MibTableRow
ruijieEghaPortEntry = _RuijieEghaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 3, 1, 1)
)
ruijieEghaPortEntry.setIndexNames(
    (0, "RUIJIE-EGHA-MIB", "ruijieEghaPortIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieEghaPortEntry.setStatus("current")
_RuijieEghaPortIfIndex_Type = Integer32
_RuijieEghaPortIfIndex_Object = MibTableColumn
ruijieEghaPortIfIndex = _RuijieEghaPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 3, 1, 1, 1),
    _RuijieEghaPortIfIndex_Type()
)
ruijieEghaPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaPortIfIndex.setStatus("current")
_RuijieEghaApIf_Type = DisplayString
_RuijieEghaApIf_Object = MibTableColumn
ruijieEghaApIf = _RuijieEghaApIf_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 3, 1, 1, 2),
    _RuijieEghaApIf_Type()
)
ruijieEghaApIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaApIf.setStatus("current")


class _RuijieEghaPortState_Type(Integer32):
    """Custom type ruijieEghaPortState based on Integer32"""
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
        *(("down", 1),
          ("up", 2),
          ("ok", 3),
          ("disable", 4),
          ("aged", 5))
    )


_RuijieEghaPortState_Type.__name__ = "Integer32"
_RuijieEghaPortState_Object = MibTableColumn
ruijieEghaPortState = _RuijieEghaPortState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 3, 1, 1, 3),
    _RuijieEghaPortState_Type()
)
ruijieEghaPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaPortState.setStatus("current")
_RuijieEghaPortPeerIfIndex_Type = Integer32
_RuijieEghaPortPeerIfIndex_Object = MibTableColumn
ruijieEghaPortPeerIfIndex = _RuijieEghaPortPeerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 3, 1, 1, 4),
    _RuijieEghaPortPeerIfIndex_Type()
)
ruijieEghaPortPeerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaPortPeerIfIndex.setStatus("current")
_RuijieEghaApTable_Object = MibTable
ruijieEghaApTable = _RuijieEghaApTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ruijieEghaApTable.setStatus("current")
_RuijieEghaApEntry_Object = MibTableRow
ruijieEghaApEntry = _RuijieEghaApEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 3, 2, 1)
)
ruijieEghaApEntry.setIndexNames(
    (0, "RUIJIE-EGHA-MIB", "ruijieEghaApIndex"),
)
if mibBuilder.loadTexts:
    ruijieEghaApEntry.setStatus("current")
_RuijieEghaApIndex_Type = Integer32
_RuijieEghaApIndex_Object = MibTableColumn
ruijieEghaApIndex = _RuijieEghaApIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 3, 2, 1, 1),
    _RuijieEghaApIndex_Type()
)
ruijieEghaApIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaApIndex.setStatus("current")
_RuijieEghaApUptime_Type = DisplayString
_RuijieEghaApUptime_Object = MibTableColumn
ruijieEghaApUptime = _RuijieEghaApUptime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 3, 2, 1, 2),
    _RuijieEghaApUptime_Type()
)
ruijieEghaApUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaApUptime.setStatus("current")
_RuijieEghaDad_ObjectIdentity = ObjectIdentity
ruijieEghaDad = _RuijieEghaDad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 4)
)
_RuijieEghaDadExIntfTable_Object = MibTable
ruijieEghaDadExIntfTable = _RuijieEghaDadExIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ruijieEghaDadExIntfTable.setStatus("current")
_RuijieEghaDadExIntfEntry_Object = MibTableRow
ruijieEghaDadExIntfEntry = _RuijieEghaDadExIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 4, 1, 1)
)
ruijieEghaDadExIntfEntry.setIndexNames(
    (0, "RUIJIE-EGHA-MIB", "ruijieEghaDadExIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieEghaDadExIntfEntry.setStatus("current")
_RuijieEghaDadExIfIndex_Type = Integer32
_RuijieEghaDadExIfIndex_Object = MibTableColumn
ruijieEghaDadExIfIndex = _RuijieEghaDadExIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 4, 1, 1, 1),
    _RuijieEghaDadExIfIndex_Type()
)
ruijieEghaDadExIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaDadExIfIndex.setStatus("current")
_RuijieEghaDadAP_ObjectIdentity = ObjectIdentity
ruijieEghaDadAP = _RuijieEghaDadAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 4, 2)
)


class _RuijieEghaDadAPEnable_Type(Integer32):
    """Custom type ruijieEghaDadAPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_RuijieEghaDadAPEnable_Type.__name__ = "Integer32"
_RuijieEghaDadAPEnable_Object = MibScalar
ruijieEghaDadAPEnable = _RuijieEghaDadAPEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 4, 2, 1),
    _RuijieEghaDadAPEnable_Type()
)
ruijieEghaDadAPEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaDadAPEnable.setStatus("current")
_RuijieEghaDadAPIfIndex_Type = Integer32
_RuijieEghaDadAPIfIndex_Object = MibScalar
ruijieEghaDadAPIfIndex = _RuijieEghaDadAPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 4, 2, 2),
    _RuijieEghaDadAPIfIndex_Type()
)
ruijieEghaDadAPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaDadAPIfIndex.setStatus("current")


class _RuijieEghaDadAPIfStatus_Type(Integer32):
    """Custom type ruijieEghaDadAPIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_RuijieEghaDadAPIfStatus_Type.__name__ = "Integer32"
_RuijieEghaDadAPIfStatus_Object = MibScalar
ruijieEghaDadAPIfStatus = _RuijieEghaDadAPIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 4, 2, 3),
    _RuijieEghaDadAPIfStatus_Type()
)
ruijieEghaDadAPIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaDadAPIfStatus.setStatus("current")
_RuijieEghaDadAPMemberIfTable_Object = MibTable
ruijieEghaDadAPMemberIfTable = _RuijieEghaDadAPMemberIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 4, 2, 4)
)
if mibBuilder.loadTexts:
    ruijieEghaDadAPMemberIfTable.setStatus("current")
_RuijieEghaDadAPMemberIfEntry_Object = MibTableRow
ruijieEghaDadAPMemberIfEntry = _RuijieEghaDadAPMemberIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 4, 2, 4, 1)
)
ruijieEghaDadAPMemberIfEntry.setIndexNames(
    (0, "RUIJIE-EGHA-MIB", "ruijieEghaDadAPMemberIfindex"),
)
if mibBuilder.loadTexts:
    ruijieEghaDadAPMemberIfEntry.setStatus("current")
_RuijieEghaDadAPMemberIfindex_Type = Integer32
_RuijieEghaDadAPMemberIfindex_Object = MibTableColumn
ruijieEghaDadAPMemberIfindex = _RuijieEghaDadAPMemberIfindex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 4, 2, 4, 1, 1),
    _RuijieEghaDadAPMemberIfindex_Type()
)
ruijieEghaDadAPMemberIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaDadAPMemberIfindex.setStatus("current")


class _RuijieEghaDadAPMemberIfStatus_Type(Integer32):
    """Custom type ruijieEghaDadAPMemberIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_RuijieEghaDadAPMemberIfStatus_Type.__name__ = "Integer32"
_RuijieEghaDadAPMemberIfStatus_Object = MibTableColumn
ruijieEghaDadAPMemberIfStatus = _RuijieEghaDadAPMemberIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 4, 2, 4, 1, 2),
    _RuijieEghaDadAPMemberIfStatus_Type()
)
ruijieEghaDadAPMemberIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaDadAPMemberIfStatus.setStatus("current")
_RuijieEghaDadAPRelayIfTable_Object = MibTable
ruijieEghaDadAPRelayIfTable = _RuijieEghaDadAPRelayIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 4, 2, 5)
)
if mibBuilder.loadTexts:
    ruijieEghaDadAPRelayIfTable.setStatus("current")
_RuijieEghaDadAPRelayIfEntry_Object = MibTableRow
ruijieEghaDadAPRelayIfEntry = _RuijieEghaDadAPRelayIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 4, 2, 5, 1)
)
ruijieEghaDadAPRelayIfEntry.setIndexNames(
    (0, "RUIJIE-EGHA-MIB", "ruijieEghaDadAPRelayIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieEghaDadAPRelayIfEntry.setStatus("current")
_RuijieEghaDadAPRelayIfIndex_Type = Integer32
_RuijieEghaDadAPRelayIfIndex_Object = MibTableColumn
ruijieEghaDadAPRelayIfIndex = _RuijieEghaDadAPRelayIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 4, 2, 5, 1, 1),
    _RuijieEghaDadAPRelayIfIndex_Type()
)
ruijieEghaDadAPRelayIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaDadAPRelayIfIndex.setStatus("current")
_RuijieEghaDadBFD_ObjectIdentity = ObjectIdentity
ruijieEghaDadBFD = _RuijieEghaDadBFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 4, 3)
)


class _RuijieEghaDadBFDEnable_Type(Integer32):
    """Custom type ruijieEghaDadBFDEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_RuijieEghaDadBFDEnable_Type.__name__ = "Integer32"
_RuijieEghaDadBFDEnable_Object = MibScalar
ruijieEghaDadBFDEnable = _RuijieEghaDadBFDEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 4, 3, 1),
    _RuijieEghaDadBFDEnable_Type()
)
ruijieEghaDadBFDEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaDadBFDEnable.setStatus("current")
_RuijieEghaDadBFDIfTable_Object = MibTable
ruijieEghaDadBFDIfTable = _RuijieEghaDadBFDIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    ruijieEghaDadBFDIfTable.setStatus("current")
_RuijieEghaDadBFDIfEntry_Object = MibTableRow
ruijieEghaDadBFDIfEntry = _RuijieEghaDadBFDIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 4, 3, 2, 1)
)
ruijieEghaDadBFDIfEntry.setIndexNames(
    (0, "RUIJIE-EGHA-MIB", "ruijieEghaDadBFDIfIndex1"),
    (0, "RUIJIE-EGHA-MIB", "ruijieEghaDadBFDIfIndex2"),
)
if mibBuilder.loadTexts:
    ruijieEghaDadBFDIfEntry.setStatus("current")
_RuijieEghaDadBFDIfIndex1_Type = Integer32
_RuijieEghaDadBFDIfIndex1_Object = MibTableColumn
ruijieEghaDadBFDIfIndex1 = _RuijieEghaDadBFDIfIndex1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 4, 3, 2, 1, 1),
    _RuijieEghaDadBFDIfIndex1_Type()
)
ruijieEghaDadBFDIfIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaDadBFDIfIndex1.setStatus("current")
_RuijieEghaDadBFDIfIndex2_Type = Integer32
_RuijieEghaDadBFDIfIndex2_Object = MibTableColumn
ruijieEghaDadBFDIfIndex2 = _RuijieEghaDadBFDIfIndex2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 4, 3, 2, 1, 2),
    _RuijieEghaDadBFDIfIndex2_Type()
)
ruijieEghaDadBFDIfIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaDadBFDIfIndex2.setStatus("current")


class _RuijieEghaDadBFDIfStatus_Type(Integer32):
    """Custom type ruijieEghaDadBFDIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_RuijieEghaDadBFDIfStatus_Type.__name__ = "Integer32"
_RuijieEghaDadBFDIfStatus_Object = MibTableColumn
ruijieEghaDadBFDIfStatus = _RuijieEghaDadBFDIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 4, 3, 2, 1, 3),
    _RuijieEghaDadBFDIfStatus_Type()
)
ruijieEghaDadBFDIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaDadBFDIfStatus.setStatus("current")
_RuijieEghaForward_ObjectIdentity = ObjectIdentity
ruijieEghaForward = _RuijieEghaForward_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 5)
)


class _RuijieEghaForwardApllf_Type(Integer32):
    """Custom type ruijieEghaForwardApllf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_RuijieEghaForwardApllf_Type.__name__ = "Integer32"
_RuijieEghaForwardApllf_Object = MibScalar
ruijieEghaForwardApllf = _RuijieEghaForwardApllf_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 5, 1),
    _RuijieEghaForwardApllf_Type()
)
ruijieEghaForwardApllf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaForwardApllf.setStatus("current")


class _RuijieEghaForwardEcmpllf_Type(Integer32):
    """Custom type ruijieEghaForwardEcmpllf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_RuijieEghaForwardEcmpllf_Type.__name__ = "Integer32"
_RuijieEghaForwardEcmpllf_Object = MibScalar
ruijieEghaForwardEcmpllf = _RuijieEghaForwardEcmpllf_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 5, 2),
    _RuijieEghaForwardEcmpllf_Type()
)
ruijieEghaForwardEcmpllf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaForwardEcmpllf.setStatus("current")
_RuijieEghaVersion_Type = DisplayString
_RuijieEghaVersion_Object = MibScalar
ruijieEghaVersion = _RuijieEghaVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 1, 6),
    _RuijieEghaVersion_Type()
)
ruijieEghaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEghaVersion.setStatus("current")
_RuijieEghaMIBTraps_ObjectIdentity = ObjectIdentity
ruijieEghaMIBTraps = _RuijieEghaMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 2)
)
_RuijieEghaTrapsNtfObjects_ObjectIdentity = ObjectIdentity
ruijieEghaTrapsNtfObjects = _RuijieEghaTrapsNtfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 2, 1)
)


class _RuijieEghaDeviceState_Type(Integer32):
    """Custom type ruijieEghaDeviceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("plugin", 1),
          ("remove", 2))
    )


_RuijieEghaDeviceState_Type.__name__ = "Integer32"
_RuijieEghaDeviceState_Object = MibScalar
ruijieEghaDeviceState = _RuijieEghaDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 2, 1, 1),
    _RuijieEghaDeviceState_Type()
)
ruijieEghaDeviceState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieEghaDeviceState.setStatus("current")
_RuijieEghaSlotID_Type = Integer32
_RuijieEghaSlotID_Object = MibScalar
ruijieEghaSlotID = _RuijieEghaSlotID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 2, 1, 2),
    _RuijieEghaSlotID_Type()
)
ruijieEghaSlotID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieEghaSlotID.setStatus("current")


class _RuijieEghaDadResult_Type(Integer32):
    """Custom type ruijieEghaDadResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("bad", 2))
    )


_RuijieEghaDadResult_Type.__name__ = "Integer32"
_RuijieEghaDadResult_Object = MibScalar
ruijieEghaDadResult = _RuijieEghaDadResult_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 2, 1, 3),
    _RuijieEghaDadResult_Type()
)
ruijieEghaDadResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieEghaDadResult.setStatus("current")
_RuijieEghaTrapsNotifications_ObjectIdentity = ObjectIdentity
ruijieEghaTrapsNotifications = _RuijieEghaTrapsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 2, 2)
)
_RuijieEghaMIBConformance_ObjectIdentity = ObjectIdentity
ruijieEghaMIBConformance = _RuijieEghaMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 3)
)
_RuijieEghaMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieEghaMIBCompliances = _RuijieEghaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 3, 1)
)
_RuijieEghaMIBGroups_ObjectIdentity = ObjectIdentity
ruijieEghaMIBGroups = _RuijieEghaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 3, 2)
)

# Managed Objects groups

ruijieEghaMIBObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 3, 2, 1)
)
ruijieEghaMIBObjectsGroup.setObjects(
      *(("RUIJIE-EGHA-MIB", "ruijieEghaTopoShape"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaTopoConn"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaDomainID"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaDeviceID"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaDeviceMac"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaDevicePri"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaDeviceDescr"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaDeviceStatus"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaDeviceRole"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaPortIfIndex"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaApIf"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaPortState"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaPortPeerIfIndex"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaApUptime"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaDadExIfIndex"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaDadAPEnable"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaDadAPIfIndex"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaDadAPIfStatus"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaDadAPMemberIfindex"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaDadAPMemberIfStatus"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaDadAPRelayIfIndex"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaDadBFDEnable"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaDadBFDIfIndex1"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaDadBFDIfIndex2"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaDadBFDIfStatus"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaForwardApllf"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaForwardEcmpllf"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaVersion"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaDeviceState"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaSlotID"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaDadResult"))
)
if mibBuilder.loadTexts:
    ruijieEghaMIBObjectsGroup.setStatus("current")


# Notification objects

ruijieEghaNotifyTopoChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 2, 2, 1)
)
ruijieEghaNotifyTopoChange.setObjects(
    ("RUIJIE-EGHA-MIB", "ruijieEghaTopoShape")
)
if mibBuilder.loadTexts:
    ruijieEghaNotifyTopoChange.setStatus(
        "current"
    )

ruijieEghaNotifyDeviceChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 2, 2, 2)
)
ruijieEghaNotifyDeviceChange.setObjects(
      *(("RUIJIE-EGHA-MIB", "ruijieEghaDeviceID"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaDeviceState"))
)
if mibBuilder.loadTexts:
    ruijieEghaNotifyDeviceChange.setStatus(
        "current"
    )

ruijieEghaNotifyDeviceRoleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 2, 2, 3)
)
ruijieEghaNotifyDeviceRoleChange.setObjects(
      *(("RUIJIE-EGHA-MIB", "ruijieEghaDeviceID"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaSlotID"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaDeviceRole"))
)
if mibBuilder.loadTexts:
    ruijieEghaNotifyDeviceRoleChange.setStatus(
        "current"
    )

ruijieEghaNotifyDad = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 2, 2, 4)
)
ruijieEghaNotifyDad.setObjects(
    ("RUIJIE-EGHA-MIB", "ruijieEghaDadResult")
)
if mibBuilder.loadTexts:
    ruijieEghaNotifyDad.setStatus(
        "current"
    )


# Notifications groups

ruijieEghaMIBTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 3, 2, 2)
)
ruijieEghaMIBTrapsGroup.setObjects(
      *(("RUIJIE-EGHA-MIB", "ruijieEghaNotifyTopoChange"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaNotifyDeviceChange"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaNotifyDeviceRoleChange"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaNotifyDad"))
)
if mibBuilder.loadTexts:
    ruijieEghaMIBTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ruijieEghaMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 139, 3, 1, 1)
)
ruijieEghaMIBCompliance.setObjects(
      *(("RUIJIE-EGHA-MIB", "ruijieEghaMIBObjectsGroup"),
        ("RUIJIE-EGHA-MIB", "ruijieEghaMIBTrapsGroup"))
)
if mibBuilder.loadTexts:
    ruijieEghaMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-EGHA-MIB",
    **{"ruijieEghaMIB": ruijieEghaMIB,
       "ruijieEghaMIBObjects": ruijieEghaMIBObjects,
       "ruijieEghaTopo": ruijieEghaTopo,
       "ruijieEghaTopoShape": ruijieEghaTopoShape,
       "ruijieEghaTopoConn": ruijieEghaTopoConn,
       "ruijieEghaDeviceInfo": ruijieEghaDeviceInfo,
       "ruijieEghaDomainID": ruijieEghaDomainID,
       "ruijieEghaDeviceTable": ruijieEghaDeviceTable,
       "ruijieEghaDeviceEntry": ruijieEghaDeviceEntry,
       "ruijieEghaDeviceID": ruijieEghaDeviceID,
       "ruijieEghaDeviceMac": ruijieEghaDeviceMac,
       "ruijieEghaDevicePri": ruijieEghaDevicePri,
       "ruijieEghaDeviceDescr": ruijieEghaDeviceDescr,
       "ruijieEghaDeviceStatus": ruijieEghaDeviceStatus,
       "ruijieEghaDeviceRole": ruijieEghaDeviceRole,
       "ruijieEghaLink": ruijieEghaLink,
       "ruijieEghaPortTable": ruijieEghaPortTable,
       "ruijieEghaPortEntry": ruijieEghaPortEntry,
       "ruijieEghaPortIfIndex": ruijieEghaPortIfIndex,
       "ruijieEghaApIf": ruijieEghaApIf,
       "ruijieEghaPortState": ruijieEghaPortState,
       "ruijieEghaPortPeerIfIndex": ruijieEghaPortPeerIfIndex,
       "ruijieEghaApTable": ruijieEghaApTable,
       "ruijieEghaApEntry": ruijieEghaApEntry,
       "ruijieEghaApIndex": ruijieEghaApIndex,
       "ruijieEghaApUptime": ruijieEghaApUptime,
       "ruijieEghaDad": ruijieEghaDad,
       "ruijieEghaDadExIntfTable": ruijieEghaDadExIntfTable,
       "ruijieEghaDadExIntfEntry": ruijieEghaDadExIntfEntry,
       "ruijieEghaDadExIfIndex": ruijieEghaDadExIfIndex,
       "ruijieEghaDadAP": ruijieEghaDadAP,
       "ruijieEghaDadAPEnable": ruijieEghaDadAPEnable,
       "ruijieEghaDadAPIfIndex": ruijieEghaDadAPIfIndex,
       "ruijieEghaDadAPIfStatus": ruijieEghaDadAPIfStatus,
       "ruijieEghaDadAPMemberIfTable": ruijieEghaDadAPMemberIfTable,
       "ruijieEghaDadAPMemberIfEntry": ruijieEghaDadAPMemberIfEntry,
       "ruijieEghaDadAPMemberIfindex": ruijieEghaDadAPMemberIfindex,
       "ruijieEghaDadAPMemberIfStatus": ruijieEghaDadAPMemberIfStatus,
       "ruijieEghaDadAPRelayIfTable": ruijieEghaDadAPRelayIfTable,
       "ruijieEghaDadAPRelayIfEntry": ruijieEghaDadAPRelayIfEntry,
       "ruijieEghaDadAPRelayIfIndex": ruijieEghaDadAPRelayIfIndex,
       "ruijieEghaDadBFD": ruijieEghaDadBFD,
       "ruijieEghaDadBFDEnable": ruijieEghaDadBFDEnable,
       "ruijieEghaDadBFDIfTable": ruijieEghaDadBFDIfTable,
       "ruijieEghaDadBFDIfEntry": ruijieEghaDadBFDIfEntry,
       "ruijieEghaDadBFDIfIndex1": ruijieEghaDadBFDIfIndex1,
       "ruijieEghaDadBFDIfIndex2": ruijieEghaDadBFDIfIndex2,
       "ruijieEghaDadBFDIfStatus": ruijieEghaDadBFDIfStatus,
       "ruijieEghaForward": ruijieEghaForward,
       "ruijieEghaForwardApllf": ruijieEghaForwardApllf,
       "ruijieEghaForwardEcmpllf": ruijieEghaForwardEcmpllf,
       "ruijieEghaVersion": ruijieEghaVersion,
       "ruijieEghaMIBTraps": ruijieEghaMIBTraps,
       "ruijieEghaTrapsNtfObjects": ruijieEghaTrapsNtfObjects,
       "ruijieEghaDeviceState": ruijieEghaDeviceState,
       "ruijieEghaSlotID": ruijieEghaSlotID,
       "ruijieEghaDadResult": ruijieEghaDadResult,
       "ruijieEghaTrapsNotifications": ruijieEghaTrapsNotifications,
       "ruijieEghaNotifyTopoChange": ruijieEghaNotifyTopoChange,
       "ruijieEghaNotifyDeviceChange": ruijieEghaNotifyDeviceChange,
       "ruijieEghaNotifyDeviceRoleChange": ruijieEghaNotifyDeviceRoleChange,
       "ruijieEghaNotifyDad": ruijieEghaNotifyDad,
       "ruijieEghaMIBConformance": ruijieEghaMIBConformance,
       "ruijieEghaMIBCompliances": ruijieEghaMIBCompliances,
       "ruijieEghaMIBCompliance": ruijieEghaMIBCompliance,
       "ruijieEghaMIBGroups": ruijieEghaMIBGroups,
       "ruijieEghaMIBObjectsGroup": ruijieEghaMIBObjectsGroup,
       "ruijieEghaMIBTrapsGroup": ruijieEghaMIBTrapsGroup}
)
