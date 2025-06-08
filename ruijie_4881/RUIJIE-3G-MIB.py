# SNMP MIB module (RUIJIE-3G-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-3G-MIB.mib
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

ruijie3GMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95)
)
if mibBuilder.loadTexts:
    ruijie3GMonitor.setRevisions(
        ("2020-10-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ruijie3GObjects_ObjectIdentity = ObjectIdentity
ruijie3GObjects = _Ruijie3GObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1)
)
_Ruijie3GTable_Object = MibTable
ruijie3GTable = _Ruijie3GTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1)
)
if mibBuilder.loadTexts:
    ruijie3GTable.setStatus("current")
_Ruijie3GEntry_Object = MibTableRow
ruijie3GEntry = _Ruijie3GEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1)
)
ruijie3GEntry.setIndexNames(
    (0, "RUIJIE-3G-MIB", "ruijie3GIPAddr"),
)
if mibBuilder.loadTexts:
    ruijie3GEntry.setStatus("current")
_Ruijie3gUsername_Type = DisplayString
_Ruijie3gUsername_Object = MibTableColumn
ruijie3gUsername = _Ruijie3gUsername_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 1),
    _Ruijie3gUsername_Type()
)
ruijie3gUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3gUsername.setStatus("current")


class _Ruijie3GOnlineStatus_Type(Integer32):
    """Custom type ruijie3GOnlineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("lpm", 0),
          ("online", 1),
          ("offline", 4),
          ("ftm", 5),
          ("reset", 6),
          ("rfOff", 7))
    )


_Ruijie3GOnlineStatus_Type.__name__ = "Integer32"
_Ruijie3GOnlineStatus_Object = MibTableColumn
ruijie3GOnlineStatus = _Ruijie3GOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 2),
    _Ruijie3GOnlineStatus_Type()
)
ruijie3GOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GOnlineStatus.setStatus("current")
_Ruijie3GIMEI_Type = DisplayString
_Ruijie3GIMEI_Object = MibTableColumn
ruijie3GIMEI = _Ruijie3GIMEI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 3),
    _Ruijie3GIMEI_Type()
)
ruijie3GIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GIMEI.setStatus("current")


class _Ruijie3GIPAddrType_Type(Integer32):
    """Custom type ruijie3GIPAddrType based on Integer32"""
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


_Ruijie3GIPAddrType_Type.__name__ = "Integer32"
_Ruijie3GIPAddrType_Object = MibTableColumn
ruijie3GIPAddrType = _Ruijie3GIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 4),
    _Ruijie3GIPAddrType_Type()
)
ruijie3GIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GIPAddrType.setStatus("current")
_Ruijie3GIPAddr_Type = IpAddress
_Ruijie3GIPAddr_Object = MibTableColumn
ruijie3GIPAddr = _Ruijie3GIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 5),
    _Ruijie3GIPAddr_Type()
)
ruijie3GIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GIPAddr.setStatus("current")
_Ruijie3GUplineTime_Type = TimeStamp
_Ruijie3GUplineTime_Object = MibTableColumn
ruijie3GUplineTime = _Ruijie3GUplineTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 6),
    _Ruijie3GUplineTime_Type()
)
ruijie3GUplineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GUplineTime.setStatus("current")


class _Ruijie3GActiveTime_Type(Integer32):
    """Custom type ruijie3GActiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ruijie3GActiveTime_Type.__name__ = "Integer32"
_Ruijie3GActiveTime_Object = MibTableColumn
ruijie3GActiveTime = _Ruijie3GActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 7),
    _Ruijie3GActiveTime_Type()
)
ruijie3GActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GActiveTime.setStatus("current")


class _Ruijie3GSignalStrength_Type(Integer32):
    """Custom type ruijie3GSignalStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Ruijie3GSignalStrength_Type.__name__ = "Integer32"
_Ruijie3GSignalStrength_Object = MibTableColumn
ruijie3GSignalStrength = _Ruijie3GSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 8),
    _Ruijie3GSignalStrength_Type()
)
ruijie3GSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GSignalStrength.setStatus("current")


class _Ruijie3GISP_Type(Integer32):
    """Custom type ruijie3GISP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chinaUnicom", 1),
          ("chinaTelecom", 2),
          ("chinaMobile", 3))
    )


_Ruijie3GISP_Type.__name__ = "Integer32"
_Ruijie3GISP_Object = MibTableColumn
ruijie3GISP = _Ruijie3GISP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 9),
    _Ruijie3GISP_Type()
)
ruijie3GISP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GISP.setStatus("current")


class _Ruijie3GSysMode_Type(Integer32):
    """Custom type ruijie3GSysMode based on Integer32"""
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
              10,
              15,
              100,
              101,
              110,
              111)
        )
    )
    namedValues = NamedValues(
        *(("noService", 0),
          ("amps", 1),
          ("cdma", 2),
          ("gsmGprs", 3),
          ("hdr", 4),
          ("wcdma", 5),
          ("gps", 6),
          ("gsmCdma", 7),
          ("cdmaHdrHybrid", 8),
          ("lte", 9),
          ("nr", 10),
          ("tdscdma", 15),
          ("td-1te", 100),
          ("fdd-lte", 101),
          ("eutran-5gc", 110),
          ("nr-5gc", 111))
    )


_Ruijie3GSysMode_Type.__name__ = "Integer32"
_Ruijie3GSysMode_Object = MibTableColumn
ruijie3GSysMode = _Ruijie3GSysMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 10),
    _Ruijie3GSysMode_Type()
)
ruijie3GSysMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GSysMode.setStatus("current")


class _Ruijie3GServiceStatus_Type(Integer32):
    """Custom type ruijie3GServiceStatus based on Integer32"""
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


_Ruijie3GServiceStatus_Type.__name__ = "Integer32"
_Ruijie3GServiceStatus_Object = MibTableColumn
ruijie3GServiceStatus = _Ruijie3GServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 11),
    _Ruijie3GServiceStatus_Type()
)
ruijie3GServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GServiceStatus.setStatus("current")


class _Ruijie3GRoamingStatus_Type(Integer32):
    """Custom type ruijie3GRoamingStatus based on Integer32"""
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


_Ruijie3GRoamingStatus_Type.__name__ = "Integer32"
_Ruijie3GRoamingStatus_Object = MibTableColumn
ruijie3GRoamingStatus = _Ruijie3GRoamingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 12),
    _Ruijie3GRoamingStatus_Type()
)
ruijie3GRoamingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GRoamingStatus.setStatus("current")


class _Ruijie3GDomain_Type(Integer32):
    """Custom type ruijie3GDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              100,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noService", 0),
          ("onlyCS", 1),
          ("onlyPS", 2),
          ("pSCS", 3),
          ("pSCSnotRegistered", 4),
          ("ePSService", 100),
          ("cdmaNotSupport", 255))
    )


_Ruijie3GDomain_Type.__name__ = "Integer32"
_Ruijie3GDomain_Object = MibTableColumn
ruijie3GDomain = _Ruijie3GDomain_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 13),
    _Ruijie3GDomain_Type()
)
ruijie3GDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GDomain.setStatus("current")


class _Ruijie3GSIMStatus_Type(Integer32):
    """Custom type ruijie3GSIMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("invalidUsimCard", 0),
          ("validUsimCard", 1),
          ("invalidForCS", 2),
          ("invalidForPS", 3),
          ("invalidForCSPS", 4),
          ("noUsimCard", 255))
    )


_Ruijie3GSIMStatus_Type.__name__ = "Integer32"
_Ruijie3GSIMStatus_Object = MibTableColumn
ruijie3GSIMStatus = _Ruijie3GSIMStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 14),
    _Ruijie3GSIMStatus_Type()
)
ruijie3GSIMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GSIMStatus.setStatus("current")


class _Ruijie3GSignalStrengthPercent_Type(Integer32):
    """Custom type ruijie3GSignalStrengthPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ruijie3GSignalStrengthPercent_Type.__name__ = "Integer32"
_Ruijie3GSignalStrengthPercent_Object = MibTableColumn
ruijie3GSignalStrengthPercent = _Ruijie3GSignalStrengthPercent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 15),
    _Ruijie3GSignalStrengthPercent_Type()
)
ruijie3GSignalStrengthPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GSignalStrengthPercent.setStatus("current")
_Ruijie3GApn_Type = DisplayString
_Ruijie3GApn_Object = MibTableColumn
ruijie3GApn = _Ruijie3GApn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 16),
    _Ruijie3GApn_Type()
)
ruijie3GApn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GApn.setStatus("current")


class _Ruijie3GCellID_Type(Integer32):
    """Custom type ruijie3GCellID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ruijie3GCellID_Type.__name__ = "Integer32"
