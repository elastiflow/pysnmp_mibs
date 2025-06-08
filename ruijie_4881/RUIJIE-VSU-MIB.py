# SNMP MIB module (RUIJIE-VSU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-VSU-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:00 2025
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

ruijieVsuMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102)
)
if mibBuilder.loadTexts:
    ruijieVsuMIB.setRevisions(
        ("2011-06-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieVsuMIBObjects_ObjectIdentity = ObjectIdentity
ruijieVsuMIBObjects = _RuijieVsuMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1)
)
_RuijieVsuTopo_ObjectIdentity = ObjectIdentity
ruijieVsuTopo = _RuijieVsuTopo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 1)
)


class _RuijieVsuTopoShape_Type(Integer32):
    """Custom type ruijieVsuTopoShape based on Integer32"""
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


_RuijieVsuTopoShape_Type.__name__ = "Integer32"
_RuijieVsuTopoShape_Object = MibScalar
ruijieVsuTopoShape = _RuijieVsuTopoShape_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 1, 1),
    _RuijieVsuTopoShape_Type()
)
ruijieVsuTopoShape.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuTopoShape.setStatus("current")
_RuijieVsuTopoConn_Type = DisplayString
_RuijieVsuTopoConn_Object = MibScalar
ruijieVsuTopoConn = _RuijieVsuTopoConn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 1, 2),
    _RuijieVsuTopoConn_Type()
)
ruijieVsuTopoConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuTopoConn.setStatus("current")
_RuijieVsuDeviceInfo_ObjectIdentity = ObjectIdentity
ruijieVsuDeviceInfo = _RuijieVsuDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 2)
)
_RuijieVsuDomainID_Type = Integer32
_RuijieVsuDomainID_Object = MibScalar
ruijieVsuDomainID = _RuijieVsuDomainID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 2, 1),
    _RuijieVsuDomainID_Type()
)
ruijieVsuDomainID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuDomainID.setStatus("current")
_RuijieVsuDeviceTable_Object = MibTable
ruijieVsuDeviceTable = _RuijieVsuDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ruijieVsuDeviceTable.setStatus("current")
_RuijieVsuDeviceEntry_Object = MibTableRow
ruijieVsuDeviceEntry = _RuijieVsuDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 2, 2, 1)
)
ruijieVsuDeviceEntry.setIndexNames(
    (0, "RUIJIE-VSU-MIB", "ruijieVsuDeviceID"),
)
if mibBuilder.loadTexts:
    ruijieVsuDeviceEntry.setStatus("current")
_RuijieVsuDeviceID_Type = Integer32
_RuijieVsuDeviceID_Object = MibTableColumn
ruijieVsuDeviceID = _RuijieVsuDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 2, 2, 1, 1),
    _RuijieVsuDeviceID_Type()
)
ruijieVsuDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuDeviceID.setStatus("current")
_RuijieVsuDeviceMac_Type = MacAddress
_RuijieVsuDeviceMac_Object = MibTableColumn
ruijieVsuDeviceMac = _RuijieVsuDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 2, 2, 1, 2),
    _RuijieVsuDeviceMac_Type()
)
ruijieVsuDeviceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuDeviceMac.setStatus("current")
_RuijieVsuDevicePri_Type = Integer32
_RuijieVsuDevicePri_Object = MibTableColumn
ruijieVsuDevicePri = _RuijieVsuDevicePri_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 2, 2, 1, 3),
    _RuijieVsuDevicePri_Type()
)
ruijieVsuDevicePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuDevicePri.setStatus("current")
_RuijieVsuDeviceDescr_Type = DisplayString
_RuijieVsuDeviceDescr_Object = MibTableColumn
ruijieVsuDeviceDescr = _RuijieVsuDeviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 2, 2, 1, 4),
    _RuijieVsuDeviceDescr_Type()
)
ruijieVsuDeviceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuDeviceDescr.setStatus("current")


class _RuijieVsuDeviceStatus_Type(Integer32):
    """Custom type ruijieVsuDeviceStatus based on Integer32"""
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


_RuijieVsuDeviceStatus_Type.__name__ = "Integer32"
_RuijieVsuDeviceStatus_Object = MibTableColumn
ruijieVsuDeviceStatus = _RuijieVsuDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 2, 2, 1, 5),
    _RuijieVsuDeviceStatus_Type()
)
ruijieVsuDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuDeviceStatus.setStatus("current")


