# SNMP MIB module (RUIJIE-4G-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-4G-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:06:22 2025
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
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ruijie4GMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127)
)
if mibBuilder.loadTexts:
    ruijie4GMonitor.setRevisions(
        ("2014-03-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ruijie4GObjects_ObjectIdentity = ObjectIdentity
ruijie4GObjects = _Ruijie4GObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1)
)
_Ruijie4GTable_Object = MibTable
ruijie4GTable = _Ruijie4GTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1)
)
if mibBuilder.loadTexts:
    ruijie4GTable.setStatus("current")
_Ruijie4GEntry_Object = MibTableRow
ruijie4GEntry = _Ruijie4GEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1)
)
ruijie4GEntry.setIndexNames(
    (0, "RUIJIE-4G-MIB", "ruijie4GRouterSlotNumber"),
)
if mibBuilder.loadTexts:
    ruijie4GEntry.setStatus("current")
_Ruijie4GUsername_Type = DisplayString
_Ruijie4GUsername_Object = MibTableColumn
ruijie4GUsername = _Ruijie4GUsername_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 1),
    _Ruijie4GUsername_Type()
)
ruijie4GUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GUsername.setStatus("current")
_Ruijie4GApn_Type = DisplayString
_Ruijie4GApn_Object = MibTableColumn
ruijie4GApn = _Ruijie4GApn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 2),
    _Ruijie4GApn_Type()
)
ruijie4GApn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GApn.setStatus("current")


class _Ruijie4GOnlineStatus_Type(Integer32):
    """Custom type ruijie4GOnlineStatus based on Integer32"""
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
        *(("minimum-function", 0),
          ("fully-function", 1),
          ("offline-mode", 2),
          ("sim-activate", 3),
          ("sim-deactivate", 4))
    )


_Ruijie4GOnlineStatus_Type.__name__ = "Integer32"
_Ruijie4GOnlineStatus_Object = MibTableColumn
ruijie4GOnlineStatus = _Ruijie4GOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 3),
    _Ruijie4GOnlineStatus_Type()
)
ruijie4GOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GOnlineStatus.setStatus("current")
_Ruijie4GIMEI_Type = DisplayString
_Ruijie4GIMEI_Object = MibTableColumn
ruijie4GIMEI = _Ruijie4GIMEI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 4),
    _Ruijie4GIMEI_Type()
)
ruijie4GIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GIMEI.setStatus("current")


class _Ruijie4GIPAddrType_Type(Integer32):
    """Custom type ruijie4GIPAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4Addr", 1),
          ("ipv6Addr", 2))
    )


_Ruijie4GIPAddrType_Type.__name__ = "Integer32"
_Ruijie4GIPAddrType_Object = MibTableColumn
ruijie4GIPAddrType = _Ruijie4GIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 5),
    _Ruijie4GIPAddrType_Type()
)
ruijie4GIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GIPAddrType.setStatus("current")
_Ruijie4GIPAddr_Type = IpAddress
_Ruijie4GIPAddr_Object = MibTableColumn
ruijie4GIPAddr = _Ruijie4GIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 6),
    _Ruijie4GIPAddr_Type()
)
ruijie4GIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GIPAddr.setStatus("current")
_Ruijie4GUplineTime_Type = TimeStamp
_Ruijie4GUplineTime_Object = MibTableColumn
ruijie4GUplineTime = _Ruijie4GUplineTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 7),
    _Ruijie4GUplineTime_Type()
)
ruijie4GUplineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GUplineTime.setStatus("current")


class _Ruijie4GActiveTime_Type(Integer32):
    """Custom type ruijie4GActiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ruijie4GActiveTime_Type.__name__ = "Integer32"
_Ruijie4GActiveTime_Object = MibTableColumn
ruijie4GActiveTime = _Ruijie4GActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 8),
    _Ruijie4GActiveTime_Type()
)
ruijie4GActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GActiveTime.setStatus("current")


class _Ruijie4GRSRP_Type(Integer32):
    """Custom type ruijie4GRSRP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Ruijie4GRSRP_Type.__name__ = "Integer32"
_Ruijie4GRSRP_Object = MibTableColumn
ruijie4GRSRP = _Ruijie4GRSRP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 9),
    _Ruijie4GRSRP_Type()
)
ruijie4GRSRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GRSRP.setStatus("current")


class _Ruijie4GSignalStrengthPercent_Type(Integer32):
    """Custom type ruijie4GSignalStrengthPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ruijie4GSignalStrengthPercent_Type.__name__ = "Integer32"