_Ruijie3GCellID_Object = MibTableColumn
ruijie3GCellID = _Ruijie3GCellID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 17),
    _Ruijie3GCellID_Type()
)
ruijie3GCellID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GCellID.setStatus("current")


class _Ruijie3GLAC_Type(Integer32):
    """Custom type ruijie3GLAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ruijie3GLAC_Type.__name__ = "Integer32"
_Ruijie3GLAC_Object = MibTableColumn
ruijie3GLAC = _Ruijie3GLAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 18),
    _Ruijie3GLAC_Type()
)
ruijie3GLAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GLAC.setStatus("current")


class _Ruijie3GBSID_Type(Integer32):
    """Custom type ruijie3GBSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ruijie3GBSID_Type.__name__ = "Integer32"
_Ruijie3GBSID_Object = MibTableColumn
ruijie3GBSID = _Ruijie3GBSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 19),
    _Ruijie3GBSID_Type()
)
ruijie3GBSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GBSID.setStatus("current")


class _Ruijie3GNID_Type(Integer32):
    """Custom type ruijie3GNID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ruijie3GNID_Type.__name__ = "Integer32"
_Ruijie3GNID_Object = MibTableColumn
ruijie3GNID = _Ruijie3GNID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 20),
    _Ruijie3GNID_Type()
)
ruijie3GNID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GNID.setStatus("current")


class _Ruijie3GSID_Type(Integer32):
    """Custom type ruijie3GSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ruijie3GSID_Type.__name__ = "Integer32"
_Ruijie3GSID_Object = MibTableColumn
ruijie3GSID = _Ruijie3GSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 21),
    _Ruijie3GSID_Type()
)
ruijie3GSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GSID.setStatus("current")
_Ruijie3GIMSI_Type = DisplayString
_Ruijie3GIMSI_Object = MibTableColumn
ruijie3GIMSI = _Ruijie3GIMSI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 22),
    _Ruijie3GIMSI_Type()
)
ruijie3GIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GIMSI.setStatus("current")
_Ruijie3GESN_Type = DisplayString
_Ruijie3GESN_Object = MibTableColumn
ruijie3GESN = _Ruijie3GESN_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 23),
    _Ruijie3GESN_Type()
)
ruijie3GESN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GESN.setStatus("current")
_Ruijie3GPhoneNumber_Type = DisplayString
_Ruijie3GPhoneNumber_Object = MibTableColumn
ruijie3GPhoneNumber = _Ruijie3GPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 24),
    _Ruijie3GPhoneNumber_Type()
)
ruijie3GPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GPhoneNumber.setStatus("current")
_Ruijie3GifIndex_Type = Integer32
_Ruijie3GifIndex_Object = MibTableColumn
ruijie3GifIndex = _Ruijie3GifIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 25),
    _Ruijie3GifIndex_Type()
)
ruijie3GifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GifIndex.setStatus("current")
_Ruijie3GBSLONG_Type = Integer32
_Ruijie3GBSLONG_Object = MibTableColumn
ruijie3GBSLONG = _Ruijie3GBSLONG_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 26),
    _Ruijie3GBSLONG_Type()
)
ruijie3GBSLONG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GBSLONG.setStatus("current")
_Ruijie3GBSLAT_Type = Integer32
_Ruijie3GBSLAT_Object = MibTableColumn
ruijie3GBSLAT = _Ruijie3GBSLAT_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 27),
    _Ruijie3GBSLAT_Type()
)
ruijie3GBSLAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GBSLAT.setStatus("current")


class _Ruijie3GBackupInfo_Type(Integer32):
    """Custom type ruijie3GBackupInfo based on Integer32"""
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
        *(("no-backup", 0),
          ("myself", 1),
          ("master", 2),
          ("slave", 3))
    )


_Ruijie3GBackupInfo_Type.__name__ = "Integer32"
_Ruijie3GBackupInfo_Object = MibTableColumn
ruijie3GBackupInfo = _Ruijie3GBackupInfo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 28),
    _Ruijie3GBackupInfo_Type()
)
ruijie3GBackupInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GBackupInfo.setStatus("current")
_Ruijie3GSerialNumber_Type = DisplayString
_Ruijie3GSerialNumber_Object = MibTableColumn
ruijie3GSerialNumber = _Ruijie3GSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 29),
    _Ruijie3GSerialNumber_Type()
)
ruijie3GSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GSerialNumber.setStatus("current")
_Ruijie3GBackupIMSI_Type = DisplayString
_Ruijie3GBackupIMSI_Object = MibTableColumn
ruijie3GBackupIMSI = _Ruijie3GBackupIMSI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 30),
    _Ruijie3GBackupIMSI_Type()
)
ruijie3GBackupIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GBackupIMSI.setStatus("current")
_Ruijie3GGatewayIPAddr_Type = IpAddress
_Ruijie3GGatewayIPAddr_Object = MibTableColumn
ruijie3GGatewayIPAddr = _Ruijie3GGatewayIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 31),
    _Ruijie3GGatewayIPAddr_Type()
)
ruijie3GGatewayIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GGatewayIPAddr.setStatus("current")
_Ruijie3GLineDownCause_Type = Integer32
_Ruijie3GLineDownCause_Object = MibTableColumn
ruijie3GLineDownCause = _Ruijie3GLineDownCause_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 32),
    _Ruijie3GLineDownCause_Type()
)
ruijie3GLineDownCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GLineDownCause.setStatus("current")


class _Ruijie3GModemType_Type(Integer32):
    """Custom type ruijie3GModemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("modem-type-3G", 1),
          ("modem-type-4G", 2),
          ("modem-type-5G", 3))
    )


_Ruijie3GModemType_Type.__name__ = "Integer32"
_Ruijie3GModemType_Object = MibTableColumn
ruijie3GModemType = _Ruijie3GModemType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 1, 1, 33),
    _Ruijie3GModemType_Type()
)
ruijie3GModemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GModemType.setStatus("current")
_Ruijie3GStatTable_Object = MibTable
ruijie3GStatTable = _Ruijie3GStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 2)
)
if mibBuilder.loadTexts:
    ruijie3GStatTable.setStatus("current")
_Ruijie3GStatEntry_Object = MibTableRow
ruijie3GStatEntry = _Ruijie3GStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 2, 1)
)
ruijie3GStatEntry.setIndexNames(
    (0, "RUIJIE-3G-MIB", "ruijie3GIPAddr"),
)
if mibBuilder.loadTexts:
    ruijie3GStatEntry.setStatus("current")
_Ruijie3GInOctets_Type = Counter64
_Ruijie3GInOctets_Object = MibTableColumn
ruijie3GInOctets = _Ruijie3GInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 2, 1, 1),
    _Ruijie3GInOctets_Type()
)
ruijie3GInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GInOctets.setStatus("current")
_Ruijie3GOutOctets_Type = Counter64
_Ruijie3GOutOctets_Object = MibTableColumn
ruijie3GOutOctets = _Ruijie3GOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 2, 1, 2),
    _Ruijie3GOutOctets_Type()
)
ruijie3GOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GOutOctets.setStatus("current")
_Ruijie3GInSpeed_Type = Counter64
_Ruijie3GInSpeed_Object = MibTableColumn
ruijie3GInSpeed = _Ruijie3GInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 2, 1, 3),
    _Ruijie3GInSpeed_Type()
)
ruijie3GInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GInSpeed.setStatus("current")
_Ruijie3GOutSpeed_Type = Counter64
_Ruijie3GOutSpeed_Object = MibTableColumn
ruijie3GOutSpeed = _Ruijie3GOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 2, 1, 4),
    _Ruijie3GOutSpeed_Type()
)
ruijie3GOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GOutSpeed.setStatus("current")
_Ruijie3G2IMSI_Type = DisplayString
_Ruijie3G2IMSI_Object = MibTableColumn
ruijie3G2IMSI = _Ruijie3G2IMSI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 2, 1, 5),
    _Ruijie3G2IMSI_Type()
)
ruijie3G2IMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3G2IMSI.setStatus("current")
_Ruijie3G2ifIndex_Type = Integer32
_Ruijie3G2ifIndex_Object = MibTableColumn
ruijie3G2ifIndex = _Ruijie3G2ifIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 2, 1, 6),
    _Ruijie3G2ifIndex_Type()
)
ruijie3G2ifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3G2ifIndex.setStatus("current")
_Ruijie3GTrap_ObjectIdentity = ObjectIdentity
ruijie3GTrap = _Ruijie3GTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 3)
)
_Ruijie3GNotifications_ObjectIdentity = ObjectIdentity
ruijie3GNotifications = _Ruijie3GNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 3, 1)
)
_Ruijie3GBsNumber_Type = Integer32
_Ruijie3GBsNumber_Object = MibScalar
ruijie3GBsNumber = _Ruijie3GBsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 4),
    _Ruijie3GBsNumber_Type()
)
ruijie3GBsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GBsNumber.setStatus("current")
_Ruijie3GBsTable_Object = MibTable
ruijie3GBsTable = _Ruijie3GBsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 5)
)
if mibBuilder.loadTexts:
    ruijie3GBsTable.setStatus("current")
_Ruijie3GBsEntry_Object = MibTableRow
ruijie3GBsEntry = _Ruijie3GBsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 5, 1)
)
ruijie3GBsEntry.setIndexNames(
    (0, "RUIJIE-3G-MIB", "ruijie3GBsSN"),
)
if mibBuilder.loadTexts:
    ruijie3GBsEntry.setStatus("current")
_Ruijie3GBsSN_Type = Integer32
_Ruijie3GBsSN_Object = MibTableColumn
ruijie3GBsSN = _Ruijie3GBsSN_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 5, 1, 1),
    _Ruijie3GBsSN_Type()
)
ruijie3GBsSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GBsSN.setStatus("current")


class _Ruijie3GBsISP_Type(Integer32):
    """Custom type ruijie3GBsISP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chinaUnicom", 1),
          ("chinaTelecom", 2),
          ("chinaMobile", 3))
    )


