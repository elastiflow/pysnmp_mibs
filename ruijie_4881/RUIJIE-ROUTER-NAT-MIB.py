# SNMP MIB module (RUIJIE-ROUTER-NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-ROUTER-NAT-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:02:06 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieNatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136)
)
if mibBuilder.loadTexts:
    ruijieNatMIB.setRevisions(
        ("2015-03-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RuijieNatType(TextualConvention, Integer32):
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
        *(("inside", 1),
          ("outside", 2),
          ("application", 3))
    )



class RuijieNatSrcDstType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("source", 1),
          ("destination", 2))
    )



class RuijieNatTcpUdpType(TextualConvention, Integer32):
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
        *(("tcp", 1),
          ("udp", 2),
          ("all", 3))
    )



class RuijieNatPoolAddressntmskprefixFlag(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("netmask", 1),
          ("prefix-length", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RuijieNatMIBObjects_ObjectIdentity = ObjectIdentity
ruijieNatMIBObjects = _RuijieNatMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1)
)
_RuijieNatSettingObjects_ObjectIdentity = ObjectIdentity
ruijieNatSettingObjects = _RuijieNatSettingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 1)
)
_RuijieNatSettingTable_Object = MibTable
ruijieNatSettingTable = _RuijieNatSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieNatSettingTable.setStatus("current")
_RuijieNatSettingEntry_Object = MibTableRow
ruijieNatSettingEntry = _RuijieNatSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 1, 1, 1)
)
ruijieNatSettingEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-NAT-MIB", "ruijieNatSettingIndex"),
)
if mibBuilder.loadTexts:
    ruijieNatSettingEntry.setStatus("current")
_RuijieNatSettingIndex_Type = Integer32
_RuijieNatSettingIndex_Object = MibTableColumn
ruijieNatSettingIndex = _RuijieNatSettingIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 1, 1, 1, 1),
    _RuijieNatSettingIndex_Type()
)
ruijieNatSettingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNatSettingIndex.setStatus("current")


class _RuijieNatSettingisno_Type(Integer32):
    """Custom type ruijieNatSettingisno based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieNatSettingisno_Type.__name__ = "Integer32"
_RuijieNatSettingisno_Object = MibTableColumn
ruijieNatSettingisno = _RuijieNatSettingisno_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 1, 1, 1, 2),
    _RuijieNatSettingisno_Type()
)
ruijieNatSettingisno.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatSettingisno.setStatus("current")
_RuijieNatSettingtype_Type = RuijieNatType
_RuijieNatSettingtype_Object = MibTableColumn
ruijieNatSettingtype = _RuijieNatSettingtype_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 1, 1, 1, 3),
    _RuijieNatSettingtype_Type()
)
ruijieNatSettingtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatSettingtype.setStatus("current")
_RuijieNatSettingsrcdst_Type = RuijieNatSrcDstType
_RuijieNatSettingsrcdst_Object = MibTableColumn
ruijieNatSettingsrcdst = _RuijieNatSettingsrcdst_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 1, 1, 1, 4),
    _RuijieNatSettingsrcdst_Type()
)
ruijieNatSettingsrcdst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatSettingsrcdst.setStatus("current")


class _RuijieNatSettingacltype_Type(Integer32):
    """Custom type ruijieNatSettingacltype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieNatSettingacltype_Type.__name__ = "Integer32"
_RuijieNatSettingacltype_Object = MibTableColumn
ruijieNatSettingacltype = _RuijieNatSettingacltype_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 1, 1, 1, 5),
    _RuijieNatSettingacltype_Type()
)
ruijieNatSettingacltype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatSettingacltype.setStatus("current")
_RuijieNatSettingaclnumber_Type = Integer32
_RuijieNatSettingaclnumber_Object = MibTableColumn
ruijieNatSettingaclnumber = _RuijieNatSettingaclnumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 1, 1, 1, 6),
    _RuijieNatSettingaclnumber_Type()
)
ruijieNatSettingaclnumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatSettingaclnumber.setStatus("current")