class _RuijieVsuDeviceRole_Type(Integer32):
    """Custom type ruijieVsuDeviceRole based on Integer32"""
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


_RuijieVsuDeviceRole_Type.__name__ = "Integer32"
_RuijieVsuDeviceRole_Object = MibTableColumn
ruijieVsuDeviceRole = _RuijieVsuDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 2, 2, 1, 6),
    _RuijieVsuDeviceRole_Type()
)
ruijieVsuDeviceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuDeviceRole.setStatus("current")
_RuijieVsuVsl_ObjectIdentity = ObjectIdentity
ruijieVsuVsl = _RuijieVsuVsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 3)
)
_RuijieVsuVslPortTable_Object = MibTable
ruijieVsuVslPortTable = _RuijieVsuVslPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ruijieVsuVslPortTable.setStatus("current")
_RuijieVsuVslPortEntry_Object = MibTableRow
ruijieVsuVslPortEntry = _RuijieVsuVslPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 3, 1, 1)
)
ruijieVsuVslPortEntry.setIndexNames(
    (0, "RUIJIE-VSU-MIB", "ruijieVsuVslPortIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieVsuVslPortEntry.setStatus("current")
_RuijieVsuVslPortIfIndex_Type = Integer32
_RuijieVsuVslPortIfIndex_Object = MibTableColumn
ruijieVsuVslPortIfIndex = _RuijieVsuVslPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 3, 1, 1, 1),
    _RuijieVsuVslPortIfIndex_Type()
)
ruijieVsuVslPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuVslPortIfIndex.setStatus("current")
_RuijieVsuVslApIf_Type = DisplayString
_RuijieVsuVslApIf_Object = MibTableColumn
ruijieVsuVslApIf = _RuijieVsuVslApIf_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 3, 1, 1, 2),
    _RuijieVsuVslApIf_Type()
)
ruijieVsuVslApIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuVslApIf.setStatus("current")


class _RuijieVsuVslPortState_Type(Integer32):
    """Custom type ruijieVsuVslPortState based on Integer32"""
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


_RuijieVsuVslPortState_Type.__name__ = "Integer32"
_RuijieVsuVslPortState_Object = MibTableColumn
ruijieVsuVslPortState = _RuijieVsuVslPortState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 3, 1, 1, 3),
    _RuijieVsuVslPortState_Type()
)
ruijieVsuVslPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuVslPortState.setStatus("current")
_RuijieVsuVslPortPeerIfIndex_Type = Integer32
_RuijieVsuVslPortPeerIfIndex_Object = MibTableColumn
ruijieVsuVslPortPeerIfIndex = _RuijieVsuVslPortPeerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 3, 1, 1, 4),
    _RuijieVsuVslPortPeerIfIndex_Type()
)
ruijieVsuVslPortPeerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuVslPortPeerIfIndex.setStatus("current")
_RuijieVsuVslTable_Object = MibTable
ruijieVsuVslTable = _RuijieVsuVslTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ruijieVsuVslTable.setStatus("current")
_RuijieVsuVslEntry_Object = MibTableRow
ruijieVsuVslEntry = _RuijieVsuVslEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 3, 2, 1)
)
ruijieVsuVslEntry.setIndexNames(
    (0, "RUIJIE-VSU-MIB", "ruijieVsuVslApIndex"),
)
if mibBuilder.loadTexts:
    ruijieVsuVslEntry.setStatus("current")