_Ruijie3GBsISP_Type.__name__ = "Integer32"
_Ruijie3GBsISP_Object = MibTableColumn
ruijie3GBsISP = _Ruijie3GBsISP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 5, 1, 2),
    _Ruijie3GBsISP_Type()
)
ruijie3GBsISP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GBsISP.setStatus("current")


class _Ruijie3GBsMode_Type(Integer32):
    """Custom type ruijie3GBsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sys2GMode", 1),
          ("sys3GMode", 2))
    )


_Ruijie3GBsMode_Type.__name__ = "Integer32"
_Ruijie3GBsMode_Object = MibTableColumn
ruijie3GBsMode = _Ruijie3GBsMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 5, 1, 3),
    _Ruijie3GBsMode_Type()
)
ruijie3GBsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GBsMode.setStatus("current")
_Ruijie3GBsIMSI_Type = DisplayString
_Ruijie3GBsIMSI_Object = MibTableColumn
ruijie3GBsIMSI = _Ruijie3GBsIMSI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 5, 1, 4),
    _Ruijie3GBsIMSI_Type()
)
ruijie3GBsIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GBsIMSI.setStatus("current")
_Ruijie3GBsLAC_Type = Integer32
_Ruijie3GBsLAC_Object = MibTableColumn
ruijie3GBsLAC = _Ruijie3GBsLAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 5, 1, 5),
    _Ruijie3GBsLAC_Type()
)
ruijie3GBsLAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GBsLAC.setStatus("current")
_Ruijie3GBsCellID_Type = Integer32
_Ruijie3GBsCellID_Object = MibTableColumn
ruijie3GBsCellID = _Ruijie3GBsCellID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 5, 1, 6),
    _Ruijie3GBsCellID_Type()
)
ruijie3GBsCellID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GBsCellID.setStatus("current")
_Ruijie3GBsBSID_Type = Integer32
_Ruijie3GBsBSID_Object = MibTableColumn
ruijie3GBsBSID = _Ruijie3GBsBSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 5, 1, 7),
    _Ruijie3GBsBSID_Type()
)
ruijie3GBsBSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GBsBSID.setStatus("current")
_Ruijie3GBsSID_Type = Integer32
_Ruijie3GBsSID_Object = MibTableColumn
ruijie3GBsSID = _Ruijie3GBsSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 5, 1, 8),
    _Ruijie3GBsSID_Type()
)
ruijie3GBsSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GBsSID.setStatus("current")
_Ruijie3GBsNID_Type = Integer32
_Ruijie3GBsNID_Object = MibTableColumn
ruijie3GBsNID = _Ruijie3GBsNID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 5, 1, 9),
    _Ruijie3GBsNID_Type()
)
ruijie3GBsNID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GBsNID.setStatus("current")
_Ruijie3GBsRssi_Type = Integer32
_Ruijie3GBsRssi_Object = MibTableColumn
ruijie3GBsRssi = _Ruijie3GBsRssi_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 5, 1, 10),
    _Ruijie3GBsRssi_Type()
)
ruijie3GBsRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GBsRssi.setStatus("current")
_Ruijie3GBsBSLONG_Type = Integer32
_Ruijie3GBsBSLONG_Object = MibTableColumn
ruijie3GBsBSLONG = _Ruijie3GBsBSLONG_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 5, 1, 11),
    _Ruijie3GBsBSLONG_Type()
)
ruijie3GBsBSLONG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GBsBSLONG.setStatus("current")
_Ruijie3GBsBSLAT_Type = Integer32
_Ruijie3GBsBSLAT_Object = MibTableColumn
ruijie3GBsBSLAT = _Ruijie3GBsBSLAT_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 5, 1, 12),
    _Ruijie3GBsBSLAT_Type()
)
ruijie3GBsBSLAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GBsBSLAT.setStatus("current")
_Ruijie3GDeviceManagementTable_Object = MibTable
ruijie3GDeviceManagementTable = _Ruijie3GDeviceManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6)
)
if mibBuilder.loadTexts:
    ruijie3GDeviceManagementTable.setStatus("current")
_Ruijie3GDeviceManagementEntry_Object = MibTableRow
ruijie3GDeviceManagementEntry = _Ruijie3GDeviceManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1)
)
ruijie3GDeviceManagementEntry.setIndexNames(
    (0, "RUIJIE-3G-MIB", "ruijie3GRouterSlotNumber"),
)
if mibBuilder.loadTexts:
    ruijie3GDeviceManagementEntry.setStatus("current")
_Ruijie3GRouterType_Type = DisplayString
_Ruijie3GRouterType_Object = MibTableColumn
ruijie3GRouterType = _Ruijie3GRouterType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 1),
    _Ruijie3GRouterType_Type()
)
ruijie3GRouterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GRouterType.setStatus("current")
_Ruijie3GRouterSN_Type = DisplayString
_Ruijie3GRouterSN_Object = MibTableColumn
ruijie3GRouterSN = _Ruijie3GRouterSN_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 2),
    _Ruijie3GRouterSN_Type()
)
ruijie3GRouterSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GRouterSN.setStatus("current")
_Ruijie3GRouterSlotNumber_Type = DisplayString
_Ruijie3GRouterSlotNumber_Object = MibTableColumn
ruijie3GRouterSlotNumber = _Ruijie3GRouterSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 3),
    _Ruijie3GRouterSlotNumber_Type()
)
ruijie3GRouterSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GRouterSlotNumber.setStatus("current")
_Ruijie3GLineCardType_Type = DisplayString
_Ruijie3GLineCardType_Object = MibTableColumn
ruijie3GLineCardType = _Ruijie3GLineCardType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 4),
    _Ruijie3GLineCardType_Type()
)
ruijie3GLineCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GLineCardType.setStatus("current")
_Ruijie3GCardIMSI_Type = DisplayString
_Ruijie3GCardIMSI_Object = MibTableColumn
ruijie3GCardIMSI = _Ruijie3GCardIMSI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 5),
    _Ruijie3GCardIMSI_Type()
)
ruijie3GCardIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GCardIMSI.setStatus("current")
_Ruijie3GModemIMEI_Type = DisplayString
_Ruijie3GModemIMEI_Object = MibTableColumn
ruijie3GModemIMEI = _Ruijie3GModemIMEI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 6),
    _Ruijie3GModemIMEI_Type()
)
ruijie3GModemIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GModemIMEI.setStatus("current")
_Ruijie3GIntfIPAddr_Type = IpAddress
_Ruijie3GIntfIPAddr_Object = MibTableColumn
ruijie3GIntfIPAddr = _Ruijie3GIntfIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 7),
    _Ruijie3GIntfIPAddr_Type()
)
ruijie3GIntfIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GIntfIPAddr.setStatus("current")
_Ruijie3GCardPhoneNumber_Type = DisplayString
_Ruijie3GCardPhoneNumber_Object = MibTableColumn
ruijie3GCardPhoneNumber = _Ruijie3GCardPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 8),
    _Ruijie3GCardPhoneNumber_Type()
)
ruijie3GCardPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GCardPhoneNumber.setStatus("current")
_Ruijie3GLineDetected_Type = Unsigned32
_Ruijie3GLineDetected_Object = MibTableColumn
ruijie3GLineDetected = _Ruijie3GLineDetected_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 9),
    _Ruijie3GLineDetected_Type()
)
ruijie3GLineDetected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijie3GLineDetected.setStatus("current")


class _Ruijie3GLineDetectedResult_Type(Integer32):
    """Custom type ruijie3GLineDetectedResult based on Integer32"""
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
        *(("noRsponse", 0),
          ("pass", 1),
          ("failed", 2),
          ("using", 3),
          ("detecting", 4))
    )


_Ruijie3GLineDetectedResult_Type.__name__ = "Integer32"
_Ruijie3GLineDetectedResult_Object = MibTableColumn
ruijie3GLineDetectedResult = _Ruijie3GLineDetectedResult_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 10),
    _Ruijie3GLineDetectedResult_Type()
)
ruijie3GLineDetectedResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GLineDetectedResult.setStatus("current")


class _Ruijie3GLineDetectedMainCause_Type(Integer32):
    """Custom type ruijie3GLineDetectedMainCause based on Integer32"""
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
        *(("noGivenReason", 0),
          ("dialFailed", 1),
          ("pppFailed", 2),
          ("ipsecSetupFailed", 3))
    )


_Ruijie3GLineDetectedMainCause_Type.__name__ = "Integer32"
_Ruijie3GLineDetectedMainCause_Object = MibTableColumn
ruijie3GLineDetectedMainCause = _Ruijie3GLineDetectedMainCause_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 11),
    _Ruijie3GLineDetectedMainCause_Type()
)
ruijie3GLineDetectedMainCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GLineDetectedMainCause.setStatus("current")


class _Ruijie3GLineDetectedSubCause_Type(Integer32):
    """Custom type ruijie3GLineDetectedSubCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noGivenReason", 0),
          ("simCardInvalid", 1),
          ("aPNInvalid", 2),
          ("powerlower", 3),
          ("userInfoError", 4),
          ("ipsecSetupFailed", 5))
    )