class _RuijieNatSettingaclname_Type(DisplayString):
    """Custom type ruijieNatSettingaclname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieNatSettingaclname_Type.__name__ = "DisplayString"
_RuijieNatSettingaclname_Object = MibTableColumn
ruijieNatSettingaclname = _RuijieNatSettingaclname_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 1, 1, 1, 7),
    _RuijieNatSettingaclname_Type()
)
ruijieNatSettingaclname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatSettingaclname.setStatus("current")


class _RuijieNatSettingstaticrule_Type(Integer32):
    """Custom type ruijieNatSettingstaticrule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieNatSettingstaticrule_Type.__name__ = "Integer32"
_RuijieNatSettingstaticrule_Object = MibTableColumn
ruijieNatSettingstaticrule = _RuijieNatSettingstaticrule_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 1, 1, 1, 8),
    _RuijieNatSettingstaticrule_Type()
)
ruijieNatSettingstaticrule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatSettingstaticrule.setStatus("current")
_RuijieNatSettingproto_Type = RuijieNatTcpUdpType
_RuijieNatSettingproto_Object = MibTableColumn
ruijieNatSettingproto = _RuijieNatSettingproto_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 1, 1, 1, 9),
    _RuijieNatSettingproto_Type()
)
ruijieNatSettingproto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatSettingproto.setStatus("current")
_RuijieNatSettinginlocalip_Type = IpAddress
_RuijieNatSettinginlocalip_Object = MibTableColumn
ruijieNatSettinginlocalip = _RuijieNatSettinginlocalip_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 1, 1, 1, 10),
    _RuijieNatSettinginlocalip_Type()
)
ruijieNatSettinginlocalip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatSettinginlocalip.setStatus("current")
_RuijieNatSettinginglobalip_Type = IpAddress
_RuijieNatSettinginglobalip_Object = MibTableColumn
ruijieNatSettinginglobalip = _RuijieNatSettinginglobalip_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 1, 1, 1, 11),
    _RuijieNatSettinginglobalip_Type()
)
ruijieNatSettinginglobalip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatSettinginglobalip.setStatus("current")
_RuijieNatSettingnetmask_Type = IpAddress
_RuijieNatSettingnetmask_Object = MibTableColumn
ruijieNatSettingnetmask = _RuijieNatSettingnetmask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 1, 1, 1, 12),
    _RuijieNatSettingnetmask_Type()
)
ruijieNatSettingnetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatSettingnetmask.setStatus("current")
_RuijieNatSettinglocalport_Type = Integer32
_RuijieNatSettinglocalport_Object = MibTableColumn
ruijieNatSettinglocalport = _RuijieNatSettinglocalport_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 1, 1, 1, 13),
    _RuijieNatSettinglocalport_Type()
)
ruijieNatSettinglocalport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatSettinglocalport.setStatus("current")
_RuijieNatSettingglobalport_Type = Integer32
_RuijieNatSettingglobalport_Object = MibTableColumn
ruijieNatSettingglobalport = _RuijieNatSettingglobalport_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 1, 1, 1, 14),
    _RuijieNatSettingglobalport_Type()
)
ruijieNatSettingglobalport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatSettingglobalport.setStatus("current")
_RuijieNatSettingmatchinterface_Type = Integer32
_RuijieNatSettingmatchinterface_Object = MibTableColumn
ruijieNatSettingmatchinterface = _RuijieNatSettingmatchinterface_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 1, 1, 1, 15),
    _RuijieNatSettingmatchinterface_Type()
)
ruijieNatSettingmatchinterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatSettingmatchinterface.setStatus("current")
_RuijieNatSettingpermisinside_Type = Integer32
_RuijieNatSettingpermisinside_Object = MibTableColumn
ruijieNatSettingpermisinside = _RuijieNatSettingpermisinside_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 1, 1, 1, 16),
    _RuijieNatSettingpermisinside_Type()
)
ruijieNatSettingpermisinside.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatSettingpermisinside.setStatus("current")
_RuijieNatSettinginterface_Type = Integer32
_RuijieNatSettinginterface_Object = MibTableColumn
ruijieNatSettinginterface = _RuijieNatSettinginterface_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 1, 1, 1, 17),
    _RuijieNatSettinginterface_Type()
)
ruijieNatSettinginterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatSettinginterface.setStatus("current")