_Ruijie4GSignalStrengthPercent_Object = MibTableColumn
ruijie4GSignalStrengthPercent = _Ruijie4GSignalStrengthPercent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 10),
    _Ruijie4GSignalStrengthPercent_Type()
)
ruijie4GSignalStrengthPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GSignalStrengthPercent.setStatus("current")


class _Ruijie4GISP_Type(Integer32):
    """Custom type ruijie4GISP based on Integer32"""
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
        *(("unknow", 0),
          ("chinaUnicom", 1),
          ("chinaTelecom", 2),
          ("chinaMobile", 3))
    )


_Ruijie4GISP_Type.__name__ = "Integer32"
_Ruijie4GISP_Object = MibTableColumn
ruijie4GISP = _Ruijie4GISP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 11),
    _Ruijie4GISP_Type()
)
ruijie4GISP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GISP.setStatus("current")


class _Ruijie4GSysMode_Type(Integer32):
    """Custom type ruijie4GSysMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              5,
              15,
              17)
        )
    )
    namedValues = NamedValues(
        *(("no-service", 0),
          ("gsm-gprs", 3),
          ("wcdma", 5),
          ("td-scdma", 15),
          ("lte", 17))
    )


_Ruijie4GSysMode_Type.__name__ = "Integer32"
_Ruijie4GSysMode_Object = MibTableColumn
ruijie4GSysMode = _Ruijie4GSysMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 12),
    _Ruijie4GSysMode_Type()
)
ruijie4GSysMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GSysMode.setStatus("current")


class _Ruijie4GServiceStatus_Type(Integer32):
    """Custom type ruijie4GServiceStatus based on Integer32"""
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
        *(("noService", 0),
          ("restricted", 1),
          ("valid", 2),
          ("restrictedRegional", 3),
          ("powerSavingAndDeepSleepState", 4))
    )


_Ruijie4GServiceStatus_Type.__name__ = "Integer32"
_Ruijie4GServiceStatus_Object = MibTableColumn
ruijie4GServiceStatus = _Ruijie4GServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 13),
    _Ruijie4GServiceStatus_Type()
)
ruijie4GServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GServiceStatus.setStatus("current")


class _Ruijie4GRoamingStatus_Type(Integer32):
    """Custom type ruijie4GRoamingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noRoaming", 0),
          ("roaming", 1))
    )


_Ruijie4GRoamingStatus_Type.__name__ = "Integer32"
_Ruijie4GRoamingStatus_Object = MibTableColumn
ruijie4GRoamingStatus = _Ruijie4GRoamingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 14),
    _Ruijie4GRoamingStatus_Type()
)
ruijie4GRoamingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GRoamingStatus.setStatus("current")


class _Ruijie4GDomain_Type(Integer32):
    """Custom type ruijie4GDomain based on Integer32"""
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
        *(("noService", 0),
          ("onlyCS", 1),
          ("onlyPS", 2),
          ("pSCS", 3),
          ("ePS", 4))
    )


_Ruijie4GDomain_Type.__name__ = "Integer32"
_Ruijie4GDomain_Object = MibTableColumn
ruijie4GDomain = _Ruijie4GDomain_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 15),
    _Ruijie4GDomain_Type()
)
ruijie4GDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GDomain.setStatus("current")


class _Ruijie4GSIMStatus_Type(Integer32):
    """Custom type ruijie4GSIMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("invalidUsimCard", 0),
          ("validUsimCard", 1),
          ("noUsimCard", 255))
    )


_Ruijie4GSIMStatus_Type.__name__ = "Integer32"
_Ruijie4GSIMStatus_Object = MibTableColumn
ruijie4GSIMStatus = _Ruijie4GSIMStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 16),
    _Ruijie4GSIMStatus_Type()
)
ruijie4GSIMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GSIMStatus.setStatus("current")


class _Ruijie4GCellID_Type(Integer32):
    """Custom type ruijie4GCellID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ruijie4GCellID_Type.__name__ = "Integer32"