_Ruijie3GLineDetectedSubCause_Type.__name__ = "Integer32"
_Ruijie3GLineDetectedSubCause_Object = MibTableColumn
ruijie3GLineDetectedSubCause = _Ruijie3GLineDetectedSubCause_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 12),
    _Ruijie3GLineDetectedSubCause_Type()
)
ruijie3GLineDetectedSubCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GLineDetectedSubCause.setStatus("current")


class _Ruijie3GDeviceBackupInfo_Type(Integer32):
    """Custom type ruijie3GDeviceBackupInfo based on Integer32"""
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
        *(("no-backup", 0),
          ("myself", 1),
          ("master", 2),
          ("slave", 3))
    )


_Ruijie3GDeviceBackupInfo_Type.__name__ = "Integer32"
_Ruijie3GDeviceBackupInfo_Object = MibTableColumn
ruijie3GDeviceBackupInfo = _Ruijie3GDeviceBackupInfo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 13),
    _Ruijie3GDeviceBackupInfo_Type()
)
ruijie3GDeviceBackupInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GDeviceBackupInfo.setStatus("current")


class _Ruijie3GRssiStrength_Type(Integer32):
    """Custom type ruijie3GRssiStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Ruijie3GRssiStrength_Type.__name__ = "Integer32"
_Ruijie3GRssiStrength_Object = MibTableColumn
ruijie3GRssiStrength = _Ruijie3GRssiStrength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 14),
    _Ruijie3GRssiStrength_Type()
)
ruijie3GRssiStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GRssiStrength.setStatus("current")


class _Ruijie3GRssiStrengthPercent_Type(Integer32):
    """Custom type ruijie3GRssiStrengthPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ruijie3GRssiStrengthPercent_Type.__name__ = "Integer32"
_Ruijie3GRssiStrengthPercent_Object = MibTableColumn
ruijie3GRssiStrengthPercent = _Ruijie3GRssiStrengthPercent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 15),
    _Ruijie3GRssiStrengthPercent_Type()
)
ruijie3GRssiStrengthPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GRssiStrengthPercent.setStatus("current")


class _Ruijie3GNetworkISPMode_Type(Integer32):
    """Custom type ruijie3GNetworkISPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chinaUnicom", 1),
          ("chinaTelecom", 2),
          ("chinaMobile", 3))
    )


_Ruijie3GNetworkISPMode_Type.__name__ = "Integer32"
_Ruijie3GNetworkISPMode_Object = MibTableColumn
ruijie3GNetworkISPMode = _Ruijie3GNetworkISPMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 16),
    _Ruijie3GNetworkISPMode_Type()
)
ruijie3GNetworkISPMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GNetworkISPMode.setStatus("current")


class _Ruijie3GNetworkSysMode_Type(Integer32):
    """Custom type ruijie3GNetworkSysMode based on Integer32"""
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
              10,
              15,
              100,
              101,
              110,
              111)
        )
    )
    namedValues = NamedValues(
        *(("noService", 0),
          ("amps", 1),
          ("cdma", 2),
          ("gsmGprs", 3),
          ("hdr", 4),
          ("wcdma", 5),
          ("gps", 6),
          ("gsmCdma", 7),
          ("cdmaHdrHybrid", 8),
          ("lte", 9),
          ("nr", 10),
          ("td-scdma", 15),
          ("td-1te", 100),
          ("fdd-lte", 101),
          ("eutran-5gc", 110),
          ("nr-5gc", 111))
    )


_Ruijie3GNetworkSysMode_Type.__name__ = "Integer32"
_Ruijie3GNetworkSysMode_Object = MibTableColumn
ruijie3GNetworkSysMode = _Ruijie3GNetworkSysMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 17),
    _Ruijie3GNetworkSysMode_Type()
)
ruijie3GNetworkSysMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijie3GNetworkSysMode.setStatus("current")


class _Ruijie3GNetworkServiceStatus_Type(Integer32):
    """Custom type ruijie3GNetworkServiceStatus based on Integer32"""
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


_Ruijie3GNetworkServiceStatus_Type.__name__ = "Integer32"
_Ruijie3GNetworkServiceStatus_Object = MibTableColumn
ruijie3GNetworkServiceStatus = _Ruijie3GNetworkServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 18),
    _Ruijie3GNetworkServiceStatus_Type()
)
ruijie3GNetworkServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GNetworkServiceStatus.setStatus("current")


class _Ruijie3GSIMCardStatus_Type(Integer32):
    """Custom type ruijie3GSIMCardStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("invalidUsimCard", 0),
          ("validUsimCard", 1),
          ("invalidForCS", 2),
          ("invalidForPS", 3),
          ("invalidForCSPS", 4),
          ("noUsimCard", 255))
    )


_Ruijie3GSIMCardStatus_Type.__name__ = "Integer32"
_Ruijie3GSIMCardStatus_Object = MibTableColumn
ruijie3GSIMCardStatus = _Ruijie3GSIMCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 19),
    _Ruijie3GSIMCardStatus_Type()
)
ruijie3GSIMCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GSIMCardStatus.setStatus("current")


class _Ruijie3GDailMode_Type(Integer32):
    """Custom type ruijie3GDailMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dialOnDemand", 0),
          ("autoDail", 1))
    )


_Ruijie3GDailMode_Type.__name__ = "Integer32"
_Ruijie3GDailMode_Object = MibTableColumn
ruijie3GDailMode = _Ruijie3GDailMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 20),
    _Ruijie3GDailMode_Type()
)
ruijie3GDailMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijie3GDailMode.setStatus("current")
_Ruijie3GDeviceBackupIMSI_Type = DisplayString
_Ruijie3GDeviceBackupIMSI_Object = MibTableColumn
ruijie3GDeviceBackupIMSI = _Ruijie3GDeviceBackupIMSI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 21),
    _Ruijie3GDeviceBackupIMSI_Type()
)
ruijie3GDeviceBackupIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GDeviceBackupIMSI.setStatus("current")


class _Ruijie3GLineDetectedMode_Type(Integer32):
    """Custom type ruijie3GLineDetectedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vpdnMode", 0),
          ("ipsecMode", 1))
    )


_Ruijie3GLineDetectedMode_Type.__name__ = "Integer32"
_Ruijie3GLineDetectedMode_Object = MibTableColumn
ruijie3GLineDetectedMode = _Ruijie3GLineDetectedMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 22),
    _Ruijie3GLineDetectedMode_Type()
)
ruijie3GLineDetectedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijie3GLineDetectedMode.setStatus("current")
_Ruijie3GPppUsername_Type = DisplayString
_Ruijie3GPppUsername_Object = MibTableColumn
ruijie3GPppUsername = _Ruijie3GPppUsername_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 23),
    _Ruijie3GPppUsername_Type()
)
ruijie3GPppUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijie3GPppUsername.setStatus("current")
_Ruijie3GUserApn_Type = DisplayString
_Ruijie3GUserApn_Object = MibTableColumn
ruijie3GUserApn = _Ruijie3GUserApn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 24),
    _Ruijie3GUserApn_Type()
)
ruijie3GUserApn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijie3GUserApn.setStatus("current")


class _Ruijie3GModemOnlineStatus_Type(Integer32):
    """Custom type ruijie3GModemOnlineStatus based on Integer32"""
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