class _RuijieNatSettingpool_Type(DisplayString):
    """Custom type ruijieNatSettingpool based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieNatSettingpool_Type.__name__ = "DisplayString"
_RuijieNatSettingpool_Object = MibTableColumn
ruijieNatSettingpool = _RuijieNatSettingpool_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 1, 1, 1, 18),
    _RuijieNatSettingpool_Type()
)
ruijieNatSettingpool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatSettingpool.setStatus("current")
_RuijieNatSettingdstchange_Type = IpAddress
_RuijieNatSettingdstchange_Object = MibTableColumn
ruijieNatSettingdstchange = _RuijieNatSettingdstchange_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 1, 1, 1, 19),
    _RuijieNatSettingdstchange_Type()
)
ruijieNatSettingdstchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatSettingdstchange.setStatus("current")
_RuijieNatSettingsrcchange_Type = IpAddress
_RuijieNatSettingsrcchange_Object = MibTableColumn
ruijieNatSettingsrcchange = _RuijieNatSettingsrcchange_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 1, 1, 1, 20),
    _RuijieNatSettingsrcchange_Type()
)
ruijieNatSettingsrcchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatSettingsrcchange.setStatus("current")
_RuijieNatPoolAddressObjects_ObjectIdentity = ObjectIdentity
ruijieNatPoolAddressObjects = _RuijieNatPoolAddressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 2)
)
_RuijieNatPoolAddressTable_Object = MibTable
ruijieNatPoolAddressTable = _RuijieNatPoolAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieNatPoolAddressTable.setStatus("current")
_RuijieNatPoolAddressEntry_Object = MibTableRow
ruijieNatPoolAddressEntry = _RuijieNatPoolAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 2, 1, 1)
)
ruijieNatPoolAddressEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-NAT-MIB", "ruijieNatPoolAddressIndex"),
)
if mibBuilder.loadTexts:
    ruijieNatPoolAddressEntry.setStatus("current")
_RuijieNatPoolAddressIndex_Type = Integer32
_RuijieNatPoolAddressIndex_Object = MibTableColumn
ruijieNatPoolAddressIndex = _RuijieNatPoolAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 2, 1, 1, 1),
    _RuijieNatPoolAddressIndex_Type()
)
ruijieNatPoolAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNatPoolAddressIndex.setStatus("current")


class _RuijieNatPoolAddressisno_Type(Integer32):
    """Custom type ruijieNatPoolAddressisno based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieNatPoolAddressisno_Type.__name__ = "Integer32"
_RuijieNatPoolAddressisno_Object = MibTableColumn
ruijieNatPoolAddressisno = _RuijieNatPoolAddressisno_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 2, 1, 1, 2),
    _RuijieNatPoolAddressisno_Type()
)
ruijieNatPoolAddressisno.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatPoolAddressisno.setStatus("current")


