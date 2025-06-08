# SNMP MIB module (CEM-CN1000-USER) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-CN1000-USER.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:49:20 2025
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

(catena,) = mibBuilder.importSymbols(
    "CEM-SMI",
    "catena")

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

cnCN1000UserModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 26)
)


# Types definitions



class Cn1000AccessLevels(Integer32):
    """Custom type Cn1000AccessLevels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("admin", 1),
          ("dataadmin", 2),
          ("voiceadmin", 3),
          ("reader", 4),
          ("onuinstaller", 5),
          ("tl1", 6),
          ("operator", 7),
          ("commission", 8))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cn1000UserTable_Object = MibTable
cn1000UserTable = _Cn1000UserTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 26, 1)
)
if mibBuilder.loadTexts:
    cn1000UserTable.setStatus("current")
_Cn1000UserEntry_Object = MibTableRow
cn1000UserEntry = _Cn1000UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 26, 1, 1)
)
cn1000UserEntry.setIndexNames(
    (1, "CEM-CN1000-USER", "cn1000UserName"),
)
if mibBuilder.loadTexts:
    cn1000UserEntry.setStatus("current")


class _Cn1000UserName_Type(SnmpAdminString):
    """Custom type cn1000UserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 20),
    )


_Cn1000UserName_Type.__name__ = "SnmpAdminString"
_Cn1000UserName_Object = MibTableColumn
cn1000UserName = _Cn1000UserName_Object(
    (1, 3, 6, 1, 4, 1, 6352, 26, 1, 1, 1),
    _Cn1000UserName_Type()
)
cn1000UserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000UserName.setStatus("current")


class _Cn1000UserPassword_Type(OctetString):
    """Custom type cn1000UserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Cn1000UserPassword_Type.__name__ = "OctetString"
_Cn1000UserPassword_Object = MibTableColumn
cn1000UserPassword = _Cn1000UserPassword_Object(
    (1, 3, 6, 1, 4, 1, 6352, 26, 1, 1, 2),
    _Cn1000UserPassword_Type()
)
cn1000UserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000UserPassword.setStatus("current")


class _Cn1000UserPasswordExpiration_Type(Integer32):
    """Custom type cn1000UserPasswordExpiration based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Cn1000UserPasswordExpiration_Type.__name__ = "Integer32"
_Cn1000UserPasswordExpiration_Object = MibTableColumn
cn1000UserPasswordExpiration = _Cn1000UserPasswordExpiration_Object(
    (1, 3, 6, 1, 4, 1, 6352, 26, 1, 1, 3),
    _Cn1000UserPasswordExpiration_Type()
)
cn1000UserPasswordExpiration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000UserPasswordExpiration.setStatus("current")
_Cn1000UserLevel_Type = Cn1000AccessLevels
_Cn1000UserLevel_Object = MibTableColumn
cn1000UserLevel = _Cn1000UserLevel_Object(
    (1, 3, 6, 1, 4, 1, 6352, 26, 1, 1, 4),
    _Cn1000UserLevel_Type()
)
cn1000UserLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000UserLevel.setStatus("current")
_Cn1000UserEnabled_Type = TruthValue
_Cn1000UserEnabled_Object = MibTableColumn
cn1000UserEnabled = _Cn1000UserEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6352, 26, 1, 1, 5),
    _Cn1000UserEnabled_Type()
)
cn1000UserEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000UserEnabled.setStatus("current")


class _Cn1000UserDistributionList_Type(OctetString):
    """Custom type cn1000UserDistributionList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Cn1000UserDistributionList_Type.__name__ = "OctetString"
_Cn1000UserDistributionList_Object = MibTableColumn
cn1000UserDistributionList = _Cn1000UserDistributionList_Object(
    (1, 3, 6, 1, 4, 1, 6352, 26, 1, 1, 6),
    _Cn1000UserDistributionList_Type()
)
cn1000UserDistributionList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000UserDistributionList.setStatus("current")
_Cn1000UserRowStatus_Type = RowStatus
_Cn1000UserRowStatus_Object = MibTableColumn
cn1000UserRowStatus = _Cn1000UserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 26, 1, 1, 7),
    _Cn1000UserRowStatus_Type()
)
cn1000UserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000UserRowStatus.setStatus("current")
_Cn100010UserGroups_ObjectIdentity = ObjectIdentity
cn100010UserGroups = _Cn100010UserGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 26, 2)
)

# Managed Objects groups

cn100010UserObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 26, 2, 1)
)
cn100010UserObjectGroup.setObjects(
      *(("CEM-CN1000-USER", "cn1000UserPassword"),
        ("CEM-CN1000-USER", "cn1000UserPasswordExpiration"),
        ("CEM-CN1000-USER", "cn1000UserLevel"),
        ("CEM-CN1000-USER", "cn1000UserDistributionList"),
        ("CEM-CN1000-USER", "cn1000UserRowStatus"),
        ("CEM-CN1000-USER", "cn1000UserEnabled"))
)
if mibBuilder.loadTexts:
    cn100010UserObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-CN1000-USER",
    **{"Cn1000AccessLevels": Cn1000AccessLevels,
       "cnCN1000UserModule": cnCN1000UserModule,
       "cn1000UserTable": cn1000UserTable,
       "cn1000UserEntry": cn1000UserEntry,
       "cn1000UserName": cn1000UserName,
       "cn1000UserPassword": cn1000UserPassword,
       "cn1000UserPasswordExpiration": cn1000UserPasswordExpiration,
       "cn1000UserLevel": cn1000UserLevel,
       "cn1000UserEnabled": cn1000UserEnabled,
       "cn1000UserDistributionList": cn1000UserDistributionList,
       "cn1000UserRowStatus": cn1000UserRowStatus,
       "cn100010UserGroups": cn100010UserGroups,
       "cn100010UserObjectGroup": cn100010UserObjectGroup}
)