_Ruijie3GModemOnlineStatus_Type.__name__ = "Integer32"
_Ruijie3GModemOnlineStatus_Object = MibTableColumn
ruijie3GModemOnlineStatus = _Ruijie3GModemOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 25),
    _Ruijie3GModemOnlineStatus_Type()
)
ruijie3GModemOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GModemOnlineStatus.setStatus("current")


class _Ruijie3GIntfIPAddrType_Type(Integer32):
    """Custom type ruijie3GIntfIPAddrType based on Integer32"""
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


_Ruijie3GIntfIPAddrType_Type.__name__ = "Integer32"
_Ruijie3GIntfIPAddrType_Object = MibTableColumn
ruijie3GIntfIPAddrType = _Ruijie3GIntfIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 26),
    _Ruijie3GIntfIPAddrType_Type()
)
ruijie3GIntfIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GIntfIPAddrType.setStatus("current")
_Ruijie3GUserUplineTime_Type = TimeStamp
_Ruijie3GUserUplineTime_Object = MibTableColumn
ruijie3GUserUplineTime = _Ruijie3GUserUplineTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 27),
    _Ruijie3GUserUplineTime_Type()
)
ruijie3GUserUplineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GUserUplineTime.setStatus("current")


class _Ruijie3GUserActiveTime_Type(Integer32):
    """Custom type ruijie3GUserActiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ruijie3GUserActiveTime_Type.__name__ = "Integer32"
_Ruijie3GUserActiveTime_Object = MibTableColumn
ruijie3GUserActiveTime = _Ruijie3GUserActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 28),
    _Ruijie3GUserActiveTime_Type()
)
ruijie3GUserActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GUserActiveTime.setStatus("current")


class _Ruijie3GSIMRoamingStatus_Type(Integer32):
    """Custom type ruijie3GSIMRoamingStatus based on Integer32"""
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


_Ruijie3GSIMRoamingStatus_Type.__name__ = "Integer32"
_Ruijie3GSIMRoamingStatus_Object = MibTableColumn
ruijie3GSIMRoamingStatus = _Ruijie3GSIMRoamingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 29),
    _Ruijie3GSIMRoamingStatus_Type()
)
ruijie3GSIMRoamingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GSIMRoamingStatus.setStatus("current")


class _Ruijie3GAcessBSCellID_Type(Integer32):
    """Custom type ruijie3GAcessBSCellID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ruijie3GAcessBSCellID_Type.__name__ = "Integer32"
_Ruijie3GAcessBSCellID_Object = MibTableColumn
ruijie3GAcessBSCellID = _Ruijie3GAcessBSCellID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 30),
    _Ruijie3GAcessBSCellID_Type()
)
ruijie3GAcessBSCellID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GAcessBSCellID.setStatus("current")


class _Ruijie3GAcessBSLAC_Type(Integer32):
    """Custom type ruijie3GAcessBSLAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ruijie3GAcessBSLAC_Type.__name__ = "Integer32"
_Ruijie3GAcessBSLAC_Object = MibTableColumn
ruijie3GAcessBSLAC = _Ruijie3GAcessBSLAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 31),
    _Ruijie3GAcessBSLAC_Type()
)
ruijie3GAcessBSLAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GAcessBSLAC.setStatus("current")
_Ruijie3GAcessBSLONG_Type = Integer32
_Ruijie3GAcessBSLONG_Object = MibTableColumn
ruijie3GAcessBSLONG = _Ruijie3GAcessBSLONG_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 32),
    _Ruijie3GAcessBSLONG_Type()
)
ruijie3GAcessBSLONG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GAcessBSLONG.setStatus("current")
_Ruijie3GAcessBSLAT_Type = Integer32
_Ruijie3GAcessBSLAT_Object = MibTableColumn
ruijie3GAcessBSLAT = _Ruijie3GAcessBSLAT_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 33),
    _Ruijie3GAcessBSLAT_Type()
)
ruijie3GAcessBSLAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GAcessBSLAT.setStatus("current")
_Ruijie3GDialOnDemandIfIndex_Type = Integer32
_Ruijie3GDialOnDemandIfIndex_Object = MibTableColumn
ruijie3GDialOnDemandIfIndex = _Ruijie3GDialOnDemandIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 34),
    _Ruijie3GDialOnDemandIfIndex_Type()
)
ruijie3GDialOnDemandIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GDialOnDemandIfIndex.setStatus("current")


class _Ruijie3GTrafficPreventMode_Type(Integer32):
    """Custom type ruijie3GTrafficPreventMode based on Integer32"""
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


_Ruijie3GTrafficPreventMode_Type.__name__ = "Integer32"
_Ruijie3GTrafficPreventMode_Object = MibTableColumn
ruijie3GTrafficPreventMode = _Ruijie3GTrafficPreventMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 35),
    _Ruijie3GTrafficPreventMode_Type()
)
ruijie3GTrafficPreventMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GTrafficPreventMode.setStatus("current")
_Ruijie3GTrafficPreventIfIndex_Type = Integer32
_Ruijie3GTrafficPreventIfIndex_Object = MibTableColumn
ruijie3GTrafficPreventIfIndex = _Ruijie3GTrafficPreventIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 36),
    _Ruijie3GTrafficPreventIfIndex_Type()
)
ruijie3GTrafficPreventIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GTrafficPreventIfIndex.setStatus("current")
_Ruijie3GTrafficPreventListID_Type = Integer32
_Ruijie3GTrafficPreventListID_Object = MibTableColumn
ruijie3GTrafficPreventListID = _Ruijie3GTrafficPreventListID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 37),
    _Ruijie3GTrafficPreventListID_Type()
)
ruijie3GTrafficPreventListID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GTrafficPreventListID.setStatus("current")
_Ruijie3GTrafficPreventListName_Type = DisplayString
_Ruijie3GTrafficPreventListName_Object = MibTableColumn
ruijie3GTrafficPreventListName = _Ruijie3GTrafficPreventListName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 38),
    _Ruijie3GTrafficPreventListName_Type()
)
ruijie3GTrafficPreventListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GTrafficPreventListName.setStatus("current")


class _Ruijie3GDeviceModemType_Type(Integer32):
    """Custom type ruijie3GDeviceModemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("modem-type-3G", 1),
          ("modem-type-4G", 2),
          ("modem-type-5G", 3))
    )


_Ruijie3GDeviceModemType_Type.__name__ = "Integer32"
_Ruijie3GDeviceModemType_Object = MibTableColumn
ruijie3GDeviceModemType = _Ruijie3GDeviceModemType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 39),
    _Ruijie3GDeviceModemType_Type()
)
ruijie3GDeviceModemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GDeviceModemType.setStatus("current")


class _Ruijie3GTrafficTrapInterval_Type(Integer32):
    """Custom type ruijie3GTrafficTrapInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_Ruijie3GTrafficTrapInterval_Type.__name__ = "Integer32"
_Ruijie3GTrafficTrapInterval_Object = MibTableColumn
ruijie3GTrafficTrapInterval = _Ruijie3GTrafficTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 40),
    _Ruijie3GTrafficTrapInterval_Type()
)
ruijie3GTrafficTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijie3GTrafficTrapInterval.setStatus("current")


class _Ruijie3GRssiThreshold_Type(Integer32):
    """Custom type ruijie3GRssiThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Ruijie3GRssiThreshold_Type.__name__ = "Integer32"
_Ruijie3GRssiThreshold_Object = MibTableColumn
ruijie3GRssiThreshold = _Ruijie3GRssiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 41),
    _Ruijie3GRssiThreshold_Type()
)
ruijie3GRssiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijie3GRssiThreshold.setStatus("current")


class _Ruijie3GTrapFilterMode_Type(Integer32):
    """Custom type ruijie3GTrapFilterMode based on Integer32"""
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


_Ruijie3GTrapFilterMode_Type.__name__ = "Integer32"
_Ruijie3GTrapFilterMode_Object = MibTableColumn
ruijie3GTrapFilterMode = _Ruijie3GTrapFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 42),
    _Ruijie3GTrapFilterMode_Type()
)
ruijie3GTrapFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijie3GTrapFilterMode.setStatus("current")


class _Ruijie3GISPtimeout_Type(Integer32):
    """Custom type ruijie3GISPtimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 36000),
    )


_Ruijie3GISPtimeout_Type.__name__ = "Integer32"
_Ruijie3GISPtimeout_Object = MibTableColumn
ruijie3GISPtimeout = _Ruijie3GISPtimeout_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 43),
    _Ruijie3GISPtimeout_Type()
)
ruijie3GISPtimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijie3GISPtimeout.setStatus("current")


class _Ruijie3GEncryptType_Type(Integer32):
    """Custom type ruijie3GEncryptType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              7)
        )
    )
    namedValues = NamedValues(
        *(("encryptNone", 0),
          ("encryptTemp", 7))
    )