class _RuijieNatPoolAddressname_Type(DisplayString):
    """Custom type ruijieNatPoolAddressname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieNatPoolAddressname_Type.__name__ = "DisplayString"
_RuijieNatPoolAddressname_Object = MibTableColumn
ruijieNatPoolAddressname = _RuijieNatPoolAddressname_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 2, 1, 1, 3),
    _RuijieNatPoolAddressname_Type()
)
ruijieNatPoolAddressname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatPoolAddressname.setStatus("current")
_RuijieNatPoolAddressntmskprefix_Type = RuijieNatPoolAddressntmskprefixFlag
_RuijieNatPoolAddressntmskprefix_Object = MibTableColumn
ruijieNatPoolAddressntmskprefix = _RuijieNatPoolAddressntmskprefix_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 2, 1, 1, 4),
    _RuijieNatPoolAddressntmskprefix_Type()
)
ruijieNatPoolAddressntmskprefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatPoolAddressntmskprefix.setStatus("current")
_RuijieNatPoolAddressnetmask_Type = IpAddress
_RuijieNatPoolAddressnetmask_Object = MibTableColumn
ruijieNatPoolAddressnetmask = _RuijieNatPoolAddressnetmask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 2, 1, 1, 5),
    _RuijieNatPoolAddressnetmask_Type()
)
ruijieNatPoolAddressnetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatPoolAddressnetmask.setStatus("current")
_RuijieNatPoolAddressprefixlength_Type = Integer32
_RuijieNatPoolAddressprefixlength_Object = MibTableColumn
ruijieNatPoolAddressprefixlength = _RuijieNatPoolAddressprefixlength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 2, 1, 1, 6),
    _RuijieNatPoolAddressprefixlength_Type()
)
ruijieNatPoolAddressprefixlength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatPoolAddressprefixlength.setStatus("current")
_RuijieNatPoolAddressstartip_Type = IpAddress
_RuijieNatPoolAddressstartip_Object = MibTableColumn
ruijieNatPoolAddressstartip = _RuijieNatPoolAddressstartip_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 2, 1, 1, 7),
    _RuijieNatPoolAddressstartip_Type()
)
ruijieNatPoolAddressstartip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatPoolAddressstartip.setStatus("current")
_RuijieNatPoolAddressendip_Type = IpAddress
_RuijieNatPoolAddressendip_Object = MibTableColumn
ruijieNatPoolAddressendip = _RuijieNatPoolAddressendip_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 2, 1, 1, 8),
    _RuijieNatPoolAddressendip_Type()
)
ruijieNatPoolAddressendip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatPoolAddressendip.setStatus("current")
_RuijieNatPoolAddressstartinterface_Type = Integer32
_RuijieNatPoolAddressstartinterface_Object = MibTableColumn
ruijieNatPoolAddressstartinterface = _RuijieNatPoolAddressstartinterface_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 2, 1, 1, 9),
    _RuijieNatPoolAddressstartinterface_Type()
)
ruijieNatPoolAddressstartinterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatPoolAddressstartinterface.setStatus("current")
_RuijieNatPoolAddressendinterface_Type = Integer32
_RuijieNatPoolAddressendinterface_Object = MibTableColumn
ruijieNatPoolAddressendinterface = _RuijieNatPoolAddressendinterface_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 2, 1, 1, 10),
    _RuijieNatPoolAddressendinterface_Type()
)
ruijieNatPoolAddressendinterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatPoolAddressendinterface.setStatus("current")
_RuijieNatPoolAddresstype_Type = Integer32
_RuijieNatPoolAddresstype_Object = MibTableColumn
ruijieNatPoolAddresstype = _RuijieNatPoolAddresstype_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 2, 1, 1, 11),
    _RuijieNatPoolAddresstype_Type()
)
ruijieNatPoolAddresstype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatPoolAddresstype.setStatus("current")
_RuijieNatInterfaceObjects_ObjectIdentity = ObjectIdentity
ruijieNatInterfaceObjects = _RuijieNatInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 3)
)
_RuijieNatInterfaceTable_Object = MibTable
ruijieNatInterfaceTable = _RuijieNatInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ruijieNatInterfaceTable.setStatus("current")
_RuijieNatInterfaceEntry_Object = MibTableRow
ruijieNatInterfaceEntry = _RuijieNatInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 3, 1, 1)
)
ruijieNatInterfaceEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-NAT-MIB", "ruijieNatInterfaceIndex"),
)
if mibBuilder.loadTexts:
    ruijieNatInterfaceEntry.setStatus("current")
_RuijieNatInterfaceIndex_Type = Integer32
_RuijieNatInterfaceIndex_Object = MibTableColumn
ruijieNatInterfaceIndex = _RuijieNatInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 3, 1, 1, 1),
    _RuijieNatInterfaceIndex_Type()
)
ruijieNatInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNatInterfaceIndex.setStatus("current")


class _RuijieNatInterfaceisno_Type(Integer32):
    """Custom type ruijieNatInterfaceisno based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieNatInterfaceisno_Type.__name__ = "Integer32"