_RuijieVsuVslApIndex_Type = Integer32
_RuijieVsuVslApIndex_Object = MibTableColumn
ruijieVsuVslApIndex = _RuijieVsuVslApIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 3, 2, 1, 1),
    _RuijieVsuVslApIndex_Type()
)
ruijieVsuVslApIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuVslApIndex.setStatus("current")
_RuijieVsuVslApUptime_Type = DisplayString
_RuijieVsuVslApUptime_Object = MibTableColumn
ruijieVsuVslApUptime = _RuijieVsuVslApUptime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 3, 2, 1, 2),
    _RuijieVsuVslApUptime_Type()
)
ruijieVsuVslApUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuVslApUptime.setStatus("current")
_RuijieVsuDad_ObjectIdentity = ObjectIdentity
ruijieVsuDad = _RuijieVsuDad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 4)
)
_RuijieVsuDadExIntfTable_Object = MibTable
ruijieVsuDadExIntfTable = _RuijieVsuDadExIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ruijieVsuDadExIntfTable.setStatus("current")
_RuijieVsuDadExIntfEntry_Object = MibTableRow
ruijieVsuDadExIntfEntry = _RuijieVsuDadExIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 4, 1, 1)
)
ruijieVsuDadExIntfEntry.setIndexNames(
    (0, "RUIJIE-VSU-MIB", "ruijieVsuDadExIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieVsuDadExIntfEntry.setStatus("current")
_RuijieVsuDadExIfIndex_Type = Integer32
_RuijieVsuDadExIfIndex_Object = MibTableColumn
ruijieVsuDadExIfIndex = _RuijieVsuDadExIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 4, 1, 1, 1),
    _RuijieVsuDadExIfIndex_Type()
)
ruijieVsuDadExIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuDadExIfIndex.setStatus("current")
_RuijieVsuDadAP_ObjectIdentity = ObjectIdentity
ruijieVsuDadAP = _RuijieVsuDadAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 4, 2)
)


class _RuijieVsuDadAPEnable_Type(Integer32):
    """Custom type ruijieVsuDadAPEnable based on Integer32"""
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


_RuijieVsuDadAPEnable_Type.__name__ = "Integer32"
_RuijieVsuDadAPEnable_Object = MibScalar
ruijieVsuDadAPEnable = _RuijieVsuDadAPEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 4, 2, 1),
    _RuijieVsuDadAPEnable_Type()
)
ruijieVsuDadAPEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuDadAPEnable.setStatus("current")
_RuijieVsuDadAPIfIndex_Type = Integer32
_RuijieVsuDadAPIfIndex_Object = MibScalar
ruijieVsuDadAPIfIndex = _RuijieVsuDadAPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 4, 2, 2),
    _RuijieVsuDadAPIfIndex_Type()
)
ruijieVsuDadAPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuDadAPIfIndex.setStatus("current")


class _RuijieVsuDadAPIfStatus_Type(Integer32):
    """Custom type ruijieVsuDadAPIfStatus based on Integer32"""
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


_RuijieVsuDadAPIfStatus_Type.__name__ = "Integer32"
_RuijieVsuDadAPIfStatus_Object = MibScalar
ruijieVsuDadAPIfStatus = _RuijieVsuDadAPIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 4, 2, 3),
    _RuijieVsuDadAPIfStatus_Type()
)
ruijieVsuDadAPIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuDadAPIfStatus.setStatus("current")
_RuijieVsuDadAPMemberIfTable_Object = MibTable
ruijieVsuDadAPMemberIfTable = _RuijieVsuDadAPMemberIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 4, 2, 4)
)
if mibBuilder.loadTexts:
    ruijieVsuDadAPMemberIfTable.setStatus("current")
_RuijieVsuDadAPMemberIfEntry_Object = MibTableRow
ruijieVsuDadAPMemberIfEntry = _RuijieVsuDadAPMemberIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 4, 2, 4, 1)
)
ruijieVsuDadAPMemberIfEntry.setIndexNames(
    (0, "RUIJIE-VSU-MIB", "ruijieVsuDadAPMemberIfindex"),
)
if mibBuilder.loadTexts:
    ruijieVsuDadAPMemberIfEntry.setStatus("current")
_RuijieVsuDadAPMemberIfindex_Type = Integer32
_RuijieVsuDadAPMemberIfindex_Object = MibTableColumn
ruijieVsuDadAPMemberIfindex = _RuijieVsuDadAPMemberIfindex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 4, 2, 4, 1, 1),
    _RuijieVsuDadAPMemberIfindex_Type()
)
ruijieVsuDadAPMemberIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuDadAPMemberIfindex.setStatus("current")


class _RuijieVsuDadAPMemberIfStatus_Type(Integer32):
    """Custom type ruijieVsuDadAPMemberIfStatus based on Integer32"""
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