_Ruijie3GEncryptType_Type.__name__ = "Integer32"
_Ruijie3GEncryptType_Object = MibTableColumn
ruijie3GEncryptType = _Ruijie3GEncryptType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 44),
    _Ruijie3GEncryptType_Type()
)
ruijie3GEncryptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijie3GEncryptType.setStatus("current")
_Ruijie3GPassword_Type = DisplayString
_Ruijie3GPassword_Object = MibTableColumn
ruijie3GPassword = _Ruijie3GPassword_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 45),
    _Ruijie3GPassword_Type()
)
ruijie3GPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijie3GPassword.setStatus("current")
_Ruijie3GNetworkISPName_Type = DisplayString
_Ruijie3GNetworkISPName_Object = MibTableColumn
ruijie3GNetworkISPName = _Ruijie3GNetworkISPName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 46),
    _Ruijie3GNetworkISPName_Type()
)
ruijie3GNetworkISPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijie3GNetworkISPName.setStatus("current")


class _RuijieSIMValidSlot_Type(Integer32):
    """Custom type ruijieSIMValidSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_RuijieSIMValidSlot_Type.__name__ = "Integer32"
_RuijieSIMValidSlot_Object = MibTableColumn
ruijieSIMValidSlot = _RuijieSIMValidSlot_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 47),
    _RuijieSIMValidSlot_Type()
)
ruijieSIMValidSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSIMValidSlot.setStatus("current")


class _RuijieSIMInUseSlot_Type(Integer32):
    """Custom type ruijieSIMInUseSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_RuijieSIMInUseSlot_Type.__name__ = "Integer32"
_RuijieSIMInUseSlot_Object = MibTableColumn
ruijieSIMInUseSlot = _RuijieSIMInUseSlot_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 6, 1, 48),
    _RuijieSIMInUseSlot_Type()
)
ruijieSIMInUseSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSIMInUseSlot.setStatus("current")
_Ruijie3GTrapNew_ObjectIdentity = ObjectIdentity
ruijie3GTrapNew = _Ruijie3GTrapNew_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 2)
)
_Ruijie3GNotificationsNew_ObjectIdentity = ObjectIdentity
ruijie3GNotificationsNew = _Ruijie3GNotificationsNew_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 2, 1)
)

# Managed Objects groups


# Notification objects

ruijie3GSignalThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 3, 1, 1)
)
ruijie3GSignalThreshold.setObjects(
      *(("RUIJIE-3G-MIB", "ruijie3GIPAddr"),
        ("RUIJIE-3G-MIB", "ruijie3GSignalStrength"),
        ("RUIJIE-3G-MIB", "ruijie3GSignalStrengthPercent"),
        ("RUIJIE-3G-MIB", "ruijie3GIMSI"))
)
if mibBuilder.loadTexts:
    ruijie3GSignalThreshold.setStatus(
        "current"
    )

ruijie3GUpLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 3, 1, 2)
)
ruijie3GUpLine.setObjects(
      *(("RUIJIE-3G-MIB", "ruijie3GIPAddr"),
        ("RUIJIE-3G-MIB", "ruijie3gUsername"),
        ("RUIJIE-3G-MIB", "ruijie3GIMSI"),
        ("RUIJIE-3G-MIB", "ruijie3GBackupInfo"),
        ("RUIJIE-3G-MIB", "ruijie3GSerialNumber"),
        ("RUIJIE-3G-MIB", "ruijie3GGatewayIPAddr"))
)
if mibBuilder.loadTexts:
    ruijie3GUpLine.setStatus(
        "current"
    )

ruijie3GDownLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 3, 1, 3)
)
ruijie3GDownLine.setObjects(
      *(("RUIJIE-3G-MIB", "ruijie3GLineDownCause"),
        ("RUIJIE-3G-MIB", "ruijie3GIPAddr"),
        ("RUIJIE-3G-MIB", "ruijie3gUsername"),
        ("RUIJIE-3G-MIB", "ruijie3GIMSI"))
)
if mibBuilder.loadTexts:
    ruijie3GDownLine.setStatus(
        "current"
    )

ruijie3GChangeAccessPoint = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 3, 1, 4)
)
ruijie3GChangeAccessPoint.setObjects(
      *(("RUIJIE-3G-MIB", "ruijie3GIPAddr"),
        ("RUIJIE-3G-MIB", "ruijie3GApn"),
        ("RUIJIE-3G-MIB", "ruijie3gUsername"),
        ("RUIJIE-3G-MIB", "ruijie3GIMSI"))
)
if mibBuilder.loadTexts:
    ruijie3GChangeAccessPoint.setStatus(
        "current"
    )

ruijie3GBackupIntfSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 3, 1, 5)
)
ruijie3GBackupIntfSwitch.setObjects(
      *(("RUIJIE-3G-MIB", "ruijie3GIPAddr"),
        ("RUIJIE-3G-MIB", "ruijie3gUsername"),
        ("RUIJIE-3G-MIB", "ruijie3GIMSI"),
        ("RUIJIE-3G-MIB", "ruijie3GSerialNumber"),
        ("RUIJIE-3G-MIB", "ruijie3GBackupIMSI"))
)
if mibBuilder.loadTexts:
    ruijie3GBackupIntfSwitch.setStatus(
        "current"
    )

ruijie3GBaseSationSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 3, 1, 6)
)
ruijie3GBaseSationSwitch.setObjects(
      *(("RUIJIE-3G-MIB", "ruijie3GISP"),
        ("RUIJIE-3G-MIB", "ruijie3GCellID"),
        ("RUIJIE-3G-MIB", "ruijie3GLAC"),
        ("RUIJIE-3G-MIB", "ruijie3GBSID"),
        ("RUIJIE-3G-MIB", "ruijie3GSID"),
        ("RUIJIE-3G-MIB", "ruijie3GNID"),
        ("RUIJIE-3G-MIB", "ruijie3GIMSI"),
        ("RUIJIE-3G-MIB", "ruijie3GPhoneNumber"))
)
if mibBuilder.loadTexts:
    ruijie3GBaseSationSwitch.setStatus(
        "current"
    )

ruijie3GTrafficInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 1, 3, 1, 7)
)
ruijie3GTrafficInformation.setObjects(
      *(("RUIJIE-3G-MIB", "ruijie3GIPAddr"),
        ("RUIJIE-3G-MIB", "ruijie3GIMSI"),
        ("RUIJIE-3G-MIB", "ruijie3GSerialNumber"),
        ("RUIJIE-3G-MIB", "ruijie3GInOctets"),
        ("RUIJIE-3G-MIB", "ruijie3GOutOctets"))
)
if mibBuilder.loadTexts:
    ruijie3GTrafficInformation.setStatus(
        "current"
    )

ruijie3GLineDetectedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 2, 1, 1)
)
ruijie3GLineDetectedNotification.setObjects(
      *(("RUIJIE-3G-MIB", "ruijie3GRouterSN"),
        ("RUIJIE-3G-MIB", "ruijie3GCardIMSI"),
        ("RUIJIE-3G-MIB", "ruijie3GIntfIPAddr"),
        ("RUIJIE-3G-MIB", "ruijie3GLineDetected"),
        ("RUIJIE-3G-MIB", "ruijie3GLineDetectedResult"),
        ("RUIJIE-3G-MIB", "ruijie3GLineDetectedMainCause"),
        ("RUIJIE-3G-MIB", "ruijie3GLineDetectedSubCause"),
        ("RUIJIE-3G-MIB", "ruijie3GDeviceBackupInfo"),
        ("RUIJIE-3G-MIB", "ruijie3GRssiStrength"),
        ("RUIJIE-3G-MIB", "ruijie3GDeviceBackupIMSI"))
)
if mibBuilder.loadTexts:
    ruijie3GLineDetectedNotification.setStatus(
        "current"
    )

ruijie3GUserUpLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 2, 1, 2)
)
ruijie3GUserUpLine.setObjects(
      *(("RUIJIE-3G-MIB", "ruijie3GRouterSlotNumber"),
        ("RUIJIE-3G-MIB", "ruijie3GCardIMSI"),
        ("RUIJIE-3G-MIB", "ruijie3GIntfIPAddr"),
        ("RUIJIE-3G-MIB", "ruijie3GTrafficPreventListName"),
        ("RUIJIE-3G-MIB", "ruijie3GTrafficPreventListID"),
        ("RUIJIE-3G-MIB", "ruijie3GTrafficPreventIfIndex"),
        ("RUIJIE-3G-MIB", "ruijie3GTrafficPreventMode"),
        ("RUIJIE-3G-MIB", "ruijie3GPppUsername"),
        ("RUIJIE-3G-MIB", "ruijie3GRouterSN"),
        ("RUIJIE-3G-MIB", "ruijie3GCardPhoneNumber"),
        ("RUIJIE-3G-MIB", "ruijie3GDailMode"),
        ("RUIJIE-3G-MIB", "ruijie3GDialOnDemandIfIndex"),
        ("RUIJIE-3G-MIB", "ruijie3GDeviceModemType"))
)
if mibBuilder.loadTexts:
    ruijie3GUserUpLine.setStatus(
        "current"
    )