_Ruijie4GCellID_Object = MibTableColumn
ruijie4GCellID = _Ruijie4GCellID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 17),
    _Ruijie4GCellID_Type()
)
ruijie4GCellID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GCellID.setStatus("current")


class _Ruijie4GLAC_Type(Integer32):
    """Custom type ruijie4GLAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ruijie4GLAC_Type.__name__ = "Integer32"
_Ruijie4GLAC_Object = MibTableColumn
ruijie4GLAC = _Ruijie4GLAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 18),
    _Ruijie4GLAC_Type()
)
ruijie4GLAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GLAC.setStatus("current")
_Ruijie4GIMSI_Type = DisplayString
_Ruijie4GIMSI_Object = MibTableColumn
ruijie4GIMSI = _Ruijie4GIMSI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 19),
    _Ruijie4GIMSI_Type()
)
ruijie4GIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GIMSI.setStatus("current")
_Ruijie4GPhoneNumber_Type = DisplayString
_Ruijie4GPhoneNumber_Object = MibTableColumn
ruijie4GPhoneNumber = _Ruijie4GPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 20),
    _Ruijie4GPhoneNumber_Type()
)
ruijie4GPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GPhoneNumber.setStatus("current")
_Ruijie4GifIndex_Type = Integer32
_Ruijie4GifIndex_Object = MibTableColumn
ruijie4GifIndex = _Ruijie4GifIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 21),
    _Ruijie4GifIndex_Type()
)
ruijie4GifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GifIndex.setStatus("current")
_Ruijie4GInOctets_Type = Counter64
_Ruijie4GInOctets_Object = MibTableColumn
ruijie4GInOctets = _Ruijie4GInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 22),
    _Ruijie4GInOctets_Type()
)
ruijie4GInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GInOctets.setStatus("current")
_Ruijie4GOutOctets_Type = Counter64
_Ruijie4GOutOctets_Object = MibTableColumn
ruijie4GOutOctets = _Ruijie4GOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 23),
    _Ruijie4GOutOctets_Type()
)
ruijie4GOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GOutOctets.setStatus("current")
_Ruijie4GInSpeed_Type = Counter64
_Ruijie4GInSpeed_Object = MibTableColumn
ruijie4GInSpeed = _Ruijie4GInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 24),
    _Ruijie4GInSpeed_Type()
)
ruijie4GInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GInSpeed.setStatus("current")
_Ruijie4GOutSpeed_Type = Counter64
_Ruijie4GOutSpeed_Object = MibTableColumn
ruijie4GOutSpeed = _Ruijie4GOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 25),
    _Ruijie4GOutSpeed_Type()
)
ruijie4GOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GOutSpeed.setStatus("current")
_Ruijie4GBSLONG_Type = Integer32
_Ruijie4GBSLONG_Object = MibTableColumn
ruijie4GBSLONG = _Ruijie4GBSLONG_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 26),
    _Ruijie4GBSLONG_Type()
)
ruijie4GBSLONG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GBSLONG.setStatus("current")
_Ruijie4GBSLAT_Type = Integer32
_Ruijie4GBSLAT_Object = MibTableColumn
ruijie4GBSLAT = _Ruijie4GBSLAT_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 27),
    _Ruijie4GBSLAT_Type()
)
ruijie4GBSLAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GBSLAT.setStatus("current")
_Ruijie4GRouterType_Type = DisplayString
_Ruijie4GRouterType_Object = MibTableColumn
ruijie4GRouterType = _Ruijie4GRouterType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 28),
    _Ruijie4GRouterType_Type()
)
ruijie4GRouterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GRouterType.setStatus("current")
_Ruijie4GRouterSN_Type = DisplayString
_Ruijie4GRouterSN_Object = MibTableColumn
ruijie4GRouterSN = _Ruijie4GRouterSN_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 29),
    _Ruijie4GRouterSN_Type()
)
ruijie4GRouterSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GRouterSN.setStatus("current")
_Ruijie4GRouterSlotNumber_Type = DisplayString
_Ruijie4GRouterSlotNumber_Object = MibTableColumn
ruijie4GRouterSlotNumber = _Ruijie4GRouterSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 30),
    _Ruijie4GRouterSlotNumber_Type()
)
ruijie4GRouterSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GRouterSlotNumber.setStatus("current")
_Ruijie4GLineCardType_Type = DisplayString
_Ruijie4GLineCardType_Object = MibTableColumn
ruijie4GLineCardType = _Ruijie4GLineCardType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 31),
    _Ruijie4GLineCardType_Type()
)
ruijie4GLineCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GLineCardType.setStatus("current")


class _Ruijie4GDialdMode_Type(Integer32):
    """Custom type ruijie4GDialdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto-dial", 0),
          ("dial-on-demand", 1))
    )