_RuijieVsuDadAPMemberIfStatus_Type.__name__ = "Integer32"
_RuijieVsuDadAPMemberIfStatus_Object = MibTableColumn
ruijieVsuDadAPMemberIfStatus = _RuijieVsuDadAPMemberIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 4, 2, 4, 1, 2),
    _RuijieVsuDadAPMemberIfStatus_Type()
)
ruijieVsuDadAPMemberIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuDadAPMemberIfStatus.setStatus("current")
_RuijieVsuDadAPRelayIfTable_Object = MibTable
ruijieVsuDadAPRelayIfTable = _RuijieVsuDadAPRelayIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 4, 2, 5)
)
if mibBuilder.loadTexts:
    ruijieVsuDadAPRelayIfTable.setStatus("current")
_RuijieVsuDadAPRelayIfEntry_Object = MibTableRow
ruijieVsuDadAPRelayIfEntry = _RuijieVsuDadAPRelayIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 4, 2, 5, 1)
)
ruijieVsuDadAPRelayIfEntry.setIndexNames(
    (0, "RUIJIE-VSU-MIB", "ruijieVsuDadAPRelayIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieVsuDadAPRelayIfEntry.setStatus("current")
_RuijieVsuDadAPRelayIfIndex_Type = Integer32
_RuijieVsuDadAPRelayIfIndex_Object = MibTableColumn
ruijieVsuDadAPRelayIfIndex = _RuijieVsuDadAPRelayIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 4, 2, 5, 1, 1),
    _RuijieVsuDadAPRelayIfIndex_Type()
)
ruijieVsuDadAPRelayIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuDadAPRelayIfIndex.setStatus("current")
_RuijieVsuDadBFD_ObjectIdentity = ObjectIdentity
ruijieVsuDadBFD = _RuijieVsuDadBFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 4, 3)
)


class _RuijieVsuDadBFDEnable_Type(Integer32):
    """Custom type ruijieVsuDadBFDEnable based on Integer32"""
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


_RuijieVsuDadBFDEnable_Type.__name__ = "Integer32"
_RuijieVsuDadBFDEnable_Object = MibScalar
ruijieVsuDadBFDEnable = _RuijieVsuDadBFDEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 4, 3, 1),
    _RuijieVsuDadBFDEnable_Type()
)
ruijieVsuDadBFDEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuDadBFDEnable.setStatus("current")
_RuijieVsuDadBFDIfTable_Object = MibTable
ruijieVsuDadBFDIfTable = _RuijieVsuDadBFDIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    ruijieVsuDadBFDIfTable.setStatus("current")
_RuijieVsuDadBFDIfEntry_Object = MibTableRow
ruijieVsuDadBFDIfEntry = _RuijieVsuDadBFDIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 4, 3, 2, 1)
)
ruijieVsuDadBFDIfEntry.setIndexNames(
    (0, "RUIJIE-VSU-MIB", "ruijieVsuDadBFDIfIndex1"),
    (0, "RUIJIE-VSU-MIB", "ruijieVsuDadBFDIfIndex2"),
)
if mibBuilder.loadTexts:
    ruijieVsuDadBFDIfEntry.setStatus("current")
_RuijieVsuDadBFDIfIndex1_Type = Integer32
_RuijieVsuDadBFDIfIndex1_Object = MibTableColumn
ruijieVsuDadBFDIfIndex1 = _RuijieVsuDadBFDIfIndex1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 4, 3, 2, 1, 1),
    _RuijieVsuDadBFDIfIndex1_Type()
)
ruijieVsuDadBFDIfIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuDadBFDIfIndex1.setStatus("current")
_RuijieVsuDadBFDIfIndex2_Type = Integer32
_RuijieVsuDadBFDIfIndex2_Object = MibTableColumn
ruijieVsuDadBFDIfIndex2 = _RuijieVsuDadBFDIfIndex2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 4, 3, 2, 1, 2),
    _RuijieVsuDadBFDIfIndex2_Type()
)
ruijieVsuDadBFDIfIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuDadBFDIfIndex2.setStatus("current")


class _RuijieVsuDadBFDIfStatus_Type(Integer32):
    """Custom type ruijieVsuDadBFDIfStatus based on Integer32"""
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