ruijie3GUserDownLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 2, 1, 3)
)
ruijie3GUserDownLine.setObjects(
      *(("RUIJIE-3G-MIB", "ruijie3GRouterSlotNumber"),
        ("RUIJIE-3G-MIB", "ruijie3GCardIMSI"),
        ("RUIJIE-3G-MIB", "ruijie3GIntfIPAddr"),
        ("RUIJIE-3G-MIB", "ruijie3GTrafficPreventListName"),
        ("RUIJIE-3G-MIB", "ruijie3GTrafficPreventListID"),
        ("RUIJIE-3G-MIB", "ruijie3GTrafficPreventIfIndex"),
        ("RUIJIE-3G-MIB", "ruijie3GTrafficPreventMode"),
        ("RUIJIE-3G-MIB", "ruijie3GPppUsername"),
        ("RUIJIE-3G-MIB", "ruijie3GRouterSN"),
        ("RUIJIE-3G-MIB", "ruijie3GCardPhoneNumber"),
        ("RUIJIE-3G-MIB", "ruijie3GDailMode"),
        ("RUIJIE-3G-MIB", "ruijie3GDialOnDemandIfIndex"),
        ("RUIJIE-3G-MIB", "ruijie3GDeviceModemType"))
)
if mibBuilder.loadTexts:
    ruijie3GUserDownLine.setStatus(
        "current"
    )

ruijie3GRssiNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 2, 1, 4)
)
ruijie3GRssiNotification.setObjects(
      *(("RUIJIE-3G-MIB", "ruijie3GRouterSlotNumber"),
        ("RUIJIE-3G-MIB", "ruijie3GCardIMSI"),
        ("RUIJIE-3G-MIB", "ruijie3GRouterSN"),
        ("RUIJIE-3G-MIB", "ruijie3GIntfIPAddr"),
        ("RUIJIE-3G-MIB", "ruijie3GRssiStrengthPercent"),
        ("RUIJIE-3G-MIB", "ruijie3GRssiStrength"),
        ("RUIJIE-3G-MIB", "ruijie3GDeviceModemType"))
)
if mibBuilder.loadTexts:
    ruijie3GRssiNotification.setStatus(
        "current"
    )

ruijie3GTrafficInfoNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 2, 1, 5)
)
ruijie3GTrafficInfoNotification.setObjects(
      *(("RUIJIE-3G-MIB", "ruijie3GRouterSlotNumber"),
        ("RUIJIE-3G-MIB", "ruijie3GCardIMSI"),
        ("RUIJIE-3G-MIB", "ruijie3GRouterSN"),
        ("RUIJIE-3G-MIB", "ruijie3GIntfIPAddr"),
        ("RUIJIE-3G-MIB", "ruijie3GOutOctets"),
        ("RUIJIE-3G-MIB", "ruijie3GInOctets"),
        ("RUIJIE-3G-MIB", "ruijie3GDeviceModemType"),
        ("RUIJIE-3G-MIB", "ruijie3GLineCardType"),
        ("RUIJIE-3G-MIB", "ruijie3GModemIMEI"),
        ("RUIJIE-3G-MIB", "ruijie3GCardPhoneNumber"),
        ("RUIJIE-3G-MIB", "ruijie3GDeviceBackupInfo"),
        ("RUIJIE-3G-MIB", "ruijie3GRssiStrength"),
        ("RUIJIE-3G-MIB", "ruijie3GRssiStrengthPercent"),
        ("RUIJIE-3G-MIB", "ruijie3GNetworkISPMode"),
        ("RUIJIE-3G-MIB", "ruijie3GNetworkSysMode"),
        ("RUIJIE-3G-MIB", "ruijie3GSIMCardStatus"),
        ("RUIJIE-3G-MIB", "ruijie3GDailMode"),
        ("RUIJIE-3G-MIB", "ruijie3GPppUsername"),
        ("RUIJIE-3G-MIB", "ruijie3GUserActiveTime"),
        ("RUIJIE-3G-MIB", "ruijie3GAcessBSCellID"),
        ("RUIJIE-3G-MIB", "ruijie3GAcessBSLAC"),
        ("RUIJIE-3G-MIB", "ruijie3GAcessBSLONG"),
        ("RUIJIE-3G-MIB", "ruijie3GAcessBSLAT"),
        ("RUIJIE-3G-MIB", "ruijie3GInSpeed"),
        ("RUIJIE-3G-MIB", "ruijie3GOutSpeed"),
        ("RUIJIE-3G-MIB", "ruijie3G2ifIndex"),
        ("RUIJIE-3G-MIB", "ruijie3GTrafficTrapInterval"),
        ("RUIJIE-3G-MIB", "ruijie3GRssiThreshold"),
        ("RUIJIE-3G-MIB", "ruijie3GTrapFilterMode"),
        ("RUIJIE-3G-MIB", "ruijie3GISPtimeout"),
        ("RUIJIE-3G-MIB", "ruijie3GNetworkISPName"))
)
if mibBuilder.loadTexts:
    ruijie3GTrafficInfoNotification.setStatus(
        "current"
    )

ruijie3GBackupMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 2, 1, 6)
)
ruijie3GBackupMaster.setObjects(
      *(("RUIJIE-3G-MIB", "ruijie3GRouterSlotNumber"),
        ("RUIJIE-3G-MIB", "ruijie3GCardIMSI"),
        ("RUIJIE-3G-MIB", "ruijie3GIntfIPAddr"),
        ("RUIJIE-3G-MIB", "ruijie3GTrafficPreventListName"),
        ("RUIJIE-3G-MIB", "ruijie3GTrafficPreventListID"),
        ("RUIJIE-3G-MIB", "ruijie3GTrafficPreventIfIndex"),
        ("RUIJIE-3G-MIB", "ruijie3GTrafficPreventMode"),
        ("RUIJIE-3G-MIB", "ruijie3GPppUsername"),
        ("RUIJIE-3G-MIB", "ruijie3GRouterSN"),
        ("RUIJIE-3G-MIB", "ruijie3GCardPhoneNumber"),
        ("RUIJIE-3G-MIB", "ruijie3GDailMode"),
        ("RUIJIE-3G-MIB", "ruijie3GDialOnDemandIfIndex"),
        ("RUIJIE-3G-MIB", "ruijie3GDeviceModemType"))
)
if mibBuilder.loadTexts:
    ruijie3GBackupMaster.setStatus(
        "current"
    )