_Ruijie4GDialdMode_Type.__name__ = "Integer32"
_Ruijie4GDialdMode_Object = MibTableColumn
ruijie4GDialdMode = _Ruijie4GDialdMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 32),
    _Ruijie4GDialdMode_Type()
)
ruijie4GDialdMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GDialdMode.setStatus("current")
_Ruijie4GDialOnDemandIfIndex_Type = Integer32
_Ruijie4GDialOnDemandIfIndex_Object = MibTableColumn
ruijie4GDialOnDemandIfIndex = _Ruijie4GDialOnDemandIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 33),
    _Ruijie4GDialOnDemandIfIndex_Type()
)
ruijie4GDialOnDemandIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GDialOnDemandIfIndex.setStatus("current")


class _Ruijie4GTrafficPreventMode_Type(Integer32):
    """Custom type ruijie4GTrafficPreventMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ruijie4GTrafficPreventMode_Type.__name__ = "Integer32"
_Ruijie4GTrafficPreventMode_Object = MibTableColumn
ruijie4GTrafficPreventMode = _Ruijie4GTrafficPreventMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 34),
    _Ruijie4GTrafficPreventMode_Type()
)
ruijie4GTrafficPreventMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GTrafficPreventMode.setStatus("current")
_Ruijie4GTrafficPreventIfIndex_Type = Integer32
_Ruijie4GTrafficPreventIfIndex_Object = MibTableColumn
ruijie4GTrafficPreventIfIndex = _Ruijie4GTrafficPreventIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 35),
    _Ruijie4GTrafficPreventIfIndex_Type()
)
ruijie4GTrafficPreventIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GTrafficPreventIfIndex.setStatus("current")
_Ruijie4GTrafficPreventListID_Type = Integer32
_Ruijie4GTrafficPreventListID_Object = MibTableColumn
ruijie4GTrafficPreventListID = _Ruijie4GTrafficPreventListID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 36),
    _Ruijie4GTrafficPreventListID_Type()
)
ruijie4GTrafficPreventListID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GTrafficPreventListID.setStatus("current")
_Ruijie4GTrafficPreventListName_Type = DisplayString
_Ruijie4GTrafficPreventListName_Object = MibTableColumn
ruijie4GTrafficPreventListName = _Ruijie4GTrafficPreventListName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 1, 1, 1, 37),
    _Ruijie4GTrafficPreventListName_Type()
)
ruijie4GTrafficPreventListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie4GTrafficPreventListName.setStatus("current")
_Ruijie4GTrap_ObjectIdentity = ObjectIdentity
ruijie4GTrap = _Ruijie4GTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 2)
)
_Ruijie4GNotifications_ObjectIdentity = ObjectIdentity
ruijie4GNotifications = _Ruijie4GNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 2, 1)
)

# Managed Objects groups


# Notification objects

ruijie4GUpLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 2, 1, 1)
)
ruijie4GUpLine.setObjects(
      *(("RUIJIE-4G-MIB", "ruijie4GRouterSlotNumber"),
        ("RUIJIE-4G-MIB", "ruijie4GIMSI"),
        ("RUIJIE-4G-MIB", "ruijie4GUsername"),
        ("RUIJIE-4G-MIB", "ruijie4GRouterSN"),
        ("RUIJIE-4G-MIB", "ruijie4GPhoneNumber"),
        ("RUIJIE-4G-MIB", "ruijie4GDialdMode"),
        ("RUIJIE-4G-MIB", "ruijie4GDialOnDemandIfIndex"),
        ("RUIJIE-4G-MIB", "ruijie4GTrafficPreventMode"),
        ("RUIJIE-4G-MIB", "ruijie4GTrafficPreventIfIndex"),
        ("RUIJIE-4G-MIB", "ruijie4GIPAddr"),
        ("RUIJIE-4G-MIB", "ruijie4GTrafficPreventListID"),
        ("RUIJIE-4G-MIB", "ruijie4GTrafficPreventListName"))
)
if mibBuilder.loadTexts:
    ruijie4GUpLine.setStatus(
        "current"
    )

ruijie4GDownLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 2, 1, 2)
)
ruijie4GDownLine.setObjects(
      *(("RUIJIE-4G-MIB", "ruijie4GRouterSlotNumber"),
        ("RUIJIE-4G-MIB", "ruijie4GIMSI"),
        ("RUIJIE-4G-MIB", "ruijie4GUsername"),
        ("RUIJIE-4G-MIB", "ruijie4GRouterSN"),
        ("RUIJIE-4G-MIB", "ruijie4GPhoneNumber"),
        ("RUIJIE-4G-MIB", "ruijie4GDialdMode"),
        ("RUIJIE-4G-MIB", "ruijie4GDialOnDemandIfIndex"),
        ("RUIJIE-4G-MIB", "ruijie4GTrafficPreventMode"),
        ("RUIJIE-4G-MIB", "ruijie4GTrafficPreventIfIndex"),
        ("RUIJIE-4G-MIB", "ruijie4GIPAddr"),
        ("RUIJIE-4G-MIB", "ruijie4GTrafficPreventListID"),
        ("RUIJIE-4G-MIB", "ruijie4GTrafficPreventListName"))
)
if mibBuilder.loadTexts:
    ruijie4GDownLine.setStatus(
        "current"
    )

ruijie4GSignalThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 2, 1, 3)
)
ruijie4GSignalThreshold.setObjects(
      *(("RUIJIE-4G-MIB", "ruijie4GRouterSlotNumber"),
        ("RUIJIE-4G-MIB", "ruijie4GIMSI"),
        ("RUIJIE-4G-MIB", "ruijie4GRSRP"),
        ("RUIJIE-4G-MIB", "ruijie4GSignalStrengthPercent"))
)
if mibBuilder.loadTexts:
    ruijie4GSignalThreshold.setStatus(
        "current"
    )

ruijie4GTrafficInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 2, 1, 4)
)
ruijie4GTrafficInformation.setObjects(
      *(("RUIJIE-4G-MIB", "ruijie4GRouterSlotNumber"),
        ("RUIJIE-4G-MIB", "ruijie4GIMSI"),
        ("RUIJIE-4G-MIB", "ruijie4GInOctets"),
        ("RUIJIE-4G-MIB", "ruijie4GOutOctets"))
)
if mibBuilder.loadTexts:
    ruijie4GTrafficInformation.setStatus(
        "current"
    )

ruijie4GBackupMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 2, 1, 5)
)
ruijie4GBackupMaster.setObjects(
      *(("RUIJIE-4G-MIB", "ruijie4GRouterSlotNumber"),
        ("RUIJIE-4G-MIB", "ruijie4GIMSI"),
        ("RUIJIE-4G-MIB", "ruijie4GUsername"),
        ("RUIJIE-4G-MIB", "ruijie4GRouterSN"),
        ("RUIJIE-4G-MIB", "ruijie4GPhoneNumber"),
        ("RUIJIE-4G-MIB", "ruijie4GDialdMode"),
        ("RUIJIE-4G-MIB", "ruijie4GDialOnDemandIfIndex"),
        ("RUIJIE-4G-MIB", "ruijie4GTrafficPreventMode"),
        ("RUIJIE-4G-MIB", "ruijie4GTrafficPreventIfIndex"),
        ("RUIJIE-4G-MIB", "ruijie4GIPAddr"),
        ("RUIJIE-4G-MIB", "ruijie4GTrafficPreventListID"),
        ("RUIJIE-4G-MIB", "ruijie4GTrafficPreventListName"))
)
if mibBuilder.loadTexts:
    ruijie4GBackupMaster.setStatus(
        "current"
    )

ruijie4GBackupSlave = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 127, 2, 1, 6)
)
ruijie4GBackupSlave.setObjects(
      *(("RUIJIE-4G-MIB", "ruijie4GRouterSlotNumber"),
        ("RUIJIE-4G-MIB", "ruijie4GIMSI"),
        ("RUIJIE-4G-MIB", "ruijie4GUsername"),
        ("RUIJIE-4G-MIB", "ruijie4GRouterSN"),
        ("RUIJIE-4G-MIB", "ruijie4GPhoneNumber"),
        ("RUIJIE-4G-MIB", "ruijie4GDialdMode"),
        ("RUIJIE-4G-MIB", "ruijie4GDialOnDemandIfIndex"),
        ("RUIJIE-4G-MIB", "ruijie4GTrafficPreventMode"),
        ("RUIJIE-4G-MIB", "ruijie4GTrafficPreventIfIndex"),
        ("RUIJIE-4G-MIB", "ruijie4GIPAddr"),
        ("RUIJIE-4G-MIB", "ruijie4GTrafficPreventListID"),
        ("RUIJIE-4G-MIB", "ruijie4GTrafficPreventListName"))
)
if mibBuilder.loadTexts:
    ruijie4GBackupSlave.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-4G-MIB",
    **{"ruijie4GMonitor": ruijie4GMonitor,
       "ruijie4GObjects": ruijie4GObjects,
       "ruijie4GTable": ruijie4GTable,
       "ruijie4GEntry": ruijie4GEntry,
       "ruijie4GUsername": ruijie4GUsername,
       "ruijie4GApn": ruijie4GApn,
       "ruijie4GOnlineStatus": ruijie4GOnlineStatus,
       "ruijie4GIMEI": ruijie4GIMEI,
       "ruijie4GIPAddrType": ruijie4GIPAddrType,
       "ruijie4GIPAddr": ruijie4GIPAddr,
       "ruijie4GUplineTime": ruijie4GUplineTime,
       "ruijie4GActiveTime": ruijie4GActiveTime,
       "ruijie4GRSRP": ruijie4GRSRP,
       "ruijie4GSignalStrengthPercent": ruijie4GSignalStrengthPercent,
       "ruijie4GISP": ruijie4GISP,
       "ruijie4GSysMode": ruijie4GSysMode,
       "ruijie4GServiceStatus": ruijie4GServiceStatus,
       "ruijie4GRoamingStatus": ruijie4GRoamingStatus,
       "ruijie4GDomain": ruijie4GDomain,
       "ruijie4GSIMStatus": ruijie4GSIMStatus,
       "ruijie4GCellID": ruijie4GCellID,
       "ruijie4GLAC": ruijie4GLAC,
       "ruijie4GIMSI": ruijie4GIMSI,
       "ruijie4GPhoneNumber": ruijie4GPhoneNumber,
       "ruijie4GifIndex": ruijie4GifIndex,
       "ruijie4GInOctets": ruijie4GInOctets,
       "ruijie4GOutOctets": ruijie4GOutOctets,
       "ruijie4GInSpeed": ruijie4GInSpeed,
       "ruijie4GOutSpeed": ruijie4GOutSpeed,
       "ruijie4GBSLONG": ruijie4GBSLONG,
       "ruijie4GBSLAT": ruijie4GBSLAT,
       "ruijie4GRouterType": ruijie4GRouterType,
       "ruijie4GRouterSN": ruijie4GRouterSN,
       "ruijie4GRouterSlotNumber": ruijie4GRouterSlotNumber,
       "ruijie4GLineCardType": ruijie4GLineCardType,
       "ruijie4GDialdMode": ruijie4GDialdMode,
       "ruijie4GDialOnDemandIfIndex": ruijie4GDialOnDemandIfIndex,
       "ruijie4GTrafficPreventMode": ruijie4GTrafficPreventMode,
       "ruijie4GTrafficPreventIfIndex": ruijie4GTrafficPreventIfIndex,
       "ruijie4GTrafficPreventListID": ruijie4GTrafficPreventListID,
       "ruijie4GTrafficPreventListName": ruijie4GTrafficPreventListName,
       "ruijie4GTrap": ruijie4GTrap,
       "ruijie4GNotifications": ruijie4GNotifications,
       "ruijie4GUpLine": ruijie4GUpLine,
       "ruijie4GDownLine": ruijie4GDownLine,
       "ruijie4GSignalThreshold": ruijie4GSignalThreshold,
       "ruijie4GTrafficInformation": ruijie4GTrafficInformation,
       "ruijie4GBackupMaster": ruijie4GBackupMaster,
       "ruijie4GBackupSlave": ruijie4GBackupSlave}
)