_RuijieVsuDadBFDIfStatus_Type.__name__ = "Integer32"
_RuijieVsuDadBFDIfStatus_Object = MibTableColumn
ruijieVsuDadBFDIfStatus = _RuijieVsuDadBFDIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 4, 3, 2, 1, 3),
    _RuijieVsuDadBFDIfStatus_Type()
)
ruijieVsuDadBFDIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuDadBFDIfStatus.setStatus("current")
_RuijieVsuForward_ObjectIdentity = ObjectIdentity
ruijieVsuForward = _RuijieVsuForward_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 5)
)


class _RuijieVsuForwardApllf_Type(Integer32):
    """Custom type ruijieVsuForwardApllf based on Integer32"""
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


_RuijieVsuForwardApllf_Type.__name__ = "Integer32"
_RuijieVsuForwardApllf_Object = MibScalar
ruijieVsuForwardApllf = _RuijieVsuForwardApllf_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 5, 1),
    _RuijieVsuForwardApllf_Type()
)
ruijieVsuForwardApllf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuForwardApllf.setStatus("current")


class _RuijieVsuForwardEcmpllf_Type(Integer32):
    """Custom type ruijieVsuForwardEcmpllf based on Integer32"""
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


_RuijieVsuForwardEcmpllf_Type.__name__ = "Integer32"
_RuijieVsuForwardEcmpllf_Object = MibScalar
ruijieVsuForwardEcmpllf = _RuijieVsuForwardEcmpllf_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 5, 2),
    _RuijieVsuForwardEcmpllf_Type()
)
ruijieVsuForwardEcmpllf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuForwardEcmpllf.setStatus("current")
_RuijieVsuVersion_Type = DisplayString
_RuijieVsuVersion_Object = MibScalar
ruijieVsuVersion = _RuijieVsuVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 1, 6),
    _RuijieVsuVersion_Type()
)
ruijieVsuVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVsuVersion.setStatus("current")
_RuijieVsuMIBTraps_ObjectIdentity = ObjectIdentity
ruijieVsuMIBTraps = _RuijieVsuMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 2)
)
_RuijieVsuTrapsNtfObjects_ObjectIdentity = ObjectIdentity
ruijieVsuTrapsNtfObjects = _RuijieVsuTrapsNtfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 2, 1)
)


class _RuijieVsuDeviceState_Type(Integer32):
    """Custom type ruijieVsuDeviceState based on Integer32"""
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


_RuijieVsuDeviceState_Type.__name__ = "Integer32"
_RuijieVsuDeviceState_Object = MibScalar
ruijieVsuDeviceState = _RuijieVsuDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 2, 1, 1),
    _RuijieVsuDeviceState_Type()
)
ruijieVsuDeviceState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieVsuDeviceState.setStatus("current")