_RuijieNatInterfaceisno_Object = MibTableColumn
ruijieNatInterfaceisno = _RuijieNatInterfaceisno_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 3, 1, 1, 2),
    _RuijieNatInterfaceisno_Type()
)
ruijieNatInterfaceisno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNatInterfaceisno.setStatus("current")
_RuijieNatInterfacedirector_Type = Integer32
_RuijieNatInterfacedirector_Object = MibTableColumn
ruijieNatInterfacedirector = _RuijieNatInterfacedirector_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 136, 1, 3, 1, 1, 3),
    _RuijieNatInterfacedirector_Type()
)
ruijieNatInterfacedirector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNatInterfacedirector.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-ROUTER-NAT-MIB",
    **{"RuijieNatType": RuijieNatType,
       "RuijieNatSrcDstType": RuijieNatSrcDstType,
       "RuijieNatTcpUdpType": RuijieNatTcpUdpType,
       "RuijieNatPoolAddressntmskprefixFlag": RuijieNatPoolAddressntmskprefixFlag,
       "ruijieNatMIB": ruijieNatMIB,
       "ruijieNatMIBObjects": ruijieNatMIBObjects,
       "ruijieNatSettingObjects": ruijieNatSettingObjects,
       "ruijieNatSettingTable": ruijieNatSettingTable,
       "ruijieNatSettingEntry": ruijieNatSettingEntry,
       "ruijieNatSettingIndex": ruijieNatSettingIndex,
       "ruijieNatSettingisno": ruijieNatSettingisno,
       "ruijieNatSettingtype": ruijieNatSettingtype,
       "ruijieNatSettingsrcdst": ruijieNatSettingsrcdst,
       "ruijieNatSettingacltype": ruijieNatSettingacltype,
       "ruijieNatSettingaclnumber": ruijieNatSettingaclnumber,
       "ruijieNatSettingaclname": ruijieNatSettingaclname,
       "ruijieNatSettingstaticrule": ruijieNatSettingstaticrule,
       "ruijieNatSettingproto": ruijieNatSettingproto,
       "ruijieNatSettinginlocalip": ruijieNatSettinginlocalip,
       "ruijieNatSettinginglobalip": ruijieNatSettinginglobalip,
       "ruijieNatSettingnetmask": ruijieNatSettingnetmask,
       "ruijieNatSettinglocalport": ruijieNatSettinglocalport,
       "ruijieNatSettingglobalport": ruijieNatSettingglobalport,
       "ruijieNatSettingmatchinterface": ruijieNatSettingmatchinterface,
       "ruijieNatSettingpermisinside": ruijieNatSettingpermisinside,
       "ruijieNatSettinginterface": ruijieNatSettinginterface,
       "ruijieNatSettingpool": ruijieNatSettingpool,
       "ruijieNatSettingdstchange": ruijieNatSettingdstchange,
       "ruijieNatSettingsrcchange": ruijieNatSettingsrcchange,
       "ruijieNatPoolAddressObjects": ruijieNatPoolAddressObjects,
       "ruijieNatPoolAddressTable": ruijieNatPoolAddressTable,
       "ruijieNatPoolAddressEntry": ruijieNatPoolAddressEntry,
       "ruijieNatPoolAddressIndex": ruijieNatPoolAddressIndex,
       "ruijieNatPoolAddressisno": ruijieNatPoolAddressisno,
       "ruijieNatPoolAddressname": ruijieNatPoolAddressname,
       "ruijieNatPoolAddressntmskprefix": ruijieNatPoolAddressntmskprefix,
       "ruijieNatPoolAddressnetmask": ruijieNatPoolAddressnetmask,
       "ruijieNatPoolAddressprefixlength": ruijieNatPoolAddressprefixlength,
       "ruijieNatPoolAddressstartip": ruijieNatPoolAddressstartip,
       "ruijieNatPoolAddressendip": ruijieNatPoolAddressendip,
       "ruijieNatPoolAddressstartinterface": ruijieNatPoolAddressstartinterface,
       "ruijieNatPoolAddressendinterface": ruijieNatPoolAddressendinterface,
       "ruijieNatPoolAddresstype": ruijieNatPoolAddresstype,
       "ruijieNatInterfaceObjects": ruijieNatInterfaceObjects,
       "ruijieNatInterfaceTable": ruijieNatInterfaceTable,
       "ruijieNatInterfaceEntry": ruijieNatInterfaceEntry,
       "ruijieNatInterfaceIndex": ruijieNatInterfaceIndex,
       "ruijieNatInterfaceisno": ruijieNatInterfaceisno,
       "ruijieNatInterfacedirector": ruijieNatInterfacedirector}
)