ruijie3GBackupSlave = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 95, 2, 1, 7)
)
ruijie3GBackupSlave.setObjects(
      *(("RUIJIE-3G-MIB", "ruijie3GRouterSlotNumber"),
        ("RUIJIE-3G-MIB", "ruijie3GCardIMSI"),
        ("RUIJIE-3G-MIB", "ruijie3GIntfIPAddr"),
        ("RUIJIE-3G-MIB", "ruijie3GTrafficPreventListName"),
        ("RUIJIE-3G-MIB", "ruijie3GTrafficPreventListID"),
        ("RUIJIE-3G-MIB", "ruijie3GTrafficPreventIfIndex"),
        ("RUIJIE-3G-MIB", "ruijie3GTrafficPreventMode"),
        ("RUIJIE-3G-MIB", "ruijie3GPppUsername"),
        ("RUIJIE-3G-MIB", "ruijie3GRouterSN"),
        ("RUIJIE-3G-MIB", "ruijie3GCardPhoneNumber"),
        ("RUIJIE-3G-MIB", "ruijie3GDailMode"),
        ("RUIJIE-3G-MIB", "ruijie3GDialOnDemandIfIndex"),
        ("RUIJIE-3G-MIB", "ruijie3GDeviceModemType"))
)
if mibBuilder.loadTexts:
    ruijie3GBackupSlave.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-3G-MIB",
    **{"ruijie3GMonitor": ruijie3GMonitor,
       "ruijie3GObjects": ruijie3GObjects,
       "ruijie3GTable": ruijie3GTable,
       "ruijie3GEntry": ruijie3GEntry,
       "ruijie3gUsername": ruijie3gUsername,
       "ruijie3GOnlineStatus": ruijie3GOnlineStatus,
       "ruijie3GIMEI": ruijie3GIMEI,
       "ruijie3GIPAddrType": ruijie3GIPAddrType,
       "ruijie3GIPAddr": ruijie3GIPAddr,
       "ruijie3GUplineTime": ruijie3GUplineTime,
       "ruijie3GActiveTime": ruijie3GActiveTime,
       "ruijie3GSignalStrength": ruijie3GSignalStrength,
       "ruijie3GISP": ruijie3GISP,
       "ruijie3GSysMode": ruijie3GSysMode,
       "ruijie3GServiceStatus": ruijie3GServiceStatus,
       "ruijie3GRoamingStatus": ruijie3GRoamingStatus,
       "ruijie3GDomain": ruijie3GDomain,
       "ruijie3GSIMStatus": ruijie3GSIMStatus,
       "ruijie3GSignalStrengthPercent": ruijie3GSignalStrengthPercent,
       "ruijie3GApn": ruijie3GApn,
       "ruijie3GCellID": ruijie3GCellID,
       "ruijie3GLAC": ruijie3GLAC,
       "ruijie3GBSID": ruijie3GBSID,
       "ruijie3GNID": ruijie3GNID,
       "ruijie3GSID": ruijie3GSID,
       "ruijie3GIMSI": ruijie3GIMSI,
       "ruijie3GESN": ruijie3GESN,
       "ruijie3GPhoneNumber": ruijie3GPhoneNumber,
       "ruijie3GifIndex": ruijie3GifIndex,
       "ruijie3GBSLONG": ruijie3GBSLONG,
       "ruijie3GBSLAT": ruijie3GBSLAT,
       "ruijie3GBackupInfo": ruijie3GBackupInfo,
       "ruijie3GSerialNumber": ruijie3GSerialNumber,
       "ruijie3GBackupIMSI": ruijie3GBackupIMSI,
       "ruijie3GGatewayIPAddr": ruijie3GGatewayIPAddr,
       "ruijie3GLineDownCause": ruijie3GLineDownCause,
       "ruijie3GModemType": ruijie3GModemType,
       "ruijie3GStatTable": ruijie3GStatTable,
       "ruijie3GStatEntry": ruijie3GStatEntry,
       "ruijie3GInOctets": ruijie3GInOctets,
       "ruijie3GOutOctets": ruijie3GOutOctets,
       "ruijie3GInSpeed": ruijie3GInSpeed,
       "ruijie3GOutSpeed": ruijie3GOutSpeed,
       "ruijie3G2IMSI": ruijie3G2IMSI,
       "ruijie3G2ifIndex": ruijie3G2ifIndex,
       "ruijie3GTrap": ruijie3GTrap,
       "ruijie3GNotifications": ruijie3GNotifications,
       "ruijie3GSignalThreshold": ruijie3GSignalThreshold,
       "ruijie3GUpLine": ruijie3GUpLine,
       "ruijie3GDownLine": ruijie3GDownLine,
       "ruijie3GChangeAccessPoint": ruijie3GChangeAccessPoint,
       "ruijie3GBackupIntfSwitch": ruijie3GBackupIntfSwitch,
       "ruijie3GBaseSationSwitch": ruijie3GBaseSationSwitch,
       "ruijie3GTrafficInformation": ruijie3GTrafficInformation,
       "ruijie3GBsNumber": ruijie3GBsNumber,
       "ruijie3GBsTable": ruijie3GBsTable,
       "ruijie3GBsEntry": ruijie3GBsEntry,
       "ruijie3GBsSN": ruijie3GBsSN,
       "ruijie3GBsISP": ruijie3GBsISP,
       "ruijie3GBsMode": ruijie3GBsMode,
       "ruijie3GBsIMSI": ruijie3GBsIMSI,
       "ruijie3GBsLAC": ruijie3GBsLAC,
       "ruijie3GBsCellID": ruijie3GBsCellID,
       "ruijie3GBsBSID": ruijie3GBsBSID,
       "ruijie3GBsSID": ruijie3GBsSID,
       "ruijie3GBsNID": ruijie3GBsNID,
       "ruijie3GBsRssi": ruijie3GBsRssi,
       "ruijie3GBsBSLONG": ruijie3GBsBSLONG,
       "ruijie3GBsBSLAT": ruijie3GBsBSLAT,
       "ruijie3GDeviceManagementTable": ruijie3GDeviceManagementTable,
       "ruijie3GDeviceManagementEntry": ruijie3GDeviceManagementEntry,
       "ruijie3GRouterType": ruijie3GRouterType,
       "ruijie3GRouterSN": ruijie3GRouterSN,
       "ruijie3GRouterSlotNumber": ruijie3GRouterSlotNumber,
       "ruijie3GLineCardType": ruijie3GLineCardType,
       "ruijie3GCardIMSI": ruijie3GCardIMSI,
       "ruijie3GModemIMEI": ruijie3GModemIMEI,
       "ruijie3GIntfIPAddr": ruijie3GIntfIPAddr,
       "ruijie3GCardPhoneNumber": ruijie3GCardPhoneNumber,
       "ruijie3GLineDetected": ruijie3GLineDetected,
       "ruijie3GLineDetectedResult": ruijie3GLineDetectedResult,
       "ruijie3GLineDetectedMainCause": ruijie3GLineDetectedMainCause,
       "ruijie3GLineDetectedSubCause": ruijie3GLineDetectedSubCause,
       "ruijie3GDeviceBackupInfo": ruijie3GDeviceBackupInfo,
       "ruijie3GRssiStrength": ruijie3GRssiStrength,
       "ruijie3GRssiStrengthPercent": ruijie3GRssiStrengthPercent,
       "ruijie3GNetworkISPMode": ruijie3GNetworkISPMode,
       "ruijie3GNetworkSysMode": ruijie3GNetworkSysMode,
       "ruijie3GNetworkServiceStatus": ruijie3GNetworkServiceStatus,
       "ruijie3GSIMCardStatus": ruijie3GSIMCardStatus,
       "ruijie3GDailMode": ruijie3GDailMode,
       "ruijie3GDeviceBackupIMSI": ruijie3GDeviceBackupIMSI,
       "ruijie3GLineDetectedMode": ruijie3GLineDetectedMode,
       "ruijie3GPppUsername": ruijie3GPppUsername,
       "ruijie3GUserApn": ruijie3GUserApn,
       "ruijie3GModemOnlineStatus": ruijie3GModemOnlineStatus,
       "ruijie3GIntfIPAddrType": ruijie3GIntfIPAddrType,
       "ruijie3GUserUplineTime": ruijie3GUserUplineTime,
       "ruijie3GUserActiveTime": ruijie3GUserActiveTime,
       "ruijie3GSIMRoamingStatus": ruijie3GSIMRoamingStatus,
       "ruijie3GAcessBSCellID": ruijie3GAcessBSCellID,
       "ruijie3GAcessBSLAC": ruijie3GAcessBSLAC,
       "ruijie3GAcessBSLONG": ruijie3GAcessBSLONG,
       "ruijie3GAcessBSLAT": ruijie3GAcessBSLAT,
       "ruijie3GDialOnDemandIfIndex": ruijie3GDialOnDemandIfIndex,
       "ruijie3GTrafficPreventMode": ruijie3GTrafficPreventMode,
       "ruijie3GTrafficPreventIfIndex": ruijie3GTrafficPreventIfIndex,
       "ruijie3GTrafficPreventListID": ruijie3GTrafficPreventListID,
       "ruijie3GTrafficPreventListName": ruijie3GTrafficPreventListName,
       "ruijie3GDeviceModemType": ruijie3GDeviceModemType,
       "ruijie3GTrafficTrapInterval": ruijie3GTrafficTrapInterval,
       "ruijie3GRssiThreshold": ruijie3GRssiThreshold,
       "ruijie3GTrapFilterMode": ruijie3GTrapFilterMode,
       "ruijie3GISPtimeout": ruijie3GISPtimeout,
       "ruijie3GEncryptType": ruijie3GEncryptType,
       "ruijie3GPassword": ruijie3GPassword,
       "ruijie3GNetworkISPName": ruijie3GNetworkISPName,
       "ruijieSIMValidSlot": ruijieSIMValidSlot,
       "ruijieSIMInUseSlot": ruijieSIMInUseSlot,
       "ruijie3GTrapNew": ruijie3GTrapNew,
       "ruijie3GNotificationsNew": ruijie3GNotificationsNew,
       "ruijie3GLineDetectedNotification": ruijie3GLineDetectedNotification,
       "ruijie3GUserUpLine": ruijie3GUserUpLine,
       "ruijie3GUserDownLine": ruijie3GUserDownLine,
       "ruijie3GRssiNotification": ruijie3GRssiNotification,
       "ruijie3GTrafficInfoNotification": ruijie3GTrafficInfoNotification,
       "ruijie3GBackupMaster": ruijie3GBackupMaster,
       "ruijie3GBackupSlave": ruijie3GBackupSlave}
)