class _RuijieVsuSlotID_Type(Integer32):
    """Custom type ruijieVsuSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("M1", 30),
          ("M2", 31))
    )


_RuijieVsuSlotID_Type.__name__ = "Integer32"
_RuijieVsuSlotID_Object = MibScalar
ruijieVsuSlotID = _RuijieVsuSlotID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 2, 1, 2),
    _RuijieVsuSlotID_Type()
)
ruijieVsuSlotID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieVsuSlotID.setStatus("current")


class _RuijieVsuDadResult_Type(Integer32):
    """Custom type ruijieVsuDadResult based on Integer32"""
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


_RuijieVsuDadResult_Type.__name__ = "Integer32"
_RuijieVsuDadResult_Object = MibScalar
ruijieVsuDadResult = _RuijieVsuDadResult_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 2, 1, 3),
    _RuijieVsuDadResult_Type()
)
ruijieVsuDadResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieVsuDadResult.setStatus("current")
_RuijieVsuTrapsNotifications_ObjectIdentity = ObjectIdentity
ruijieVsuTrapsNotifications = _RuijieVsuTrapsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 2, 2)
)
_RuijieVsuMIBConformance_ObjectIdentity = ObjectIdentity
ruijieVsuMIBConformance = _RuijieVsuMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 3)
)
_RuijieVsuMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieVsuMIBCompliances = _RuijieVsuMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 3, 1)
)
_RuijieVsuMIBGroups_ObjectIdentity = ObjectIdentity
ruijieVsuMIBGroups = _RuijieVsuMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 3, 2)
)

# Managed Objects groups

ruijieVsuMIBObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 3, 2, 1)
)
ruijieVsuMIBObjectsGroup.setObjects(
      *(("RUIJIE-VSU-MIB", "ruijieVsuTopoShape"),
        ("RUIJIE-VSU-MIB", "ruijieVsuTopoConn"),
        ("RUIJIE-VSU-MIB", "ruijieVsuDomainID"),
        ("RUIJIE-VSU-MIB", "ruijieVsuDeviceID"),
        ("RUIJIE-VSU-MIB", "ruijieVsuDeviceMac"),
        ("RUIJIE-VSU-MIB", "ruijieVsuDevicePri"),
        ("RUIJIE-VSU-MIB", "ruijieVsuDeviceDescr"),
        ("RUIJIE-VSU-MIB", "ruijieVsuDeviceStatus"),
        ("RUIJIE-VSU-MIB", "ruijieVsuDeviceRole"),
        ("RUIJIE-VSU-MIB", "ruijieVsuVslPortIfIndex"),
        ("RUIJIE-VSU-MIB", "ruijieVsuVslApIf"),
        ("RUIJIE-VSU-MIB", "ruijieVsuVslPortState"),
        ("RUIJIE-VSU-MIB", "ruijieVsuVslPortPeerIfIndex"),
        ("RUIJIE-VSU-MIB", "ruijieVsuVslApUptime"),
        ("RUIJIE-VSU-MIB", "ruijieVsuDadExIfIndex"),
        ("RUIJIE-VSU-MIB", "ruijieVsuDadAPEnable"),
        ("RUIJIE-VSU-MIB", "ruijieVsuDadAPIfIndex"),
        ("RUIJIE-VSU-MIB", "ruijieVsuDadAPIfStatus"),
        ("RUIJIE-VSU-MIB", "ruijieVsuDadAPMemberIfindex"),
        ("RUIJIE-VSU-MIB", "ruijieVsuDadAPMemberIfStatus"),
        ("RUIJIE-VSU-MIB", "ruijieVsuDadAPRelayIfIndex"),
        ("RUIJIE-VSU-MIB", "ruijieVsuDadBFDEnable"),
        ("RUIJIE-VSU-MIB", "ruijieVsuDadBFDIfIndex1"),
        ("RUIJIE-VSU-MIB", "ruijieVsuDadBFDIfIndex2"),
        ("RUIJIE-VSU-MIB", "ruijieVsuDadBFDIfStatus"),
        ("RUIJIE-VSU-MIB", "ruijieVsuForwardApllf"),
        ("RUIJIE-VSU-MIB", "ruijieVsuForwardEcmpllf"),
        ("RUIJIE-VSU-MIB", "ruijieVsuVersion"),
        ("RUIJIE-VSU-MIB", "ruijieVsuDeviceState"),
        ("RUIJIE-VSU-MIB", "ruijieVsuSlotID"),
        ("RUIJIE-VSU-MIB", "ruijieVsuDadResult"))
)
if mibBuilder.loadTexts:
    ruijieVsuMIBObjectsGroup.setStatus("current")


# Notification objects

ruijieVsuNotifyTopoChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 2, 2, 1)
)
ruijieVsuNotifyTopoChange.setObjects(
    ("RUIJIE-VSU-MIB", "ruijieVsuTopoShape")
)
if mibBuilder.loadTexts:
    ruijieVsuNotifyTopoChange.setStatus(
        "current"
    )

ruijieVsuNotifyDeviceChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 2, 2, 2)
)
ruijieVsuNotifyDeviceChange.setObjects(
      *(("RUIJIE-VSU-MIB", "ruijieVsuDeviceID"),
        ("RUIJIE-VSU-MIB", "ruijieVsuDeviceState"))
)
if mibBuilder.loadTexts:
    ruijieVsuNotifyDeviceChange.setStatus(
        "current"
    )

ruijieVsuNotifyDeviceRoleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 2, 2, 3)
)
ruijieVsuNotifyDeviceRoleChange.setObjects(
      *(("RUIJIE-VSU-MIB", "ruijieVsuDeviceID"),
        ("RUIJIE-VSU-MIB", "ruijieVsuSlotID"),
        ("RUIJIE-VSU-MIB", "ruijieVsuDeviceRole"))
)
if mibBuilder.loadTexts:
    ruijieVsuNotifyDeviceRoleChange.setStatus(
        "current"
    )

ruijieVsuNotifyDad = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 2, 2, 4)
)
ruijieVsuNotifyDad.setObjects(
    ("RUIJIE-VSU-MIB", "ruijieVsuDadResult")
)
if mibBuilder.loadTexts:
    ruijieVsuNotifyDad.setStatus(
        "current"
    )

ruijieVsuNotifyDeviceJoin = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 2, 2, 5)
)
ruijieVsuNotifyDeviceJoin.setObjects(
    ("RUIJIE-VSU-MIB", "ruijieVsuDeviceID")
)
if mibBuilder.loadTexts:
    ruijieVsuNotifyDeviceJoin.setStatus(
        "current"
    )

ruijieVsuNotifyDeviceLeave = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 2, 2, 6)
)
ruijieVsuNotifyDeviceLeave.setObjects(
    ("RUIJIE-VSU-MIB", "ruijieVsuDeviceID")
)
if mibBuilder.loadTexts:
    ruijieVsuNotifyDeviceLeave.setStatus(
        "current"
    )


# Notifications groups

ruijieVsuMIBTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 3, 2, 2)
)
ruijieVsuMIBTrapsGroup.setObjects(
      *(("RUIJIE-VSU-MIB", "ruijieVsuNotifyTopoChange"),
        ("RUIJIE-VSU-MIB", "ruijieVsuNotifyDeviceChange"),
        ("RUIJIE-VSU-MIB", "ruijieVsuNotifyDeviceRoleChange"),
        ("RUIJIE-VSU-MIB", "ruijieVsuNotifyDad"),
        ("RUIJIE-VSU-MIB", "ruijieVsuNotifyDeviceJoin"),
        ("RUIJIE-VSU-MIB", "ruijieVsuNotifyDeviceLeave"))
)
if mibBuilder.loadTexts:
    ruijieVsuMIBTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ruijieVsuMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 102, 3, 1, 1)
)
ruijieVsuMIBCompliance.setObjects(
      *(("RUIJIE-VSU-MIB", "ruijieVsuMIBObjectsGroup"),
        ("RUIJIE-VSU-MIB", "ruijieVsuMIBTrapsGroup"))
)
if mibBuilder.loadTexts:
    ruijieVsuMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-VSU-MIB",
    **{"ruijieVsuMIB": ruijieVsuMIB,
       "ruijieVsuMIBObjects": ruijieVsuMIBObjects,
       "ruijieVsuTopo": ruijieVsuTopo,
       "ruijieVsuTopoShape": ruijieVsuTopoShape,
       "ruijieVsuTopoConn": ruijieVsuTopoConn,
       "ruijieVsuDeviceInfo": ruijieVsuDeviceInfo,
       "ruijieVsuDomainID": ruijieVsuDomainID,
       "ruijieVsuDeviceTable": ruijieVsuDeviceTable,
       "ruijieVsuDeviceEntry": ruijieVsuDeviceEntry,
       "ruijieVsuDeviceID": ruijieVsuDeviceID,
       "ruijieVsuDeviceMac": ruijieVsuDeviceMac,
       "ruijieVsuDevicePri": ruijieVsuDevicePri,
       "ruijieVsuDeviceDescr": ruijieVsuDeviceDescr,
       "ruijieVsuDeviceStatus": ruijieVsuDeviceStatus,
       "ruijieVsuDeviceRole": ruijieVsuDeviceRole,
       "ruijieVsuVsl": ruijieVsuVsl,
       "ruijieVsuVslPortTable": ruijieVsuVslPortTable,
       "ruijieVsuVslPortEntry": ruijieVsuVslPortEntry,
       "ruijieVsuVslPortIfIndex": ruijieVsuVslPortIfIndex,
       "ruijieVsuVslApIf": ruijieVsuVslApIf,
       "ruijieVsuVslPortState": ruijieVsuVslPortState,
       "ruijieVsuVslPortPeerIfIndex": ruijieVsuVslPortPeerIfIndex,
       "ruijieVsuVslTable": ruijieVsuVslTable,
       "ruijieVsuVslEntry": ruijieVsuVslEntry,
       "ruijieVsuVslApIndex": ruijieVsuVslApIndex,
       "ruijieVsuVslApUptime": ruijieVsuVslApUptime,
       "ruijieVsuDad": ruijieVsuDad,
       "ruijieVsuDadExIntfTable": ruijieVsuDadExIntfTable,
       "ruijieVsuDadExIntfEntry": ruijieVsuDadExIntfEntry,
       "ruijieVsuDadExIfIndex": ruijieVsuDadExIfIndex,
       "ruijieVsuDadAP": ruijieVsuDadAP,
       "ruijieVsuDadAPEnable": ruijieVsuDadAPEnable,
       "ruijieVsuDadAPIfIndex": ruijieVsuDadAPIfIndex,
       "ruijieVsuDadAPIfStatus": ruijieVsuDadAPIfStatus,
       "ruijieVsuDadAPMemberIfTable": ruijieVsuDadAPMemberIfTable,
       "ruijieVsuDadAPMemberIfEntry": ruijieVsuDadAPMemberIfEntry,
       "ruijieVsuDadAPMemberIfindex": ruijieVsuDadAPMemberIfindex,
       "ruijieVsuDadAPMemberIfStatus": ruijieVsuDadAPMemberIfStatus,
       "ruijieVsuDadAPRelayIfTable": ruijieVsuDadAPRelayIfTable,
       "ruijieVsuDadAPRelayIfEntry": ruijieVsuDadAPRelayIfEntry,
       "ruijieVsuDadAPRelayIfIndex": ruijieVsuDadAPRelayIfIndex,
       "ruijieVsuDadBFD": ruijieVsuDadBFD,
       "ruijieVsuDadBFDEnable": ruijieVsuDadBFDEnable,
       "ruijieVsuDadBFDIfTable": ruijieVsuDadBFDIfTable,
       "ruijieVsuDadBFDIfEntry": ruijieVsuDadBFDIfEntry,
       "ruijieVsuDadBFDIfIndex1": ruijieVsuDadBFDIfIndex1,
       "ruijieVsuDadBFDIfIndex2": ruijieVsuDadBFDIfIndex2,
       "ruijieVsuDadBFDIfStatus": ruijieVsuDadBFDIfStatus,
       "ruijieVsuForward": ruijieVsuForward,
       "ruijieVsuForwardApllf": ruijieVsuForwardApllf,
       "ruijieVsuForwardEcmpllf": ruijieVsuForwardEcmpllf,
       "ruijieVsuVersion": ruijieVsuVersion,
       "ruijieVsuMIBTraps": ruijieVsuMIBTraps,
       "ruijieVsuTrapsNtfObjects": ruijieVsuTrapsNtfObjects,
       "ruijieVsuDeviceState": ruijieVsuDeviceState,
       "ruijieVsuSlotID": ruijieVsuSlotID,
       "ruijieVsuDadResult": ruijieVsuDadResult,
       "ruijieVsuTrapsNotifications": ruijieVsuTrapsNotifications,
       "ruijieVsuNotifyTopoChange": ruijieVsuNotifyTopoChange,
       "ruijieVsuNotifyDeviceChange": ruijieVsuNotifyDeviceChange,
       "ruijieVsuNotifyDeviceRoleChange": ruijieVsuNotifyDeviceRoleChange,
       "ruijieVsuNotifyDad": ruijieVsuNotifyDad,
       "ruijieVsuNotifyDeviceJoin": ruijieVsuNotifyDeviceJoin,
       "ruijieVsuNotifyDeviceLeave": ruijieVsuNotifyDeviceLeave,
       "ruijieVsuMIBConformance": ruijieVsuMIBConformance,
       "ruijieVsuMIBCompliances": ruijieVsuMIBCompliances,
       "ruijieVsuMIBCompliance": ruijieVsuMIBCompliance,
       "ruijieVsuMIBGroups": ruijieVsuMIBGroups,
       "ruijieVsuMIBObjectsGroup": ruijieVsuMIBObjectsGroup,
       "ruijieVsuMIBTrapsGroup": ruijieVsuMIBTrapsGroup}
)
